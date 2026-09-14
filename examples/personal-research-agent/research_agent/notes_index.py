"""笔记库检索:纯 Python TF-IDF,不依赖重型向量库。

对应第 15 章 8.3 节"案例 RAG 最小实现":
- 切分:按 Markdown 标题切 chunk,≤ 500 字,重叠 50 字
- 嵌入/检索:这里是 TF-IDF(比书中 numpy 余弦 Embedding 更轻,
  离线可跑,适合千级 chunk 的笔记库;万级以上再按 08 章换向量库)

分词:英文/数字按词切,中文按字二元组(bigram)切——不引入 jieba 等
额外依赖,对中英文混合笔记都可用。
"""
from __future__ import annotations

import math
import re
from collections import Counter
from pathlib import Path

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

_LATIN_WORD = re.compile(r"[a-z0-9_]+")
_CJK_RUN = re.compile(r"[一-鿿]+")


def tokenize(text: str) -> list[str]:
    """中英文混合分词:拉丁词 + 中文 bigram。"""
    text = text.lower()
    tokens = _LATIN_WORD.findall(text)
    for run in _CJK_RUN.findall(text):
        if len(run) == 1:
            tokens.append(run)
        else:
            tokens.extend(run[i : i + 2] for i in range(len(run) - 1))
    return tokens


def chunk_markdown(text: str) -> list[str]:
    """按 Markdown 标题切分,再按 500 字 / 50 字重叠滑窗兜底。"""
    sections: list[str] = []
    current: list[str] = []
    for line in text.splitlines():
        if line.lstrip().startswith("#") and current:
            sections.append("\n".join(current))
            current = []
        current.append(line)
    if current:
        sections.append("\n".join(current))

    chunks: list[str] = []
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        if len(sec) <= CHUNK_SIZE:
            chunks.append(sec)
        else:
            start = 0
            while start < len(sec):
                chunks.append(sec[start : start + CHUNK_SIZE])
                start += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks


class NotesIndex:
    """对一个目录下的 Markdown 文件建 TF-IDF 索引。"""

    def __init__(self, notes_dir: Path):
        self.notes_dir = Path(notes_dir)
        self.chunks: list[dict] = []   # {path, snippet, terms}
        self.idf: dict[str, float] = {}
        self._build()

    def _build(self) -> None:
        if not self.notes_dir.is_dir():
            return
        for md in sorted(self.notes_dir.rglob("*.md")):
            try:
                text = md.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            rel = str(md.relative_to(self.notes_dir))
            for chunk in chunk_markdown(text):
                self.chunks.append(
                    {"path": rel, "snippet": chunk, "terms": Counter(tokenize(chunk))}
                )
        # IDF
        df: Counter[str] = Counter()
        for c in self.chunks:
            for term in c["terms"]:
                df[term] += 1
        n = len(self.chunks)
        self.idf = {t: math.log((n + 1) / (d + 1)) + 1 for t, d in df.items()}

    def _tfidf(self, terms: Counter) -> dict[str, float]:
        vec: dict[str, float] = {}
        for t, tf in terms.items():
            idf = self.idf.get(t)
            if idf:
                vec[t] = (1 + math.log(tf)) * idf
        return vec

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """返回 [{path, snippet, score}],按 TF-IDF 余弦相似度降序。"""
        q_vec = self._tfidf(Counter(tokenize(query)))
        if not q_vec:
            return []
        q_norm = math.sqrt(sum(v * v for v in q_vec.values()))
        scored = []
        for c in self.chunks:
            d_vec = self._tfidf(c["terms"])
            dot = sum(q_vec[t] * d_vec.get(t, 0.0) for t in q_vec)
            if dot <= 0:
                continue
            d_norm = math.sqrt(sum(v * v for v in d_vec.values()))
            scored.append((dot / (q_norm * d_norm), c))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [
            {"path": c["path"], "snippet": c["snippet"], "score": round(s, 4)}
            for s, c in scored[: max(1, top_k)]
        ]
