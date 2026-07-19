# 08 - RAG 知识库体系(RAG Stack)

> 检索增强生成技术栈。涵盖 RAG 全流程、Naive/Advanced/Modular RAG 演进、GraphRAG、RAPTOR、HippoRAG、Self-RAG、CRAG、向量数据库、Embedding 模型、Chunk 分块、ANN 索引、Hybrid Search、Reranker、Query Rewriting、RAG 评估等核心概念。本章是 Agent 体系的"知识中枢",理解它 = 知道 Agent 如何"开卷考试"、把外部知识精准接入 LLM。

---

## 0. 专业词汇速查表(Glossary)

> 阅读本章前必看,所有术语均附中英文对照 + 一句话解释。

| 序号 | 术语(英文) | 中文 | 一句话解释 |
|------|------------|------|-----------|
| 1 | **RAG** | 检索增强生成 | Retrieval-Augmented Generation,检索相关文档辅助 LLM 生成 |
| 2 | **Naive RAG** | 朴素 RAG | 最基础的 RAG,分块→向量化→检索→拼接 |
| 3 | **Advanced RAG** | 高级 RAG | 增加预检索/后检索优化的 RAG |
| 4 | **Modular RAG** | 模块化 RAG | 组件化、可编排、可插拔的 RAG 架构 |
| 5 | **GraphRAG** | 图谱 RAG | 微软提出,基于知识图谱做多跳推理与全局总结 |
| 6 | **RAPTOR** | 树状分层 RAG | Recursive Abstractive Processing,树状分层索引 |
| 7 | **HippoRAG** | 海马体 RAG | 模拟人类海马体记忆机制,多跳推理增强 |
| 8 | **Self-RAG** | 自反思 RAG | LLM 自主决定是否检索,并对结果反思 |
| 9 | **CRAG** | 纠正 RAG | Corrective RAG,检索结果质量评估与纠正 |
| 10 | **Embedding** | 嵌入/向量化 | 把文本映射为高维向量 |
| 11 | **Embedding Model** | 嵌入模型 | 文本转向量的模型(如 BGE、text-embedding-3) |
| 12 | **Vector Database** | 向量数据库 | 专门存储和检索向量的数据库 |
| 13 | **Chunk** | 文本块 | 文档切分后的最小检索单元 |
| 14 | **Chunking** | 分块 | 把长文档切分为块的过程 |
| 15 | **Splitter** | 分割器 | 实现分块的工具 |
| 16 | **Overlap** | 重叠 | 相邻块之间保留的重叠区域,避免边界丢信息 |
| 17 | **Index** | 索引 | 加速向量相似度搜索的数据结构 |
| 18 | **ANN** | 近似最近邻 | Approximate Nearest Neighbor,近似最近邻搜索 |
| 19 | **HNSW** | 层次导航小世界图 | 最常用的 ANN 索引算法 |
| 20 | **IVF** | 倒排文件索引 | 聚类后搜索的 ANN 算法 |
| 21 | **PQ** | 乘积量化 | Product Quantization,向量压缩算法 |
| 22 | **Metadata** | 元数据 | 附加在向量上的结构化数据,用于过滤 |
| 23 | **Retrieval** | 检索 | 从知识库找最相关文档的过程 |
| 24 | **Top-K** | 前 K 个 | 返回最相关的 K 个结果 |
| 25 | **Hybrid Search** | 混合检索 | 向量检索 + 关键词检索融合 |
| 26 | **Reranker** | 重排器 | 对初检结果二次排序,提升精度 |
| 27 | **Query Rewriting** | 查询改写 | 用 LLM 改写用户查询以提升检索效果 |
| 28 | **HyDE** | 假设文档嵌入 | Hypothetical Document Embeddings,先让 LLM 写答案再检索 |
| 29 | **RRF** | 倒数排名融合 | Reciprocal Rank Fusion,多路检索结果融合 |
| 30 | **Recall/Precision** | 召回率/精确率 | 检索质量的核心评估指标 |
| 31 | **MRR** | 平均倒数排名 | Mean Reciprocal Rank,第一个相关结果的排名倒数 |
| 32 | **NDCG** | 归一化折损增益 | 考虑排名位置的检索质量指标 |
| 33 | **BM25** | BM25 算法 | 经典关键词检索算法,基于词频和文档长度 |
| 34 | **Dense Retrieval** | 稠密检索 | 基于向量的语义检索 |
| 35 | **Sparse Retrieval** | 稀疏检索 | 基于关键词的检索(如 BM25) |
| 36 | **Knowledge Base** | 知识库 | 供 RAG 检索的结构化/非结构化知识集合 |
| 37 | **Document Loader** | 文档加载器 | 从各种来源加载文档的组件 |
| 38 | **Contextual Retrieval** | 上下文检索 | Anthropic 提出,给每个块加上下文前缀 |
| 39 | **RAGAS** | RAG 评估框架 | RAG Assessment,自动化评估 RAG 系统 |
| 40 | **Long Context** | 长上下文 | 利用超长上下文窗口替代部分 RAG 场景 |

---

## 一、RAG(检索增强生成)基础

### 1.1 基础定义

**全称:** Retrieval-Augmented Generation

**定义:** 通过检索外部知识库获取相关文档,作为上下文提供给 LLM,让模型基于事实生成回答,减少幻觉。

**核心思想:** 让 LLM "开卷考试",而不是"闭卷背诵"。

**原始论文:** Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", 2020
- 论文链接:https://arxiv.org/abs/2005.11401
- 机构:Meta AI(Facebook AI Research)

### 1.2 为什么需要 RAG

| 问题 | LLM 单独的局限 | RAG 的解决方案 |
|------|---------------|---------------|
| **知识截止日期** | 训练数据有截止时间,不知道最新事件 | 检索最新文档,实时接入 |
| **幻觉问题** | 模型可能编造看似合理的事实 | 基于检索到的事实生成,可溯源 |
| **私有数据** | 私有数据无法预训练进模型 | 检索私有知识库,无需训练 |
| **可追溯性** | 黑盒,无法知道答案从哪来 | 答案可关联到具体文档来源 |
| **成本** | 微调训练成本高 | 只需检索,无需训练 |
| **领域知识** | 通用模型缺乏专业领域深度 | 接入领域知识库,即时专业 |
| **更新频率** | 重新训练周期长、成本高 | 知识库随时更新,即时生效 |
| **多语言/多模态** | 跨语言、跨模态能力有限 | 多语言知识库、多模态文档 |

### 1.3 RAG 基本流程(三阶段)

```
┌────────────────────────────────────────────────────────────────────┐
│                      RAG 标准三阶段流程                              │
│                                                                    │
│  ┌──────────────┐                                                  │
│  │  用户提问     │                                                  │
│  └──────┬───────┘                                                  │
│         ↓                                                          │
│  ┌──────────────────────────────────────────────────┐              │
│  │  [1] 检索(Retrieval)                              │              │
│  │      ├── 问题向量化(Embedding)                   │              │
│  │      ├── 向量相似度搜索(ANN Search)              │              │
│  │      ├── 元数据过滤(Metadata Filter)             │              │
│  │      └── 返回 Top-K 相关文档                      │              │
│  └──────────────────────────────────────────────────┘              │
│         ↓                                                          │
│  ┌──────────────────────────────────────────────────┐              │
│  │  [2] 增强(Augmentation)                          │              │
│  │      ├── 拼接检索到的文档到 Prompt                │              │
│  │      ├── 加入引用信息(Source Citation)           │              │
│  │      └── 加入系统指令(只基于文档回答)            │              │
│  └──────────────────────────────────────────────────┘              │
│         ↓                                                          │
│  ┌──────────────────────────────────────────────────┐              │
│  │  [3] 生成(Generation)                            │              │
│  │      ├── LLM 基于检索结果生成回答                 │              │
│  │      ├── 引用来源标注                             │              │
│  │      └── 处理"我不知道"场景                       │              │
│  └──────────────────────────────────────────────────┘              │
│         ↓                                                          │
│  ┌──────────────┐                                                  │
│  │  回答+引用源  │                                                  │
│  └──────────────┘                                                  │
└────────────────────────────────────────────────────────────────────┘
```

### 1.4 RAG 的核心价值

| 价值 | 说明 | 对比微调 |
|------|------|---------|
| **事实准确性** | 基于检索到的事实生成,减少幻觉 | 微调仍然可能幻觉 |
| **时效性** | 知识库可实时更新 | 需要重新训练 |
| **私有化** | 可接入企业私有知识库 | 数据训练成本高 |
| **可追溯** | 答案可关联到来源 | 黑盒 |
| **成本低** | 不需要训练,只需检索 | 训练成本高 |
| **可解释** | 知道答案从哪来 | 难以解释 |
| **可撤销** | 删除知识库文档即可"遗忘" | 无法"撤销"已学知识 |
| **多知识源** | 可同时接入多个知识库 | 训练数据混合 |

### 1.5 最简 RAG 代码示例(LangChain)

```python
from langchain_community.document_loaders import TextDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. 加载文档
loader = TextDocumentLoader("knowledge.txt")
docs = loader.load()

# 2. 分块
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 3. 向量化并存储
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings)

# 4. 构建检索器
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 5. 构建 RAG Chain
template = """基于以下上下文回答问题。如果上下文中没有答案,回答"我不知道"。

上下文:
{context}

问题: {question}

回答:"""
prompt = ChatPromptTemplate.from_template(template)

llm = ChatOpenAI(model="gpt-4o", temperature=0)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 6. 提问
answer = rag_chain.invoke("什么是 RAG?")
print(answer)
```

### 1.6 Anthropic Claude 的 RAG 最佳实践

> 来源:Anthropic Contextual Retrieval 官方文档(2024-09)
> https://www.anthropic.com/news/contextual-retrieval

Anthropic 在 2024-09 发布的 Contextual Retrieval 方法,通过给每个块加上下文前缀,将检索失败率降低 49%(配合重排降低 67%):

```python
# Contextual Retrieval:给每个 Chunk 加上文档级上下文
def add_context_to_chunk(chunk, document_summary):
    """用 LLM 为每个块生成上下文前缀"""
    prompt = f"""<document>
{document_summary}
</document>
Here is the chunk we want to situate within the whole document:
<chunk>
{chunk.content}
</chunk>
Please give a short succinct context to situate this chunk within the overall document
for the purposes of improving search retrieval of the chunk.
Answer only with the succinct context and nothing else."""
    
    context = llm.invoke(prompt)
    chunk.content = f"{context}\n\n{chunk.content}"
    return chunk
```

---

## 二、RAG 的演进(Naive → Advanced → Modular)

### 2.1 演进总览

```
2020 RAG 原始论文
    ↓
Naive RAG(朴素 RAG)        ── 简单分块+向量检索+生成
    ↓ 问题:召回低、噪声多、无优化
Advanced RAG(高级 RAG)      ── 增加预检索/后检索优化
    ↓ 进一步组件化
Modular RAG(模块化 RAG)     ── 可插拔、可编排、可组合
    ↓ 智能化
Self-RAG / CRAG / Adaptive RAG ── LLM 自主决策是否检索、检索什么
    ↓
Agentic RAG(2024+)         ── Agent + RAG,多轮检索、多源检索
```

### 2.2 Naive RAG(朴素 RAG)

**结构:**

```
文档 → 分块 → 向量化 → 存入向量库
                              ↓
查询 → 向量化 → 相似度搜索 → Top-K → 拼接到 Prompt → LLM 生成
```

**特点:**
- 流程简单,易于实现
- 单一检索策略(纯向量)
- 无查询优化、无重排

**问题:**
| 问题 | 说明 |
|------|------|
| **分块粒度难把握** | 太大噪声多,太小上下文丢失 |
| **检索结果可能不相关** | 单纯向量相似度有限 |
| **没有排序和重排** | 相关结果可能排在后面 |
| **查询表达不清时效果差** | 用户问得模糊,检索就模糊 |
| **不支持多跳推理** | A→B→C 类问题无法回答 |

### 2.3 Advanced RAG(高级 RAG)

**结构:**

```
┌──────────────────────────────────────────────────────────┐
│              Advanced RAG 三阶段优化                       │
│                                                          │
│  [预检索 Pre-retrieval]                                   │
│    ├── 查询改写(Query Rewriting)                         │
│    ├── 查询扩展(Query Expansion)                         │
│    ├── 查询分解(Query Decomposition)                     │
│    ├── HyDE(Hypothetical Document)                       │
│    └── 分块策略优化(Chunking Strategy)                   │
│              ↓                                           │
│  [检索 Retrieval]                                         │
│    ├── 混合检索(Hybrid Search)                            │
│    │   ├── 向量检索(Dense Retrieval)                     │
│    │   └── 关键词检索(Sparse Retrieval / BM25)           │
│    ├── 元数据过滤(Metadata Filter)                       │
│    └── 多路检索(Multi-route Retrieval)                   │
│              ↓                                           │
│  [后检索 Post-retrieval]                                  │
│    ├── 重排(Reranking)                                   │
│    ├── 去重(Deduplication)                               │
│    ├── 压缩(Context Compression)                         │
│    └── 引用标注(Source Citation)                         │
│              ↓                                           │
│  [生成 Generation]                                        │
│    ├── Prompt 优化                                        │
│    ├── 引用强化                                           │
│    └── 自我反思(Self-Reflection)                         │
└──────────────────────────────────────────────────────────┘
```

### 2.4 Modular RAG(模块化 RAG)

**特点:** 组件化、可插拔、可编排,如 LlamaIndex、LangChain。

**核心模块:**

| 模块 | 功能 | 可选组件 |
|------|------|---------|
| **Indexing** | 文档加载、分块、向量化 | PDFLoader、RecursiveSplitter、BGE |
| **Pre-retrieval** | 查询优化 | QueryRewriter、HyDE、StepBack |
| **Retrieval** | 检索 | VectorRetriever、BM25Retriever、HybridRetriever |
| **Post-retrieval** | 结果处理 | Reranker、Compressor、Deduplicator |
| **Generation** | 答案生成 | LLM、Prompt Template |
| **Orchestration** | 编排 | Router、Loop、Adaptive |
| **Evaluation** | 评估 | RAGAS、TruLens |

### 2.5 三代 RAG 对比

| 维度 | Naive RAG | Advanced RAG | Modular RAG |
|------|-----------|--------------|-------------|
| **结构** | 线性流水线 | 三阶段优化 | 模块化组件 |
| **检索** | 纯向量 | 混合+重排 | 可插拔多种 |
| **查询** | 直接用 | 改写+扩展 | 自适应决策 |
| **编排** | 固定流程 | 固定流程 | 动态编排 |
| **评估** | 无 | 离线评估 | 在线+离线 |
| **复杂度** | 低 | 中 | 高 |
| **灵活性** | 低 | 中 | 高 |
| **典型工具** | 简单脚本 | LangChain | LlamaIndex/LangGraph |

---

## 三、GraphRAG(图谱检索增强)

### 3.1 基础定义

**定义:** 结合知识图谱的 RAG,利用实体关系进行多跳推理和全局理解。

**提出方:** Microsoft,2024-04
**GitHub:** https://github.com/microsoft/graphrag
**论文:** "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"(Edge et al., 2024-04)
**论文链接:** https://arxiv.org/abs/2404.16130

### 3.2 GraphRAG 的核心思想

传统 RAG 基于向量相似度搜索,适合匹配字面相关的内容,但有以下局限:
- **无法多跳推理:** A 影响 B,B 影响 C,推理 A 间接影响 C
- **无法全局理解:** 总结整个文档集主题
- **无法回答关系问题:** "X 和 Y 的关系是什么?"

GraphRAG 通过构建知识图谱,支持:
- **多跳推理(A → B → C):** 沿图谱边遍历
- **全局理解:** 社区摘要覆盖整个文档集
- **实体关系查询:** 直接查图
- **复杂问题解答:** 综合多个实体和关系

### 3.3 GraphRAG vs 传统 RAG

| 维度 | 传统 RAG | GraphRAG |
|------|----------|----------|
| **结构** | 向量 + 文本块 | 知识图谱(实体+关系) |
| **强项** | 简单问答、字面匹配 | 多跳推理、全局总结 |
| **构建成本** | 低 | 高(需要抽取实体关系) |
| **检索方式** | 相似度搜索 | 图遍历 + 子图检索 |
| **适合场景** | 通用问答 | 实体密集、关系复杂 |
| **回答类型** | 局部事实 | 全局总结、关系推理 |
| **Token 消耗** | 中 | 高(社区摘要多) |
| **更新难度** | 易(增删向量) | 难(图结构变更) |

### 3.4 GraphRAG 构建流程(Indexing)

```
原始文档
    ↓
[1] 文本分块(Chunking)
    ↓
[2] 实体抽取(Entity Extraction)
    ├── 用 LLM 从每个块抽取实体
    ├── 实体类型:人物/组织/地点/概念/...
    └── 输出:实体列表 + 实体描述
    ↓
[3] 关系抽取(Relation Extraction)
    ├── 用 LLM 抽取实体间关系
    ├── 关系类型:属于/影响/位于/...
    └── 输出:关系三元组(主体,关系,客体)
    ↓
[4] 图谱构建(Graph Construction)
    ├── 节点:实体
    ├── 边:关系
    ├── 属性:描述、来源、权重
    └── 输出:完整知识图谱
    ↓
[5] 社区发现(Community Detection)
    ├── 用 Leiden 算法划分社区
    ├── 社区 = 紧密相关的实体集合
    └── 输出:社区层级结构
    ↓
[6] 社区摘要(Community Summarization)
    ├── 用 LLM 为每个社区生成摘要
    ├── 自底向上构建层级摘要
    └── 输出:多层级社区摘要
    ↓
[7] 索引存储
    ├── 图谱存储(Neo4j / NetworkX)
    ├── 向量索引(实体/关系/块)
    └── 社区摘要索引
```

### 3.5 GraphRAG 检索流程(Query)

GraphRAG 支持两种查询模式:

#### 3.5.1 Global Search(全局查询)

适合"总结性"问题,如"这个文档集的主要主题是什么?"

```
用户问题
    ↓
[1] 社区摘要映射:把问题映射到相关社区
    ↓
[2] 多社区回答生成:每个社区独立生成部分回答
    ↓
[3] 答案聚合:把多社区回答聚合成最终答案
```

#### 3.5.2 Local Search(局部查询)

适合"具体实体/关系"问题,如"张三和谁有关系?"

```
用户问题
    ↓
[1] 实体识别:从问题中识别关键实体
    ↓
[2] 子图抽取:从图谱中抽取相关子图(实体+关系)
    ↓
[3] 社区匹配:找到相关社区摘要
    ↓
[4] 上下文组装:子图 + 社区摘要 + 相关文档块
    ↓
[5] LLM 生成:基于丰富上下文回答
```

### 3.6 GraphRAG 代码示例

```python
# 使用微软 GraphRAG 官方库
# pip install graphrag

import graphrag

# 1. 初始化配置
graphrag.init(root_dir="./graphrag_workspace")

# 2. 构建索引(抽取实体、关系、社区)
# 命令行: python -m graphrag.index --root ./graphrag_workspace
graphrag.index.run(
    root_dir="./graphrag_workspace",
    documents_dir="./input"
)

# 3. 全局查询
from graphrag.query.structured_search.global_search.search import GlobalSearch
global_search = GlobalSearch(...)
result = global_search.search("这个文档集讨论了哪些主要主题?")
print(result.response)

# 4. 局部查询
from graphrag.query.structured_search.local_search.search import LocalSearch
local_search = LocalSearch(...)
result = local_search.search("张三和李四是什么关系?")
print(result.response)
```

### 3.7 GraphRAG 适用场景

| 场景 | 示例 | 为什么 GraphRAG 适用 |
|------|------|---------------------|
| **多跳推理** | "X 间接影响了 Y 吗?" | 沿图谱边遍历 |
| **全局总结** | "这本文档集讲了什么?" | 社区摘要覆盖 |
| **关系查询** | "A 和 B 是什么关系?" | 直接查图边 |
| **实体密集** | 人物关系、组织架构 | 图谱天然适合 |
| **跨文档关联** | 多文档中的同一实体 | 实体对齐 |

---

## 四、RAPTOR(分层检索框架)

### 4.1 基础定义

**全称:** Recursive Abstractive Processing for Tree-Organized Retrieval

**定义:** 树状分层索引的 RAG 框架,支持从摘要到细节的多层级检索。

**论文:** Sarthi et al., "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval", 2024-01
**论文链接:** https://arxiv.org/abs/2401.18059
**GitHub:** https://github.com/parthsarthi03/raptor

### 4.2 RAPTOR 的核心思想

传统 RAG 只有一个粒度的文本块,无法同时回答"细节问题"和"全局问题":
- 细节问题需要小块(精确匹配)
- 全局问题需要大块(完整上下文)
- 长文档问题需要跨章节理解

RAPTOR 构建树状结构:
- **叶子节点:** 原始文本块(细粒度)
- **中间节点:** 摘要(中粒度)
- **根节点:** 全局摘要(粗粒度)

检索时可以:
- 从顶层摘要开始,逐步下钻
- 根据问题选择合适的粒度
- 支持全局理解 + 细节支撑

### 4.3 RAPTOR 树结构

```
                    ┌─────────────────┐
                    │   全局摘要(根)   │  ← 顶层(粗粒度)
                    │ "整本书讲了..."   │
                    └────────┬────────┘
                             │
            ┌────────────────┴────────────────┐
            ↓                                 ↓
    ┌───────────────┐                 ┌───────────────┐
    │ 章节摘要(L2)   │                 │ 章节摘要(L2)   │  ← 中层
    │ "第1章讲了..."  │                 │ "第2章讲了..."  │
    └───────┬───────┘                 └───────┬───────┘
            │                                 │
        ┌───┴───┐                         ┌───┴───┐
        ↓       ↓                         ↓       ↓
    ┌───────┐┌───────┐                 ┌───────┐┌───────┐
    │ 段落摘要││ 段落摘要│                 │ 段落摘要││ 段落摘要│  ← 底层摘要
    └───┬───┘└───┬───┘                 └───┬───┘└───┬───┘
        │        │                         │        │
    ┌───┴───┐┌───┴───┐                 ┌───┴───┐┌───┴───┐
    │文本块1 ││文本块2 │                 │文本块3 ││文本块4 │  ← 叶子(细粒度)
    └───────┘└───────┘                 └───────┘└───────┘
```

### 4.4 RAPTOR 构建流程

```
[1] 叶子层构建
    ├── 文档分块(按段落/语义)
    ├── 每个块向量化
    └── 存入叶子节点

[2] 聚类
    ├── 对叶子块向量做聚类(如 GMM)
    ├── 把相似的块聚为一组
    └── 每组生成摘要

[3] 摘要层构建
    ├── 用 LLM 为每组生成摘要
    ├── 摘要向量化
    └── 摘要作为上层节点

[4] 递归
    ├── 对摘要再聚类、再摘要
    ├── 直到达到根节点或阈值
    └── 形成多层树
```

### 4.5 RAPTOR 检索策略

#### 4.5.1 树遍历(Tree Traversal)

```
查询
    ↓
从根节点开始,匹配最相关的子节点
    ↓
递归下钻,直到叶子或合适的粒度
    ↓
返回路径上的所有节点
```

适合:从全局到细节的渐进式查询。

#### 4.5.2 折叠树(Collapsed Tree)

```
查询
    ↓
把整棵树"折叠"为扁平的节点列表
    ↓
对所有节点(叶子+摘要)统一向量检索
    ↓
返回 Top-K(可能来自不同层)
```

适合:同时需要摘要和细节的复杂问题。

### 4.6 RAPTOR vs 传统 RAG vs GraphRAG

| 维度 | 传统 RAG | GraphRAG | RAPTOR |
|------|----------|----------|--------|
| **结构** | 扁平向量 | 知识图谱 | 树状分层 |
| **强项** | 简单高效 | 多跳关系 | 全局摘要 + 分层 |
| **适合** | 通用问答 | 实体关系密集 | 长文档总结 |
| **构建复杂度** | 低 | 高 | 中 |
| **检索粒度** | 单一 | 多种 | 多层级 |
| **Token 消耗** | 中 | 高 | 中 |
| **更新难度** | 易 | 难 | 中 |

---

## 五、新型 RAG 变体

### 5.1 Self-RAG(自反思 RAG)

**论文:** Asai et al., "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection", 2023-10
**论文链接:** https://arxiv.org/abs/2310.11511

**核心思想:** LLM 自主决定是否检索、检索什么,并对检索结果进行反思。

```
用户问题
    ↓
[1] Retrieve Token 决策:是否需要检索?
    ├── Yes → 进入 [2]
    └── No → 直接生成
    ↓
[2] 检索
    ↓
[3] IsRel Token 评估:检索结果是否相关?
    ├── Relevant → 使用
    └── Irrelevant → 重新检索或忽略
    ↓
[4] IsUse Token 评估:生成是否基于检索?
    ├── Supported → 输出
    └── Not Supported → 反思并重新生成
    ↓
输出 + 反思标记
```

### 5.2 CRAG(纠正 RAG)

**论文:** Yan et al., "Corrective Retrieval Augmented Generation", 2024-01
**论文链接:** https://arxiv.org/abs/2401.15884

**核心思想:** 评估检索结果质量,低质量时转向网络搜索纠正。

```
检索结果
    ↓
[1] 评估器:检索结果质量如何?
    ├── Correct → 直接用
    ├── Incorrect → 转向网络搜索
    └── Ambiguous → 融合两种结果
    ↓
[2] 知识精炼:去除噪声
    ↓
[3] 生成
```

### 5.3 HippoRAG(海马体 RAG)

**论文:** Gutiérrez et al., "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models", 2024-05
**论文链接:** https://arxiv.org/abs/2405.14831

**核心思想:** 模拟人类海马体的记忆机制,用知识图谱 + Personalized PageRank 做多跳推理。

```
[索引阶段]
    ├── 实体抽取(海马体中的模式分离)
    ├── 知识图谱构建(海马体中的模式补全)
    └── PageRank 索引(记忆关联)

[检索阶段]
    ├── 查询实体识别
    ├── 多跳关联检索(PPR 算法)
    └── 综合多跳路径生成答案
```

### 5.4 Adaptive RAG(自适应 RAG)

**论文:** Jeong et al., "Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models", 2024-01
**论文链接:** https://arxiv.org/abs/2402.10222

**核心思想:** 根据查询复杂度,自适应选择 No Retrieval / Single-step RAG / Multi-step RAG。

```
用户问题
    ↓
[1] 查询复杂度分类器
    ├── 简单(A) → No Retrieval(直接回答)
    ├── 中等(B) → Single-step RAG(单次检索)
    └── 复杂(C) → Multi-step RAG(多步检索)
    ↓
[2] 对应策略执行
    ↓
输出
```

### 5.5 RAG 变体对比

| 变体 | 核心创新 | 适用场景 | 论文年份 |
|------|---------|---------|---------|
| **Naive RAG** | 基础检索+生成 | 通用问答 | 2020 |
| **Advanced RAG** | 预检索+后检索优化 | 生产环境 | 2023 |
| **Modular RAG** | 模块化组件 | 复杂业务 | 2024 |
| **GraphRAG** | 知识图谱+社区 | 多跳推理 | 2024 |
| **RAPTOR** | 树状分层 | 长文档总结 | 2024 |
| **Self-RAG** | 自反思+决策 | 高准确率问答 | 2023 |
| **CRAG** | 检索质量纠正 | 容错性要求高 | 2024 |
| **HippoRAG** | 海马体机制 | 多跳推理 | 2024 |
| **Adaptive RAG** | 复杂度自适应 | 混合复杂度 | 2024 |
| **Agentic RAG** | Agent+RAG | 复杂任务 | 2024+ |

---

## 六、Embedding(嵌入模型)

### 6.1 基础定义

**定义:** 把文本、图像等数据映射为高维向量的过程,使得语义相近的内容在向量空间中也相近。

### 6.2 Embedding 工作原理

```
文本: "猫坐在垫子上"
    ↓
Tokenizer 分词: [猫, 坐, 在, 垫子, 上]
    ↓
Embedding Model(如 BGE)
    ↓
向量: [0.12, -0.34, 0.56, ..., 0.78]  ← 768 维或更高
    ↓
语义相近的文本,向量也相近
    "猫趴在垫子上"  →  [0.11, -0.35, 0.55, ..., 0.77]  (相近)
    "狗跑在草地上"  →  [0.45, 0.23, -0.12, ..., 0.09]  (较远)
```

### 6.3 主流 Embedding 模型对比

| 模型 | 来源 | 维度 | 特点 | 中文支持 | 开源 |
|------|------|------|------|---------|------|
| **text-embedding-3-large** | OpenAI | 3072 | 性能强,API 调用 | 良好 | ❌ |
| **text-embedding-3-small** | OpenAI | 1536 | 性价比高 | 良好 | ❌ |
| **text-embedding-ada-002** | OpenAI | 1536 | 经典版本 | 一般 | ❌ |
| **voyage-3** | Voyage AI | 1024 | 2024 新版,性能强 | 良好 | ❌ |
| **BGE-large-zh-v1.5** | 智源 | 1024 | 中文最佳开源 | 优秀 | ✅ |
| **BGE-m3** | 智源 | 1024 | 多语言+多功能 | 优秀 | ✅ |
| **m3e-large** | MoKa AI | 1024 | 中文优秀开源 | 优秀 | ✅ |
| **gte-large-zh** | 阿里达摩院 | 1024 | 中文优秀 | 优秀 | ✅ |
| **Cohere embed-v3** | Cohere | 1024 | 多语言 | 良好 | ❌ |
| **jina-embeddings-v3** | Jina AI | 1024 | 多语言+长文本 | 良好 | ✅ |
| **E5-mistral-7b** | 微软 | 4096 | 大模型级嵌入 | 良好 | ✅ |
| **NV-Embed-v2** | NVIDIA | 4096 | MTEB 榜单顶级 | 良好 | ✅ |

### 6.4 MTEB 榜单

> MTEB(Massive Text Embedding Benchmark)是嵌入模型的标准评测榜单
> https://huggingface.co/spaces/mteb/leaderboard

**评测任务:**
- Retrieval(检索)
- Reranking(重排)
- Classification(分类)
- Clustering(聚类)
- STS(语义文本相似度)
- Pair Classification(成对分类)
- Bitext Mining(双语文本挖掘)

### 6.5 Embedding 模型选择

| 场景 | 推荐模型 | 理由 |
|------|---------|------|
| **中文为主** | BGE-large-zh-v1.5 / m3e-large | 中文 SOTA |
| **多语言** | BGE-m3 / Cohere embed-v3 | 多语言支持好 |
| **英文为主** | text-embedding-3-large | OpenAI 性能强 |
| **本地部署** | BGE-large / m3e-large | 开源、可商用 |
| **长文本** | jina-embeddings-v3 | 支持 8K token |
| **追求极致** | NV-Embed-v2 / E5-mistral-7b | MTEB 榜单前列 |
| **预算敏感** | text-embedding-3-small | 性价比高 |

### 6.6 Embedding 代码示例

```python
# OpenAI Embedding
from openai import OpenAI
client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-large",
    input="什么是检索增强生成?"
)
vector = response.data[0].embedding  # 3072 维

# 开源 BGE Embedding(本地部署)
from FlagEmbedding import FlagModel
model = FlagModel('BAAI/bge-large-zh-v1.5',
                  query_instruction="为这个句子生成表示以用于检索相关文章:")
vector = model.encode("什么是检索增强生成?")  # 1024 维

# Sentence-Transformers(通用)
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('BAAI/bge-large-zh-v1.5')
vectors = model.encode([
    "猫坐在垫子上",
    "狗跑在草地上",
    "小猫趴在垫子上"
])
# vectors[0] 和 vectors[2] 相似度高,和 vectors[1] 相似度低
```

---

## 七、Chunk(文本分块)

### 7.1 基础定义

**定义:** 将长文档切分为小块(Chunk),每个块独立向量化和存储。

### 7.2 为什么需要分块

| 原因 | 说明 |
|------|------|
| **上下文窗口限制** | LLM 上下文有限,不能塞整个文档 |
| **检索精度** | 太大的块会引入噪声,太小的块会丢失上下文 |
| **向量质量** | 合适粒度的块,向量表征更准确 |
| **Token 成本** | 大块导致 Token 消耗高 |
| **检索速度** | 块少则检索快,但精度可能下降 |

### 7.3 分块策略详解

| 策略 | 说明 | 优点 | 缺点 | 适用 |
|------|------|------|------|------|
| **固定大小** | 按字符/token 数切分 | 简单 | 可能切断语义 | 通用 |
| **按句子** | 按句子边界切分 | 语义完整 | 句子长短不一 | 短文本 |
| **按段落** | 按段落切分 | 自然语义单元 | 段落可能太长 | 结构化文档 |
| **按标题** | 按文档标题层级切分 | 结构清晰 | 需要有结构的文档 | Markdown/HTML |
| **递归切分** | 先按大分隔符,再按小的 | 平衡语义和大小 | 略复杂 | 通用(最常用) |
| **语义切分** | 基于语义相似度切分 | 语义最完整 | 成本高、需要模型 | 高精度场景 |
| **代码感知** | 按函数/类切分 | 保留代码结构 | 仅适用代码 | 代码库 |

### 7.4 分块大小选择

| 块大小 | 适用场景 | 优缺点 |
|--------|----------|--------|
| **小(128-256)** | 精确匹配、问答 | 精度高,但上下文不足 |
| **中(512-1024)** | 通用场景 | 平衡精度和上下文 |
| **大(2000+)** | 摘要、长文档理解 | 上下文丰富,但噪声多 |

**经验法则:**
- 通用问答:512 字符左右
- 代码:按函数/类
- 长文档总结:大块或 RAPTOR
- 精确事实:小块 + 重叠

### 7.5 递归分块示例(LangChain 最常用)

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 递归分块:先按段落,再按句号,再按逗号,最后按字符
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", "。", ".", " ", ""],
    keep_separator=True
)

chunks = splitter.split_text(long_text)
```

### 7.6 Markdown 标题分块

```python
from langchain_text_splitters import MarkdownHeaderTextSplitter

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
)

chunks = splitter.split_text(markdown_text)
# 每个 chunk 自带 headers 元数据
```

### 7.7 代码分块

```python
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_text(python_code)
# 优先按 class/function 切分,保留代码结构
```

### 7.8 语义分块(Semantic Chunker)

```python
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="percentile",  # 或 "standard_deviation"
    breakpoint_threshold_amount=95
)

chunks = splitter.split_text(long_text)
# 基于相邻句子向量相似度,相似度低时切分
```

### 7.9 Overlap(重叠)

相邻块之间保留一定的重叠,避免信息在边界处丢失:

```
块1: [这是第一句。这是第二句。][这是第三句。]
块2:                 [这是第三句。][这是第四句。]
                        ↑ overlap
```

**推荐重叠大小:** 块大小的 10%~20%

| 块大小 | 推荐 Overlap |
|--------|-------------|
| 256 | 25-50 |
| 512 | 50-100 |
| 1024 | 100-200 |
| 2048 | 200-400 |

### 7.10 Contextual Retrieval(Anthropic 2024-09)

Anthropic 提出的 Contextual Retrieval,给每个 Chunk 加上文档级上下文前缀:

```python
# 原始 Chunk
chunk = "本节介绍了 RAG 的基本原理..."

# Contextual Retrieval
chunk_with_context = """
本块来自《RAG 技术指南》第 3 章"RAG 基础",该章涵盖 RAG 的三阶段流程。

本节介绍了 RAG 的基本原理...
"""

# 效果:检索失败率降低 49%(单独),67%(配合 BM25)
```

---

## 八、Vector Database(向量数据库)深度

### 8.1 基础定义

**定义:** 专门用于存储和检索向量嵌入的数据库,核心能力是相似度搜索。

### 8.2 向量数据库的核心能力

| 能力 | 说明 |
|------|------|
| **向量存储** | 存储高维向量(通常 384~4096 维) |
| **相似度搜索** | 根据查询向量返回最相似的向量 |
| **索引优化** | 使用 ANN 索引加速搜索 |
| **元数据过滤** | 支持基于元数据的条件过滤 |
| **CRUD 操作** | 向量的增删改查 |
| **持久化** | 数据持久化存储 |
| **水平扩展** | 支持分片、副本 |
| **混合查询** | 向量+标量联合查询 |
| **实时更新** | 支持增量插入和删除 |

### 8.3 相似度计算方法

| 方法 | 公式 | 适用场景 | 取值范围 |
|------|------|----------|---------|
| **余弦相似度(Cosine)** | cosθ = A·B / (|A||B|) | 文本相似度(最常用) | [-1, 1] |
| **欧氏距离(L2)** | d = √(Σ(aᵢ-bᵢ)²) | 图像、空间数据 | [0, ∞) |
| **点积(Dot Product)** | A·B = Σaᵢbᵢ | 归一化向量的快速计算 | (-∞, ∞) |
| **曼哈顿距离(L1)** | d = Σ|aᵢ-bᵢ| | 高维稀疏数据 | [0, ∞) |
| **汉明距离** | 不同维度的个数 | 二进制向量 | [0, dim] |

**何时用哪个:**
- 文本 RAG:Cosine(最常用)
- 归一化向量:Dot Product(等价 Cosine 但更快)
- 图像:L2
- 二进制特征:Hamming

### 8.4 主流向量数据库对比(2026 版)

| 数据库 | 类型 | 特点 | 适用场景 | 官网 |
|--------|------|------|----------|------|
| **Pinecone** | 全托管 SaaS | 高性能、易扩展、无运维 | 生产级、企业 | pinecone.io |
| **Milvus** | 开源、可自托管 | 高性能、功能丰富、云原生 | 大规模、定制化 | milvus.io |
| **Chroma** | 开源、轻量 | 简单易用、Python 友好 | 原型、中小规模 | trychroma.com |
| **Weaviate** | 开源 + SaaS | 模块化、GraphQL、向量+标量 | 语义搜索、知识图谱 | weaviate.io |
| **Qdrant** | 开源 + 云服务 | Rust 实现、高性能、过滤强 | 生产级、高吞吐 | qdrant.tech |
| **pgvector** | PostgreSQL 扩展 | 复用 PG 生态、SQL 查询 | 已有 PG、简单场景 | github.com/pgvector/pgvector |
| **FAISS** | 库(非数据库) | Meta 开源、性能极致、无服务端 | 本地计算、嵌入搜索 | github.com/facebookresearch/faiss |
| **LanceDB** | 开源 | 列式存储、多模态 | 多模态、嵌入式 | lancedb.github.io/lancedb |
| **Vespa** | 开源 | 全功能搜索引擎 | 大规模搜索 | vespa.ai |
| **Redis Vector** | Redis 模块 | 复用 Redis 生态 | 已用 Redis | redis.io |
| **Elasticsearch** | 开源 + 云 | 8.x+ 支持向量 | 已用 ES | elastic.co |

### 8.5 向量数据库选型决策树

```
是否需要全托管?
├── 是 → Pinecone
└── 否 → 是否已有 PostgreSQL?
        ├── 是 → pgvector(简单)/ Milvus(复杂)
        └── 否 → 数据规模?
                ├── 小(< 100万) → Chroma / LanceDB
                ├── 中(100万-1亿) → Qdrant / Weaviate
                └── 大(> 1亿) → Milvus / Vespa
```

### 8.6 ANN(近似最近邻)索引

精确搜索是 O(n),大规模数据下太慢。ANN 用精度换速度:

| 索引类型 | 原理 | 特点 | 适用规模 |
|----------|------|------|---------|
| **HNSW** | 层次化导航小世界图 | 搜索快、内存友好、最常用 | 中大规模 |
| **IVF** | 倒排文件 | 聚类后搜索,适合大规模 | 大规模 |
| **PQ** | 乘积量化 | 压缩向量,节省内存 | 大规模+低内存 |
| **IVF-PQ** | IVF + PQ 组合 | 大规模 + 高压缩 | 超大规模 |
| **ScaNN** | 各向异性量化 | Google 提出,精度高 | 中大规模 |
| **DiskANN** | 磁盘索引 | 内存友好,数据在磁盘 | 超大规模 |
| **Brute Force** | 暴力搜索 | 100% 精度,慢 | 小数据(< 10万) |

### 8.7 HNSW 索引参数详解

HNSW 是最常用的索引类型,关键参数:

| 参数 | 作用 | 影响 | 典型值 |
|------|------|------|--------|
| **M** | 每个节点的连接数 | M 越大,精度越高,内存越大,构建越慢 | 16 |
| **efConstruction** | 构建时的搜索宽度 | 越大构建越慢,索引质量越好 | 200 |
| **efSearch** | 搜索时的搜索宽度 | 越大搜索越慢,召回率越高 | 100 |

**调优经验:**
- M=16, efConstruction=200, efSearch=100 是通用默认值
- 高精度需求:M=32, efSearch=200
- 大规模数据:M=8-12,使用 IVF-PQ 替代

### 8.8 向量数据库代码示例

```python
# 1. Chroma(轻量级)
import chromadb
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.create_collection("docs")
collection.add(
    documents=["文本1", "文本2"],
    metadatas=[{"source": "a.pdf"}, {"source": "b.pdf"}],
    ids=["1", "2"]
)
results = collection.query(query_texts=["查询"], n_results=3)

# 2. Qdrant(生产级)
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

client = QdrantClient(host="localhost", port=6333)
client.create_collection(
    "docs",
    vectors_config=VectorParams(size=1024, distance=Distance.COSINE)
)
client.upsert(
    "docs",
    points=[PointStruct(id=1, vector=[0.1, ...], payload={"text": "..."})]
)
results = client.search("docs", query_vector=[0.2, ...], limit=5)

# 3. Milvus(大规模)
from pymilvus import MilvusClient
client = MilvusClient("milvus.db")
client.create_collection("docs", ...)
client.insert("docs", [...])
results = client.search("docs", data=[query_vector], limit=5)

# 4. pgvector(PostgreSQL)
import psycopg2
conn = psycopg2.connect("dbname=test")
cur = conn.cursor()
cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
cur.execute("CREATE TABLE docs (id serial, content text, embedding vector(1024))")
cur.execute("CREATE INDEX ON docs USING hnsw (embedding vector_cosine_ops)")
```

---

## 九、Retrieval(检索)深度

### 9.1 检索流程

```
用户查询
    ↓
[预检索]
    ├── 查询改写(Query Rewriting)
    ├── 查询扩展(Query Expansion)
    ├── 查询分解(Query Decomposition)
    └── HyDE
    ↓
[检索]
    ├── 向量检索(Dense Retrieval)
    ├── 关键词检索(Sparse Retrieval / BM25)
    ├── 混合检索(Hybrid Search)
    └── 元数据过滤
    ↓
[后检索]
    ├── 重排(Reranking)
    ├── 去重(Deduplication)
    ├── 压缩(Context Compression)
    └── 引用标注
    ↓
Top-K 最终结果
```

### 9.2 Top-K

返回最相关的 K 个结果。K 的选择:
- K 太小:可能漏掉相关结果(召回率低)
- K 太大:引入噪声,占用 Token(精确率低)

**经验值:**
- 初检 K = 20-50
- 重排后取 3-10
- LLM 上下文:5-10 个最佳

### 9.3 检索策略

| 策略 | 说明 | 效果 |
|------|------|------|
| **向量检索(Dense)** | 纯相似度搜索 | 语义匹配,但可能漏字面匹配 |
| **关键词检索(Sparse/BM25)** | BM25 等传统检索 | 字面匹配好,但语义弱 |
| **混合检索(Hybrid)** | 向量 + 关键词融合 | 兼顾语义和字面 |
| **多路检索** | 多个检索器并行 | 召回率高 |
| **迭代检索** | 多轮检索,基于前一轮结果 | 多跳推理 |

### 9.4 BM25 算法详解

**BM25(Best Matching 25)** 是经典关键词检索算法,基于词频和文档长度。

**公式:**
```
score(D, Q) = Σ IDF(qi) · (f(qi, D) · (k1 + 1))
                              / (f(qi, D) + k1 · (1 - b + b · |D| / avgdl))

其中:
- D: 文档
- Q: 查询
- qi: 查询中的第 i 个词
- f(qi, D): qi 在 D 中的词频
- |D|: 文档长度
- avgdl: 平均文档长度
- k1: 词频饱和参数(典型 1.2-2.0)
- b: 长度归一化参数(典型 0.75)
- IDF(qi): qi 的逆文档频率
```

**特点:**
- 字面匹配强
- 不理解语义
- 适合专有名词、代码、编号
- 速度快(倒排索引)

```python
# BM25 实现
from rank_bm25 import BM25Okapi

corpus = [
    "Hello there good man!",
    "It is quite windy in London",
    "How is the weather today?"
]
tokenized_corpus = [doc.split() for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus)

query = "windy London".split()
scores = bm25.get_scores(query)
# scores: [0., 0.867, 0.]
```

### 9.5 Dense Retrieval(稠密检索)

基于 Embedding 向量的语义检索:

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('BAAI/bge-large-zh-v1.5')

# 文档库
docs = ["猫坐在垫子上", "狗跑在草地上", "Python 是编程语言"]
doc_vectors = model.encode(docs)

# 查询
query = "小猫趴在哪?"
query_vector = model.encode([query])

# 余弦相似度
scores = np.dot(query_vector, doc_vectors.T)
# scores: [[0.85, 0.32, 0.15]] → 第 0 个文档最相关
```

---

## 十、Hybrid Search(混合检索)

### 10.1 基础定义

**定义:** 结合向量检索(语义)和关键词检索(字面)的检索方式,取两者之长。

### 10.2 为什么需要混合检索

| 场景 | 向量检索 | 关键词检索 | 混合检索 |
|------|----------|-----------|----------|
| 语义相似但用词不同 | ✅ 好 | ❌ 差 | ✅ 好 |
| 专有名词、产品名 | ❌ 差 | ✅ 好 | ✅ 好 |
| 代码、编号 | ❌ 差 | ✅ 好 | ✅ 好 |
| 错别字、变体 | ✅ 好 | ❌ 差 | ✅ 好 |
| 长尾查询 | ❌ 差 | ✅ 好 | ✅ 好 |
| 复杂语义 | ✅ 好 | ❌ 差 | ✅ 好 |

### 10.3 混合检索的实现

```
查询
    ↓
┌─────────┐    ┌─────────┐
│ 向量检索 │    │关键词检索│
│ (Dense)  │    │ (BM25)  │
└────┬────┘    └────┬────┘
     │               │
     └───────┬───────┘
             ▼
        结果融合(RRF / 加权)
             ↓
        重排(Reranker)
             ↓
         最终结果
```

### 10.4 结果融合方法

| 方法 | 说明 | 公式 |
|------|------|------|
| **RRF(Reciprocal Rank Fusion)** | 基于排名的倒数融合,效果好,无需调参 | score = Σ 1/(k+rank),k=60 |
| **加权平均** | 给两个相似度分数加权平均 | score = α·s_vec + (1-α)·s_bm25 |
| **convex combination** | 凸组合,保证和为 1 | score = α·s_vec + (1-α)·s_bm25,α∈[0,1] |
| **concat** | 简单拼接两个结果列表 | 无融合,靠重排 |
| ** Learned Fusion** | 学习权重 | 训练一个小模型 |

**RRF 公式(最常用):**
```
score(d) = Σ 1 / (k + rank_i(d))

其中:
- d: 文档
- rank_i(d): 文档 d 在第 i 路检索中的排名
- k: 平滑参数,通常取 60
```

### 10.5 混合检索代码示例

```python
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import Chroma
from langchain.retrievers import EnsembleRetriever

# 1. 关键词检索
bm25_retriever = BM25Retriever.from_documents(chunks)
bm25_retriever.k = 5

# 2. 向量检索
vector_retriever = Chroma.from_documents(chunks, embeddings).as_retriever(search_kwargs={"k": 5})

# 3. 混合检索
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.4, 0.6]  # BM25 40%,向量 60%
)

results = ensemble_retriever.invoke("查询")
```

---

## 十一、Reranker(重排器)

### 11.1 基础定义

**定义:** 对初检结果做二次排序,用更精细的模型重新计算 query-doc 相关性,提升精度。

### 11.2 为什么需要重排

| 阶段 | 模型 | 速度 | 精度 |
|------|------|------|------|
| **初检** | Embedding + ANN | 快(毫秒级) | 中(粗排) |
| **重排** | Cross-Encoder | 慢(几十毫秒) | 高(精排) |

初检用 Embedding 是因为快(向量预计算+ANN),但精度有限(独立编码 query 和 doc)。
重排用 Cross-Encoder,把 query 和 doc 一起输入模型,精度更高,但慢。

### 11.3 Cross-Encoder vs Bi-Encoder

```
[Bi-Encoder] (用于初检)
    Query  → Encoder → Query Vector ┐
                                    ├── Cosine Similarity
    Doc    → Encoder → Doc Vector ──┘
    
    优点:可预计算,检索快
    缺点:精度有限

[Cross-Encoder] (用于重排)
    [Query, Doc] → Encoder → Score
    
    优点:精度高(query 和 doc 联合编码)
    缺点:无法预计算,慢
```

### 11.4 主流 Reranker 模型

| 模型 | 来源 | 特点 | 开源 |
|------|------|------|------|
| **bge-reranker-v2-m3** | 智源 | 多语言,中文优秀 | ✅ |
| **bge-reranker-large** | 智源 | 中文优秀 | ✅ |
| **Cohere Rerank 3** | Cohere | 商用 API,性能强 | ❌ |
| **Jina Reranker v2** | Jina | 多语言 | ✅ |
| **Voyage Rerank-2** | Voyage AI | 商用顶级 | ❌ |
| **ColBERT v2** | 开源 | 延迟交互,精度高 | ✅ |
| **RankGPT** | 开源 | 用 LLM 做 rerank | ✅ |

### 11.5 重排代码示例

```python
# 1. BGE Reranker(本地)
from FlagEmbedding import FlagReranker
reranker = FlagReranker('BAAI/bge-reranker-v2-m3', use_fp16=True)

pairs = [['查询', '文档1'], ['查询', '文档2'], ['查询', '文档3']]
scores = reranker.compute_score(pairs)
# scores: [0.95, 0.32, -0.15]

# 2. Cohere Rerank(商用 API)
from langchain_cohere import CohereRerank
reranker = CohereRerank(model="rerank-multilingual-v3.0", top_n=5)
reranked_docs = reranker.compress_documents(docs, query)

# 3. LangChain RAG 重排链
from langchain.retrievers import ContextualCompressionRetriever
compression_retriever = ContextualCompressionRetriever(
    base_compressor=reranker,
    base_retriever=ensemble_retriever
)
results = compression_retriever.invoke("查询")
```

### 11.6 重排效果

Anthropic 在 Contextual Retrieval 文档中报告:
- 朴素 RAG:基准
- + Contextual Retrieval:失败率 ↓ 49%
- + BM25 混合检索:失败率 ↓ 56%
- + Reranker:失败率 ↓ 67%
- + Contextual + BM25 + Reranker:失败率 ↓ 67%

---

## 十二、Query Rewriting(查询改写)

### 12.1 基础定义

**定义:** 用 LLM 改写用户查询,以提升检索效果。

### 12.2 为什么需要查询改写

| 问题 | 示例 | 改写后 |
|------|------|--------|
| **查询太短** | "RAG" | "什么是检索增强生成 RAG" |
| **查询有歧义** | "苹果" | "苹果公司股价" |
| **查询口语化** | "怎么用这个" | "如何使用 RAG 模块" |
| **查询错别字** | "MCP协议" | "MCP 协议 Model Context Protocol" |
| **查询太复杂** | "对比 A 和 B 的优缺点" | 拆为多个子查询 |

### 12.3 查询改写策略

#### 12.3.1 查询扩展(Query Expansion)

```python
def expand_query(query):
    prompt = f"""请把以下查询扩展为 3 个相关但不同的查询,用于检索:
    
    原查询: {query}
    
    扩展查询:"""
    expanded = llm.invoke(prompt)
    return [query] + expanded.split("\n")
```

#### 12.3.2 查询分解(Query Decomposition)

```python
def decompose_query(query):
    prompt = f"""把以下复杂查询分解为多个简单子查询:
    
    复杂查询: {query}
    
    子查询:"""
    subqueries = llm.invoke(prompt)
    return subqueries
```

#### 12.3.3 HyDE(Hypothetical Document Embeddings)

**论文:** Gao et al., "Precise Zero-Shot Dense Retrieval without Relevance Labels", 2022-12
**论文链接:** https://arxiv.org/abs/2212.10496

**核心思想:** 先让 LLM 写一个假设性答案,然后用这个答案去检索(因为答案和文档更相似)。

```python
def hyde_retrieval(query):
    # 1. 让 LLM 写假设答案
    hyde_prompt = f"""请回答以下问题(即使是猜测也写一段答案):
    
    问题: {query}
    
    假设答案:"""
    hypothetical_answer = llm.invoke(hyde_prompt)
    
    # 2. 用假设答案去检索(而不是用 query)
    docs = vector_store.similarity_search(hypothetical_answer, k=5)
    
    # 3. 用 query + 检索到的文档生成最终答案
    final_answer = llm.invoke(f"基于以下文档回答:{docs}\n问题:{query}")
    return final_answer
```

#### 12.3.4 Step-Back Prompting

**论文:** Zheng et al., "Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models", 2023-10
**论文链接:** https://arxiv.org/abs/2310.06117

**核心思想:** 让 LLM 先问一个更抽象的"后退问题",再回答具体问题。

```python
def step_back_retrieval(query):
    # 1. 生成后退问题(更抽象)
    stepback_prompt = f"""把以下具体问题转为一个更抽象、更通用的问题:
    
    具体问题: {query}
    
    抽象问题:"""
    stepback_question = llm.invoke(stepback_prompt)
    
    # 2. 同时检索具体和抽象问题
    docs_concrete = retriever.search(query, k=3)
    docs_abstract = retriever.search(stepback_question, k=3)
    
    # 3. 综合生成
    all_docs = docs_concrete + docs_abstract
    return llm.invoke(f"基于:{all_docs}\n回答:{query}")
```

#### 12.3.5 Multi-Query

```python
def multi_query_retrieval(query):
    """生成多个变体查询,并行检索,合并去重"""
    prompt = f"""生成 3 个不同角度的查询变体:
    
    原查询: {query}
    
    变体:"""
    variants = llm.invoke(prompt).split("\n")
    
    all_docs = []
    for v in variants:
        docs = retriever.search(v, k=3)
        all_docs.extend(docs)
    
    # 去重
    unique_docs = deduplicate(all_docs)
    return unique_docs
```

### 12.4 查询改写策略对比

| 策略 | 适用场景 | 成本 | 效果 |
|------|---------|------|------|
| **查询扩展** | 短查询 | 低 | 中 |
| **查询分解** | 复杂查询 | 中 | 高 |
| **HyDE** | 概念性问题 | 中 | 高 |
| **Step-Back** | 抽象问题 | 中 | 高 |
| **Multi-Query** | 通用 | 中 | 中高 |

---

## 十三、Recall & Precision(召回率与精确率)

### 13.1 定义

| 指标 | 公式 | 含义 |
|------|------|------|
| **召回率(Recall)** | 相关结果被检索到的 / 所有相关结果 | 有没有漏掉 |
| **精确率(Precision)** | 检索到的相关结果 / 所有检索结果 | 准不准确 |
| **F1** | 2·P·R / (P+R) | 调和平均 |
| **Hit Rate@K** | Top-K 中至少有一个相关的比例 | 是否命中 |
| **MRR** | 1/第一个相关结果的排名 | 排名质量 |
| **NDCG@K** | 考虑排名位置的相关性 | 排序质量 |

### 13.2 召回率 vs 精确率权衡

```
召回率 ↑ ←───────→ 精确率 ↓
   (多返回一些,保证不漏)  (少返回一些,保证准确)
```

**RAG 中的选择:**
- RAG 更看重召回率(漏掉比多几个噪声更严重)
- 可以通过重排来提升精确率
- 典型策略:检索多一些(如 Top-20),重排后取前几个(如 Top-5)

### 13.3 评估指标详解

#### 13.3.1 MRR(Mean Reciprocal Rank)

```
MRR = (1/|Q|) · Σ 1/rank_i

示例:
Q1: 第一个相关结果在 rank 1 → 1/1 = 1.0
Q2: 第一个相关结果在 rank 3 → 1/3 = 0.33
Q3: 第一个相关结果在 rank 2 → 1/2 = 0.5

MRR = (1.0 + 0.33 + 0.5) / 3 = 0.61
```

#### 13.3.2 NDCG(Normalized Discounted Cumulative Gain)

```
DCG = Σ rel_i / log2(i+1)
NDCG = DCG / IDCG  (理想 DCG)

考虑因素:
- 相关性等级(0/1/2/3)
- 排名位置(越靠前越好)
- 归一化(便于跨查询比较)
```

#### 13.3.3 Hit Rate@K

```
Hit@K = (有相关结果在 Top-K 的查询数) / 总查询数

例如:Hit@5 = 0.8 表示 80% 的查询在 Top-5 中至少有一个相关结果
```

### 13.4 RAG 评估框架 RAGAS

**RAGAS(RAG Assessment)** 是流行的 RAG 评估框架:
- GitHub: https://github.com/explodinggradients/ragas

**核心指标:**

| 指标 | 说明 |
|------|------|
| **Faithfulness(忠实度)** | 答案是否基于检索到的文档(防幻觉) |
| **Answer Relevancy(答案相关性)** | 答案是否回应了问题 |
| **Context Precision(上下文精确率)** | 检索到的文档是否相关 |
| **Context Recall(上下文召回率)** | 相关文档是否都被检索到 |

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness, answer_relevancy, context_precision, context_recall
)
from datasets import Dataset

# 准备评估数据
eval_data = Dataset.from_dict({
    "question": ["什么是 RAG?"],
    "answer": ["RAG 是检索增强生成..."],
    "contexts": [["文档1", "文档2"]],
    "ground_truth": ["RAG 是 Retrieval-Augmented Generation..."]
})

# 评估
result = evaluate(
    eval_data,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
)
print(result)
# {'faithfulness': 0.95, 'answer_relevancy': 0.88, 'context_precision': 0.92, 'context_recall': 0.85}
```

---

## 十四、Knowledge Base(知识库)

### 14.1 基础定义

**定义:** 结构化或非结构化的知识集合,供 RAG 系统检索使用。

### 14.2 知识库的类型

| 类型 | 说明 | 示例 | 检索方式 |
|------|------|------|---------|
| **文档库** | PDF、Word、Markdown 等文档 | 产品手册、帮助中心 | 向量检索 |
| **数据库** | 结构化数据 | 业务数据库 | SQL |
| **知识图谱** | 实体-关系图谱 | 企业知识图谱 | 图遍历 |
| **FAQ** | 问答对 | 客服知识库 | 语义匹配 |
| **网页** | 爬取的网页 | 文档站 | 向量+关键词 |
| **代码库** | 源代码 | 开发文档 | 代码感知 |
| **多模态** | 图片、视频 | 图文知识 | 多模态嵌入 |
| **API** | 实时数据接口 | 业务系统 API | API 调用 |

### 14.3 知识库质量

RAG 效果的上限取决于知识库的质量:

| 维度 | 说明 | 影响 |
|------|------|------|
| **准确性** | 知识本身是否正确 | 错误知识 → 错误答案 |
| **完整性** | 是否覆盖所需知识点 | 缺失 → 无法回答 |
| **时效性** | 是否及时更新 | 过时 → 答案错误 |
| **结构化程度** | 是否便于检索 | 混乱 → 召回低 |
| **去重** | 是否有冗余 | 重复 → 浪费 Token |
| **质量一致** | 各文档质量是否一致 | 参差 → 检索不稳定 |

### 14.4 知识库构建流程

```
[1] 数据收集
    ├── 内部文档(PDF/Word/Confluence)
    ├── 网页爬取
    ├── API 接入
    └── 数据库导出
    ↓
[2] 数据清洗
    ├── 去噪(去除 HTML 标签、水印)
    ├── 去重
    ├── 格式统一
    └── 质量过滤
    ↓
[3] 文档解析
    ├── PDF 解析(版面分析)
    ├── OCR(图片中的文字)
    ├── 表格识别
    └── 公式识别
    ↓
[4] 分块
    ├── 选择分块策略
    ├── 设置 chunk_size 和 overlap
    └── 元数据标注
    ↓
[5] 向量化
    ├── 选择 Embedding 模型
    ├── 批量向量化
    └── 质量校验
    ↓
[6] 索引构建
    ├── 选择向量数据库
    ├── 构建 ANN 索引
    └── 元数据索引
    ↓
[7] 评估
    ├── 检索质量(召回率/精确率)
    ├── 端到端(RAGAS)
    └── 人工抽检
    ↓
[8] 上线
    ├── 增量更新机制
    ├── 监控告警
    └── 持续优化
```

---

## 十五、Document Loader(文档加载器)

### 15.1 常见的 Loader

| Loader | 支持格式 | 来源 |
|--------|----------|------|
| **PyPDFLoader** | PDF | LangChain |
| **PDFPlumberLoader** | PDF(含表格) | LangChain |
| **UnstructuredPDFLoader** | PDF(含图片) | Unstructured |
| **Unstructured** | PDF/Word/PPT/HTML/... | Unstructured.io |
| **DirectoryLoader** | 目录(多种格式) | LangChain |
| **NotionLoader** | Notion 页面 | LangChain |
| **ConfluenceLoader** | Confluence 文档 | LangChain |
| **WebBaseLoader** | 网页 | LangChain |
| **SitemapLoader** | 站点地图 | LangChain |
| **GitLoader** | Git 仓库 | LlamaIndex |
| **NotebookLoader** | Jupyter Notebook | LangChain |
| **CSVLoader** | CSV | LangChain |
| **JSONLoader** | JSON | LangChain |
| **SQLDatabaseLoader** | SQL 数据库 | LangChain |

### 15.2 PDF 解析的挑战

PDF 是 RAG 中最难的格式之一:

| 挑战 | 说明 | 解决方案 |
|------|------|---------|
| **多栏排版** | 文字阅读顺序错乱 | 版面分析(LayoutLM) |
| **表格识别** | 表格无法提取为结构 | Camelot/Tabula |
| **图片中的文字** | 需要 OCR | Tesseract/PaddleOCR |
| **数学公式** | 公式无法解析 | Nougat/Mathpix |
| **图表** | 图表无法理解 | 多模态 LLM |
| **扫描件** | 图片型 PDF | OCR |
| **页眉页脚** | 干扰内容 | 清洗过滤 |

### 15.3 文档处理流程

```
原始文件(PDF/Word/...)
    ↓
加载器读取文本
    ↓
清洗(去噪、去重、格式化)
    ↓
分块(Splitter)
    ↓
向量化(Embedding)
    ↓
存入向量数据库
```

### 15.4 LlamaIndex 文档加载示例

```python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# 1. 加载目录下所有文档
documents = SimpleDirectoryReader("./data").load_data()

# 2. 自动构建索引(分块+向量化+存储)
index = VectorStoreIndex.from_documents(documents)

# 3. 查询
query_engine = index.as_query_engine(similarity_top_k=5)
response = query_engine.query("什么是 RAG?")
print(response)
```

---

## 十六、RAG 完整代码示例(生产级)

```python
"""
生产级 RAG 系统:Hybrid Search + Reranker + Query Rewriting
"""
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever, ContextualCompressionRetriever
from langchain_cohere import CohereRerank
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
import os

# 1. 加载文档
loader = DirectoryLoader("./docs", glob="**/*.pdf", loader_cls=PyPDFLoader)
docs = loader.load()

# 2. 分块(递归 + 上下文元数据)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50,
    separators=["\n\n", "\n", "。", ".", " ", ""]
)
chunks = splitter.split_documents(docs)

# 3. 向量化(中文 BGE)
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-large-zh-v1.5",
    encode_kwargs={"normalize_embeddings": True}
)

# 4. 存入向量数据库
vectorstore = Chroma.from_documents(
    chunks, embeddings, persist_directory="./chroma_db"
)

# 5. 构建混合检索器
bm25_retriever = BM25Retriever.from_documents(chunks)
bm25_retriever.k = 20

vector_retriever = vectorstore.as_retriever(search_kwargs={"k": 20})

ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.3, 0.7]
)

# 6. 重排器
reranker = CohereRerank(model="rerank-multilingual-v3.0", top_n=5)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=reranker,
    base_retriever=ensemble_retriever
)

# 7. 查询改写
def rewrite_query(query):
    rewrite_prompt = ChatPromptTemplate.from_template("""
    把以下查询改写为更适合检索的形式(关键词更明确,语义更完整):
    
    原查询: {query}
    
    改写后(直接输出,不要解释):""")
    chain = rewrite_prompt | ChatOpenAI(temperature=0) | StrOutputParser()
    return chain.invoke({"query": query})

# 8. RAG Chain
template = """你是一个专业的问答助手。基于以下检索到的上下文回答问题。
如果上下文中没有相关信息,回答"根据已知信息无法回答该问题"。
回答时请引用来源(如[1]、[2])。

上下文:
{context}

问题: {question}

回答:"""

prompt = ChatPromptTemplate.from_template(template)
llm = ChatOpenAI(model="gpt-4o", temperature=0)

def format_docs(docs):
    return "\n\n".join([f"[{i+1}] {doc.page_content}" for i, doc in enumerate(docs)])

rag_chain = RunnableParallel(
    {"context": compression_retriever | format_docs,
     "question": RunnablePassthrough()}
) | prompt | llm | StrOutputParser()

# 9. 完整 RAG 流程
def rag_query(question):
    # 9.1 查询改写
    rewritten = rewrite_query(question)
    print(f"改写后查询: {rewritten}")
    
    # 9.2 RAG 生成
    answer = rag_chain.invoke(rewritten)
    return answer

# 10. 测试
answer = rag_query("什么是 RAG?它和微调有什么区别?")
print(answer)
```

---

## 十七、Long Context vs RAG

### 17.1 长上下文模型的崛起

随着 Claude 3.5(200K)、Gemini 1.5 Pro(2M)、GPT-4o(128K)等模型上下文窗口增大,有人开始质疑 RAG 是否还需要。

### 17.2 长上下文 vs RAG 对比

| 维度 | Long Context | RAG |
|------|--------------|-----|
| **原理** | 把所有文档塞进上下文 | 检索相关文档 |
| **上限** | 模型上下文窗口 | 知识库大小 |
| **延迟** | 高(长输入推理慢) | 低(短输入) |
| **成本** | 高(按 Token 计费) | 低(只检索相关) |
| **精度** | 中("Lost in the Middle") | 高(精选相关) |
| **更新** | 重新塞入 | 知识库更新即可 |
| **规模** | 有限(几百万 Token) | 无限(TB 级) |
| **实现** | 简单 | 复杂 |

### 17.3 Long Context RAG(混合方案)

Anthropic 提出 Long Context RAG:用长上下文模型 + RAG,把检索到的更多文档塞入长上下文。

```
传统 RAG:Top-5 文档
    ↓
Long Context RAG:Top-50 文档(塞入 200K 上下文)
    ↓
优势:更多上下文,减少漏检
```

### 17.4 选型建议

| 场景 | 推荐 |
|------|------|
| **文档数 < 50 个** | Long Context |
| **文档数 > 1000 个** | RAG |
| **需要精确溯源** | RAG |
| **快速原型** | Long Context |
| **生产级、大规模** | RAG(可加 Long Context) |
| **成本敏感** | RAG |

---

## 十八、易混淆概念对比

### 18.1 RAG vs 微调

| 维度 | RAG | 微调(Fine-tuning) |
|------|-----|-------------------|
| **原理** | 检索 + 生成 | 更新模型参数 |
| **时效性** | 高(可实时更新) | 低(需要重新训练) |
| **成本** | 低(检索成本) | 高(训练成本) |
| **可解释性** | 高(可追溯来源) | 低(黑盒) |
| **适合** | 事实性问答、知识库 | 风格、语气、特定能力 |
| **数据量** | 任意 | 需要训练数据 |
| **更新难度** | 易(更新知识库) | 难(重新训练) |
| **"遗忘"** | 易(删除文档) | 难(无法精确遗忘) |
| **延迟** | 中(检索+生成) | 低(只生成) |

### 18.2 RAG vs GraphRAG vs RAPTOR

| 维度 | RAG | GraphRAG | RAPTOR |
|------|-----|----------|--------|
| **结构** | 扁平向量 | 知识图谱 | 树状分层 |
| **强项** | 简单高效 | 多跳关系 | 全局摘要 + 分层 |
| **适合** | 通用 | 实体关系密集 | 长文档总结 |
| **构建复杂度** | 低 | 高 | 中 |
| **检索粒度** | 单一 | 多种 | 多层级 |
| **更新难度** | 易 | 难 | 中 |

### 18.3 Dense vs Sparse Retrieval

| 维度 | Dense Retrieval | Sparse Retrieval |
|------|----------------|------------------|
| **代表** | Embedding + ANN | BM25 / TF-IDF |
| **原理** | 语义向量相似度 | 关键词匹配 |
| **理解语义** | ✅ 是 | ❌ 否 |
| **字面匹配** | ❌ 弱 | ✅ 强 |
| **专有名词** | ❌ 弱 | ✅ 强 |
| **跨语言** | ✅ 是 | ❌ 否 |
| **速度** | 中 | 快 |
| **依赖训练** | 是(Embedding 模型) | 否 |

### 18.4 Bi-Encoder vs Cross-Encoder

| 维度 | Bi-Encoder | Cross-Encoder |
|------|-----------|----------------|
| **用途** | 初检(检索) | 重排 |
| **速度** | 快(可预计算) | 慢(每对独立计算) |
| **精度** | 中 | 高 |
| **能否预计算** | ✅ 可以 | ❌ 不能 |
| **典型应用** | ANN 检索 | Reranker |

### 18.5 向量数据库 vs 传统数据库

| 维度 | 向量数据库 | 传统数据库 |
|------|-----------|-----------|
| **数据** | 高维向量 | 结构化数据 |
| **查询** | 相似度搜索 | 精确匹配/范围查询 |
| **索引** | ANN 索引 | B树/哈希/倒排 |
| **结果** | 近似最近邻 | 精确结果 |
| **场景** | 语义搜索、RAG | 事务、精确查询 |

---

## 十九、RAG 系统设计模式

### 19.1 模式一:朴素 RAG(原型)

```
[文档] → [分块] → [Embedding] → [向量库]
                                        ↓
[查询] → [Embedding] → [ANN 检索] → [Top-K] → [LLM 生成]
```

适用:原型、小规模、简单问答。

### 19.2 模式二:Advanced RAG(生产)

```
[查询] → [查询改写] → [Hybrid 检索] → [重排] → [Top-K] → [LLM 生成]
                                                              ↓
                                                        [引用标注]
```

适用:生产环境、中等规模、高质量问答。

### 19.3 模式三:Agentic RAG(智能)

```
[查询] → [Agent]
            ↓
         [决策:是否检索?]
            ├── 否 → 直接回答
            └── 是 → [检索]
                      ↓
                   [评估:结果够吗?]
                      ├── 够 → [生成]
                      └── 不够 → [再检索](迭代)
                                  ↓
                              [最终生成]
```

适用:复杂任务、多跳推理、自主决策。

### 19.4 模式四:Multi-Modal RAG(多模态)

```
[图片+文本] → [多模态 Embedding] → [向量库]
                                        ↓
[查询] → [Embedding] → [检索] → [图片+文本] → [多模态 LLM 生成]
```

适用:图文混合知识库。

### 19.5 模式五:GraphRAG(关系密集)

```
[文档] → [实体抽取] → [图谱构建] → [社区发现] → [摘要]
                                                    ↓
[查询] → [实体识别] → [子图抽取] → [社区匹配] → [LLM 生成]
```

适用:多跳推理、关系查询。

---

## 二十、RAG 调优清单

### 20.1 检索质量优化

| 优化项 | 方法 | 效果 |
|--------|------|------|
| **分块策略** | 递归/语义/代码感知 | 中 |
| **分块大小** | 512 通用,256 精确 | 中 |
| **Embedding 模型** | BGE-m3 / text-embedding-3 | 高 |
| **混合检索** | 向量 + BM25 | 高 |
| **重排** | Cross-Encoder | 高 |
| **查询改写** | HyDE / Multi-Query | 中 |
| **元数据过滤** | 时间/类别/来源 | 中 |
| **Contextual Retrieval** | Anthropic 方法 | 高 |

### 20.2 生成质量优化

| 优化项 | 方法 | 效果 |
|--------|------|------|
| **Prompt** | 明确指令+引用要求 | 高 |
| **系统提示** | "只基于文档回答" | 高 |
| **Few-shot** | 给定示例 | 中 |
| **CoT** | 让 LLM 推理 | 中 |
| **引用标注** | 强制引用来源 | 中 |
| **答案校验** | 二次校验答案 | 中 |

### 20.3 系统性能优化

| 优化项 | 方法 | 效果 |
|--------|------|------|
| **缓存** | 缓存热门查询 | 高 |
| **异步** | 异步检索+生成 | 中 |
| **批处理** | 批量 Embedding | 中 |
| **索引优化** | HNSW 参数调优 | 中 |
| **水平扩展** | 向量库分片 | 高 |
| **CDN** | 静态资源 CDN | 中 |

---

## 二十一、真实场景应用

### 21.1 企业知识库问答

```
[需求] 企业内部文档(PDF/Word/Confluence)+ 员工问答
[方案]
    ├── Unstructured 解析多格式文档
    ├── RecursiveCharacterTextSplitter 分块(512)
    ├── BGE-large-zh-v1.5 向量化
    ├── Milvus 存储(百万级文档)
    ├── Hybrid Search(向量+BM25)
    ├── BGE Reranker 重排
    └── Claude/GPT 生成 + 引用标注
[效果] 准确率 85%+,响应 < 2s
```

### 21.2 客服系统

```
[需求] FAQ + 历史工单 → 自动客服
[方案]
    ├── FAQ 结构化(问答对)
    ├── 历史工单向量化
    ├── 意图分类(Routing)
    ├── 检索 FAQ + 相似工单
    ├── LLM 生成回答 + 推荐人工
    └── 失败转人工
[效果] 60% 问题自动解决
```

### 21.3 代码库问答

```
[需求] 开发者查询代码库
[方案]
    ├── 按 class/function 分块(代码感知)
    ├── 保留 import 和签名
    ├── Code Embedding
    ├── 检索 + 重排
    └── LLM 解释 + 代码引用
[工具] Sourcegraph Cody / Continue.dev
```

### 21.4 法律文书检索

```
[需求] 法律条文+案例检索
[方案]
    ├── GraphRAG(条文引用关系图)
    ├── 实体抽取(法条/案例/概念)
    ├── 多跳推理(条文 A 引用条文 B)
    └── 引用强化
[效果] 支持复杂法律问题
```

### 21.5 学术论文助手

```
[需求] 学术论文问答 + 综述生成
[方案]
    ├── RAPTOR(论文分层摘要)
    ├── 多论文检索
    ├── 跨论文综合
    └── 引用生成
[效果] 支持跨论文综述
```

---

## 二十二、Anthropic / OpenAI 官方建议

### 22.1 Anthropic 官方建议

> 来源:Anthropic Contextual Retrieval(2024-09)
> https://www.anthropic.com/news/contextual-retrieval

1. **使用 Contextual Retrieval:** 给每个 Chunk 加上下文前缀
2. **混合检索:** 向量 + BM25
3. **重排:** 用 Cross-Encoder 重排
4. **长上下文:** 利用 Claude 200K 上下文,塞入更多文档
5. **Prompt Caching:** 缓存文档前缀,降低成本
6. **引用标注:** 强制 LLM 引用来源

### 22.2 OpenAI 官方建议

> 来源:OpenAI Cookbook - Building RAG with OpenAI
> https://cookbook.openai.com/

1. **text-embedding-3-large:** 用最新 Embedding 模型
2. **Hybrid Search:** 向量 + BM25
3. **Reranker:** 用 GPT-4 做 rerank
4. **结构化输出:** 用 JSON Schema 强制结构化
5. **Function Calling:** 用函数调用接入检索
6. **Assistants API:** 用内置 file_search 工具

### 22.3 RAG 设计清单

- [ ] 选择合适的 Embedding 模型(中文用 BGE,英文用 text-embedding-3)
- [ ] 选择合适的分块策略(通用递归,代码感知,语义分块)
- [ ] 设置合适的 chunk_size(512)和 overlap(50)
- [ ] 使用混合检索(向量 + BM25)
- [ ] 使用重排器(Cross-Encoder)
- [ ] 使用查询改写(HyDE / Multi-Query)
- [ ] 加入元数据过滤
- [ ] 设计 Prompt(只基于文档 + 引用标注)
- [ ] 实现"我不知道"兜底
- [ ] 评估(RAGAS / 人工抽检)
- [ ] 监控(检索质量、生成质量、延迟)
- [ ] 增量更新机制

---

## 二十三、参考资源

### 官方项目
- **GraphRAG(微软):** https://github.com/microsoft/graphrag
- **RAPTOR:** https://github.com/parthsarthi03/raptor
- **HippoRAG:** https://github.com/OSU-NLP-Group/HippoRAG
- **FAISS(Meta):** https://github.com/facebookresearch/faiss
- **LlamaIndex:** https://www.llamaindex.ai/
- **LangChain:** https://www.langchain.com/
- **RAGAS:** https://github.com/explodinggradients/ragas
- **FlagEmbedding(BGE):** https://github.com/FlagOpen/FlagEmbedding

### 向量数据库
- **Pinecone:** https://www.pinecone.io/
- **Milvus:** https://milvus.io/
- **Chroma:** https://www.trychroma.com/
- **Qdrant:** https://qdrant.tech/
- **Weaviate:** https://weaviate.io/
- **pgvector:** https://github.com/pgvector/pgvector
- **LanceDB:** https://lancedb.github.io/lancedb/

### Embedding 模型
- **BGE 系列:** https://huggingface.co/BAAI
- **MTEB 榜单:** https://huggingface.co/spaces/mteb/leaderboard
- **OpenAI Embedding:** https://platform.openai.com/docs/guides/embeddings
- **Cohere Embed:** https://cohere.com/embeddings
- **Voyage AI:** https://www.voyageai.com/

### 论文
- **RAG 原始论文(Lewis et al., 2020):** https://arxiv.org/abs/2005.11401
- **GraphRAG(Edge et al., 2024):** https://arxiv.org/abs/2404.16130
- **RAPTOR(Sarthi et al., 2024):** https://arxiv.org/abs/2401.18059
- **HippoRAG(Gutiérrez et al., 2024):** https://arxiv.org/abs/2405.14831
- **Self-RAG(Asai et al., 2023):** https://arxiv.org/abs/2310.11511
- **CRAG(Yan et al., 2024):** https://arxiv.org/abs/2401.15884
- **Adaptive RAG(Jeong et al., 2024):** https://arxiv.org/abs/2402.10222
- **HyDE(Gao et al., 2022):** https://arxiv.org/abs/2212.10496
- **Step-Back(Zheng et al., 2023):** https://arxiv.org/abs/2310.06117
- **Dense Passage Retrieval:** https://arxiv.org/abs/2004.04906
- **Lost in the Middle:** https://arxiv.org/abs/2307.03172
- **ColBERT:** https://arxiv.org/abs/2004.12832
- **Many-Shot ICL:** https://arxiv.org/abs/2404.11018

### 教程与书籍
- **LlamaIndex 官方文档:** https://docs.llamaindex.ai/
- **LangChain RAG 教程:** https://python.langchain.com/docs/tutorials/rag/
- **Anthropic Contextual Retrieval:** https://www.anthropic.com/news/contextual-retrieval
- **OpenAI RAG Cookbook:** https://cookbook.openai.com/
- **Pinecone Learn:** https://www.pinecone.io/learn/

### 评估与基准
- **RAGAS:** https://github.com/explodinggradients/ragas
- **TruLens:** https://www.trulens.org/
- **MTEB:** https://huggingface.co/spaces/mteb/leaderboard
- **BEIR:** https://github.com/beir-cellar/beir
