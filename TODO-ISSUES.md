# 待解决问题与迭代清单(TODO & Issues)

> 本文档记录知识体系中**尚未覆盖、覆盖不足、或存在疑问**的内容,作为下次迭代的输入。
> 每条标注来源、状态和优先级,迭代完成后移到对应章节的版本日志。

---

## 一、本次迭代(v4.7)新增内容

> 以下内容已在 v4.7 中补充完成,列出供确认。

| 序号 | 主题 | 补充位置 | 状态 | 说明 |
|------|------|---------|------|------|
| 1 | GPU 分区(MIG/MPS/Time-Slicing) | 10-§9.6 | ✅ 已完成 | 三方案对比 + 选型决策树 + MIG 实例规格表 |
| 2 | TTFT/TPS/ITL 量化基准 | 10-§16.3.1 | ✅ 已完成 | 8 种模型/GPU 组合 + 延迟公式 + 用户体验阈值 |
| 3 | TPS 量化基准 | 10-§16.3.2 | ✅ 已完成 | 6 种配置 + QPS 换算 + TPS 公式 |
| 4 | 错误率指标 | 10-§16.3.3 | ✅ 已完成 | 7 种错误类型 + SLO 目标 + PromQL 告警 |
| 5 | SLI/SLO/SLA 框架 | 10-§16.3.4 | ✅ 已完成 | 8 项 SLO 模板 + Error Budget 计算 |
| 6 | 缓存命中率量化 | 10-§17.5 | ✅ 已完成 | 5 层命中率基准 + 计算公式 + 监控 + 优化策略 |
| 7 | 兜底/容错/推理失败恢复 | 05-§16.6 | ✅ 已完成 | 5 级兜底 + checkpoint 回滚 + 补偿事务 |
| 8 | Embedding 语义路由 + 向量合并 | 10-§21.3 | ✅ 已完成 | 4 种路由方式对比 + 代码 + 效果量化 |
| 9 | 流式 vs 非流式网络开销 | 10-§21.4 | ✅ 已完成 | 传输量对比 + 选型建议 + Nginx 配置 |
| 10 | 指标采集命令行验证 | 10-§16.3.5 | ✅ 已完成 | curl /metrics + vLLM benchmark_serving |

---

## 二、已覆盖但深度不足(下次可加强)

| 序号 | 主题 | 当前位置 | 当前状态 | 待加强方向 | 优先级 |
|------|------|---------|---------|-----------|--------|
| 1 | **滑动窗口(限流)** | 10-§14.2.2 | 仅 5 行文字描述 | 补充:滑动窗口的 Python/Redis 实现、与令牌桶的场景对比量化 | 中 |
| 2 | **滑动窗口(上下文管理)** | 07-§4.4.1 | 有基础代码 | 补充:滑动窗口 vs 摘要压缩 vs 检索增强的 Token 消耗量化对比 | 中 |
| 3 | **ReAct 模式** | 06-§8 | 有完整示例和 LangGraph 实现 | 补充:ReAct 与 Plan-and-Execute、Reflexion 的量化对比(步数/Token/成功率) | 中 |
| 4 | **注意力机制** | 09-§2.3-2.5 | 有公式和 4 种变体 | 补充:FlashAttention-2/3 的量化加速比;MLA 的 KV Cache 压缩率量化 | 低 |
| 5 | **Durable Execution** | 05-§16 | 有 Temporal + LangGraph 示例 | 补充:Restate/Inngest 对比;Event Sourcing 的存储成本量化 | 低 |

---

## 三、尚未覆盖的点(下次迭代优先)

| 序号 | 主题 | 所属章节(建议) | 来源 | 说明 | 优先级 |
|------|------|---------------|------|------|--------|
| 1 | **Embedding 服务部署** | 10-部署运维 | 截图"还有向量的部分embedding" | 当前 10 章提到 Embedding 但没有独立的 Embedding 服务部署节(vLLM 可跑 Embedding 模型,但 Tei/Sentence-Transformers 等专用方案未覆盖) | 高 |
| 2 | **Ollama 与 vLLM 部署对比量化** | 10-部署运维 | 截图"他和vllm都是部署的但是没见到" | 当前有 Ollama 和 vLLM 各自的章节,但缺少**同模型同硬件**下的量化对比表(QPS/TTFT/显存/并发) | 高 |
| 3 | **Agent 框架 loop/multi-agent communication/harness/prompt 能力** | 03-智能体主体 | 截图"loop和多agent通信的还有harness还有prompt" | 当前 03 章有 17 个框架对比,但缺少**横向能力矩阵**:哪些框架原生支持 Agent Loop?哪些支持多 Agent 通信?哪些有测试 Harness?哪些有 Prompt 管理? | 高 |
| 4 | **节点还原(分布式状态恢复)** | 05-任务流程编排 | 截图"但是要看节点去还原" | §16.6 已补充 checkpoint 回滚,但"分布式多节点状态还原"(如多个 Worker 节点崩溃后的全局状态恢复)未深入 | 中 |
| 5 | **推理模型(o1/o3/DeepSeek-R1)部署特殊考量** | 10-部署运维 | 推理模型 2025-2026 爆发 | 推理模型的 reasoning token 对 KV Cache/计费/流式的影响未量化(如 reasoning token 可能数千,显著增加延迟和成本) | 中 |
| 6 | **Edge/边缘部署** | 10-部署运维 | llama.cpp/MLC-LLM 章节 | 手机/边缘设备上部署 LLM 的量化(内存占用/TTFT/功耗)未覆盖 | 低 |

---

## 四、待确认/存疑的问题

> 以下内容存在不确定性,需要查证后再写入正文。

| 序号 | 问题 | 当前处理 | 需要确认 | 优先级 |
|------|------|---------|---------|--------|
| 1 | **vLLM `--stream-interval` 参数** | §21.4 中提到 `--stream-interval 0.05` | 需确认该参数在 vLLM V1 引擎中是否仍存在,还是已被移除/改名 | 高 |
| 2 | **vLLM Prefix Cache 命中率指标名** | §17.5 使用 `vllm:gpu_prefix_cache_hit_rate` | vLLM V0 和 V1 引擎的指标名可能不同,V1 可能直接暴露 `prefix_cache_hit_rate`,需核实官方 metrics 文档 | 高 |
| 3 | **TTFT/TPOT 量化基准数据来源** | §16.3.1/16.3.2 的基准表 | 这些数值是基于社区博客和经验的估算,非严格 benchmark。需标注"参考值"或补充实际压测数据 | 中 |
| 4 | **MPS `--gpu-memory-utilization` 隔离** | §9.6 提到 MPS 可用 `--gpu-memory-utilization` 限制各实例显存 | 需确认 vLLM 的 `--gpu-memory-utilization` 在 MPS 下是否真正隔离显存(可能只是限制 KV Cache 池大小,模型权重仍共享) | 中 |
| 5 | **Embedding 路由效果量化** | §21.3.4 的路由效果表 | "小模型占比 60%/准确率 92%" 等数据为估算值,需补充真实 A/B 测试数据或论文引用 | 中 |
| 6 | **流式传输量 5x 的计算** | §21.4.2 声称流式传输量约为非流式 5 倍 | 该计算基于 200 token 输出 + 每 chunk 60B 估算;实际 chunk 大小受 SSE 格式、JSON 序列化、token 编码影响,可能有偏差 | 低 |
| 7 | **LangGraph 条件边回滚行为** | §16.6.2 中 `retry` 路由回 `search` 节点 | 需确认 LangGraph 在条件边回退时是否真正"回滚"到上一个 checkpoint,还是重新从 START 执行(取决于 checkpointer 实现) | 高 |

---

## 五、截图中的其他提及点(已覆盖确认)

> 用户截图中提到的一些点,经检查已在现有章节中覆盖,列出供确认。

| 截图内容 | 检查结果 | 位置 |
|---------|---------|------|
| "他和vllm都是部署的" → vLLM 部署 | ✅ 已覆盖 | 10-§3.5(完整部署示例) |
| "分离 / Ollama / OneAI" → P/D 分离 | ✅ 已覆盖 | 10-§9.5(P/D 分离深度) |
| "还有向量的部分embedding" → Embedding | ⚠️ 部分覆盖 | 09-§7(Embedding 概念);10-§9.6 提到 MIG 可跑 Embedding 服务,但缺少独立部署节 → 见问题 #1 |
| "loop和多agent通信的还有harness还有prompt" | ⚠️ 需加强 | 03 章有框架对比但缺能力矩阵 → 见问题 #3 |
| "计算库构建的轻量级本地推理框架(llama.cpp)" | ✅ 已覆盖 | 10-§8(llama.cpp 深度) |
| "这几个都没(loop/harness/multi-agent/prompt)" | ⚠️ 需加强 | 指的是某个具体框架缺失这些能力 → 需在 03 章补充能力矩阵 |

---

## 六、迭代计划

### v4.8(下次迭代建议优先级)

1. **[高]** Embedding 服务部署独立节(10 章):TEI / vLLM Embedding / Sentence-Transformers 部署 + 性能对比
2. **[高]** Ollama vs vLLM 量化对比表(10 章):同模型同硬件的 QPS/TTFT/显存/并发对比
3. **[高]** Agent 框架能力矩阵(03 章):Loop / Multi-Agent 通信 / Harness / Prompt 管理 横向对比
4. **[高]** 待确认问题 #1/#2/#7:核实 vLLM V1 指标名和 LangGraph 回滚行为
5. **[中]** 推理模型部署特殊考量(10 章):reasoning token 对延迟/成本/KV Cache 的影响量化
6. **[中]** 滑动窗口深度补充(10 章):Python/Redis 实现 + 与令牌桶场景量化对比

### v4.9+(远期)

- Edge/边缘部署量化(手机/Jetson 树莓派)
- Restate/Inngest 与 Temporal 对比(05 章)
- FlashAttention-2/3 加速比量化(09 章)
- ReAct vs Plan-Execute vs Reflexion 量化对比(06 章)

---

**📅 最后更新:** 2026-07-28
**📊 对应版本:** v4.7
