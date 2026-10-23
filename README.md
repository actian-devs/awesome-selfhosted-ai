# Awesome Self-Hosted AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/t26wZw22X)

The full stack for running AI on your own hardware: models, inference, embeddings, vector databases, agents, GPUs, and deployment.

## Contents

- [Agents & memory](#agents--memory)
- [Vector databases](#vector-databases)
- [RAG & orchestration](#rag--orchestration)
- [Eval & observability](#eval--observability)
- [UIs](#uis)
- [Datasets & benchmarks](#datasets--benchmarks)
- [Local runtimes](#local-runtimes)
- [Inference servers](#inference-servers)
- [Compute & GPUs](#compute--gpus)
- [Deployment & infra](#deployment--infra)
- [Learning](#learning)
- [Communities](#communities)
- [Privacy & offline](#privacy--offline)
- [Open-weight models](#open-weight-models)
- [Embeddings](#embeddings)
- [Related](#related)

## Agents & memory

- [Actian Agent Memory Hub](https://github.com/actian-devs/agent-memory-hub) - Free resources for building persistent memory into AI agents.
- [Agno](https://github.com/agno-agi/agno) - Lightweight library for building multimodal agents.
- [Aider](https://github.com/Aider-AI/aider) - AI pair programming in your terminal.
- [AutoGen](https://github.com/microsoft/autogen) - Microsoft's framework for multi-agent conversations.
- [Browser Use](https://github.com/browser-use/browser-use) - Make AI agents control a real browser.
- [CAMEL](https://github.com/camel-ai/camel) - Communicative agents for role-playing research.
- [cognee](https://github.com/topoteretes/cognee) - Memory and knowledge engine for AI agents.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Multi-agent orchestration with role-playing crews.
- [Graphiti](https://github.com/getzep/graphiti) - Temporal knowledge graphs for agent memory.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Stateful, graph-based agent workflows.
- [Letta](https://github.com/letta-ai/letta) - Stateful agents with long-term memory.
- [Mastra](https://github.com/mastra-ai/mastra) - TypeScript framework for AI agents and workflows.
- [MCP servers](https://github.com/modelcontextprotocol/servers) - Reference Model Context Protocol server implementations.
- [Mem0](https://github.com/mem0ai/mem0) - Memory layer for AI agents and apps.
- [Open Interpreter](https://github.com/openinterpreter/openinterpreter) - Natural-language interface for a local code interpreter.
- [OpenHands](https://github.com/OpenHands/OpenHands) - Open platform for AI software development agents.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Agent framework built on Pydantic validation.
- [smolagents](https://github.com/huggingface/smolagents) - Minimal code-writing agents from Hugging Face.

## Vector databases

- [Actian VectorAI DB](https://www.actian.com/databases/vectorai-db/) - Self-hosted vector database for on-prem and edge; free Community Edition for local development (`⊘ Proprietary`).
- [Chroma](https://github.com/chroma-core/chroma) - Embedding database for AI applications.
- [Elasticsearch](https://github.com/elastic/elasticsearch) - Search and analytics engine with dense vector support.
- [Faiss](https://github.com/facebookresearch/faiss) - Library for efficient similarity search over dense vectors.
- [LanceDB](https://github.com/lancedb/lancedb) - Embedded, serverless vector database on Lance.
- [Marqo](https://github.com/marqo-ai/marqo) - End-to-end vector search engine with multimodal models.
- [Milvus](https://github.com/milvus-io/milvus) - Distributed cloud-native vector database.
- [OpenSearch](https://github.com/opensearch-project/OpenSearch) - Community-driven search engine with vector search.
- [pgvector](https://github.com/pgvector/pgvector) - Open-source vector similarity search for PostgreSQL.
- [Qdrant](https://github.com/qdrant/qdrant) - High-performance vector search engine written in Rust.
- [Redis](https://github.com/redis/redis) - In-memory data store with RediSearch vector indexes.
- [Typesense](https://github.com/typesense/typesense) - Fast typo-tolerant search engine with vector search.
- [Vald](https://github.com/vdaas/vald) - Distributed vector search engine for Kubernetes.
- [Vespa](https://github.com/vespa-engine/vespa) - Open-source big data serving engine with vector ranking.
- [Weaviate](https://github.com/weaviate/weaviate) - Open-source vector database with hybrid search.

## RAG & orchestration

- [Dify](https://github.com/langgenius/dify) - Self-hostable platform for agentic workflows and RAG.
- [Docling](https://github.com/docling-project/docling) - Convert PDFs and office documents for generative AI.
- [DSPy](https://github.com/stanfordnlp/dspy) - Framework for programming, not prompting, LLM pipelines.
- [GraphRAG](https://github.com/microsoft/graphrag) - Graph-based retrieval-augmented generation from Microsoft.
- [Haystack](https://github.com/deepset-ai/haystack) - Orchestration framework for RAG and agent pipelines.
- [LangChain](https://github.com/langchain-ai/langchain) - Framework for building LLM applications and agents.
- [LightRAG](https://github.com/HKUDS/LightRAG) - Simple and fast graph-enhanced RAG framework.
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for connecting documents to LLMs.
- [MaxKB](https://github.com/1Panel-dev/MaxKB) - Open-source knowledge-base Q&A system based on LLMs.
- [Quivr](https://github.com/The-Vibe-Company/quivr) - Open-source engine for search and monitoring over continuous content streams.
- [RAGFlow](https://github.com/infiniflow/ragflow) - Self-hostable RAG engine with deep document understanding.
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) - SDK for integrating LLMs into applications.
- [txtai](https://github.com/neuml/txtai) - All-in-one embeddings database and semantic search.
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - Open-source ETL for transforming documents into LLM-ready data.

## Eval & observability

- [DeepEval](https://github.com/confident-ai/deepeval) - Unit-test style evaluation framework for LLM apps.
- [Giskard](https://github.com/Giskard-AI/giskard-oss) - Open-source testing and evaluation for ML and LLM models.
- [Helicone](https://github.com/Helicone/helicone) - Open-source LLM observability and gateway.
- [Langfuse](https://github.com/langfuse/langfuse) - Self-hostable tracing, evals, and prompt management.
- [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) - Standard few-shot evaluation harness for language models.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry instrumentation for LLM applications.
- [Opik](https://github.com/comet-ml/opik) - Open-source platform for LLM tracing and evaluation.
- [Phoenix](https://github.com/Arize-ai/phoenix) - Open-source AI observability and evaluation.
- [promptfoo](https://github.com/promptfoo/promptfoo) - CLI for prompt testing, comparisons, and red-teaming.
- [TruLens](https://github.com/truera/trulens) - Evaluate and track LLM app quality with feedback functions.

## UIs

- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) - All-in-one desktop and Docker AI app with built-in RAG.
- [Big-AGI](https://github.com/enricoros/big-AGI) - Personal AI suite with personas, voice, and tools.
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI) - Node-based UI and backend for diffusion models.
- [Continue](https://github.com/continuedev/continue) - Open-source coding assistant that works with local models.
- [LibreChat](https://github.com/LibreChat-AI/LibreChat) - Multi-provider self-hosted ChatGPT-style UI.
- [LobeHub](https://github.com/lobehub/lobehub) - Chat and agent workspace UI (`⊘ Proprietary`).
- [Open WebUI](https://github.com/open-webui/open-webui) - Self-hosted chat UI for local and remote models.
- [SillyTavern](https://github.com/SillyTavern/SillyTavern) - Power-user chat frontend for local LLM backends.
- [Tabby](https://github.com/TabbyML/tabby) - Self-hosted coding assistant with local models.
- [Text generation web UI](https://github.com/oobabooga/textgen) - Gradio desktop UI for running local LLMs.
- [Vane](https://github.com/ItzCrazyKns/Vane) - Open-source AI-powered answering engine, formerly Perplexica.

## Datasets & benchmarks

- [ANN-Benchmarks](https://github.com/erikbern/ann-benchmarks) - Benchmarks for approximate nearest-neighbour libraries.
- [BEIR](https://github.com/beir-cellar/beir) - Heterogeneous benchmark for information retrieval.
- [Datasets](https://github.com/huggingface/datasets) - Library to load and process machine-learning datasets.
- [Dolma](https://github.com/allenai/dolma) - AI2 open pretraining corpus and inspection toolkit.
- [EleutherAI The Pile](https://github.com/EleutherAI/the-pile) - Large open-source language modelling dataset.
- [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb) - Large cleaned web dataset for LLM pretraining.
- [LLM Datasets](https://github.com/mlabonne/llm-datasets) - Curated datasets and tools for LLM post-training.
- [LMSYS Chatbot Arena](https://github.com/lm-sys/FastChat) - Open platform for training, serving, and evaluating chat models.
- [MTEB](https://github.com/embeddings-benchmark/mteb) - Massive Text Embedding Benchmark across languages.
- [RedPajama-Data](https://github.com/togethercomputer/RedPajama-Data) - Code to prepare large datasets for LLM pretraining.
- [VectorDBBench](https://github.com/zilliztech/VectorDBBench) - Open benchmark tool for vector databases.

## Local runtimes

- [candle](https://github.com/huggingface/candle) - Minimalist ML framework for Rust with GPU support.
- [Jan](https://github.com/janhq/jan) - Desktop app that runs models fully offline.
- [KoboldCpp](https://github.com/LostRuins/koboldcpp) - Single-file llama.cpp client with a built-in UI.
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) - Python bindings for llama.cpp with an OpenAI-compatible API.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - C/C++ LLM inference on CPUs and GPUs; home of GGUF.
- [llamafile](https://github.com/mozilla-ai/llamafile) - Single-file executables that bundle a model and runtime.
- [LocalAI](https://github.com/mudler/LocalAI) - OpenAI-compatible API server for local models on any hardware.
- [MLC LLM](https://github.com/mlc-ai/mlc-llm) - Compiler-based LLM deployment across GPUs, phones, and browsers.
- [MLX](https://github.com/ml-explore/mlx) - Apple array framework for machine learning on Apple silicon.
- [mlx-lm](https://github.com/ml-explore/mlx-lm) - Run LLMs with MLX on Apple silicon.
- [Ollama](https://github.com/ollama/ollama) - Run open-weight LLMs locally behind a CLI and REST API.
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp) - Port of OpenAI Whisper to C/C++ for local speech recognition.

## Inference servers

- [BentoML](https://github.com/bentoml/BentoML) - Package and serve AI models as production APIs.
- [CTranslate2](https://github.com/OpenNMT/CTranslate2) - Fast inference engine for Transformer models.
- [KTransformers](https://github.com/kvcache-ai/ktransformers) - CPU/GPU hybrid inference for large MoE models.
- [LMDeploy](https://github.com/InternLM/lmdeploy) - Toolkit to compress, deploy, and serve LLMs.
- [SGLang](https://github.com/sgl-project/sglang) - Fast serving framework for LLMs and vision-language models.
- [Sonar](https://github.com/dphnAI/sonar) - Large-scale LLM inference engine based on vLLM, formerly Aphrodite Engine.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - NVIDIA optimized library for LLM inference.
- [Triton Inference Server](https://github.com/triton-inference-server/server) - Multi-framework model server for cloud and edge.
- [vLLM](https://github.com/vllm-project/vllm) - High-throughput and memory-efficient LLM serving engine.

## Compute & GPUs

- [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) - 8-bit and 4-bit optimizers and quantization for PyTorch.
- [exo](https://github.com/exo-explore/exo) - Run frontier models across a cluster of everyday devices.
- [ggml](https://github.com/ggml-org/ggml) - Tensor library for machine learning on CPUs and GPUs.
- [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) - Enable GPU access inside containers.
- [NVIDIA device plugin for Kubernetes](https://github.com/NVIDIA/k8s-device-plugin) - Schedule NVIDIA GPUs in Kubernetes clusters.
- [nvitop](https://github.com/XuehaiPan/nvitop) - Interactive NVIDIA GPU process viewer.
- [nvtop](https://github.com/Syllo/nvtop) - GPU and accelerator process monitor for the terminal.
- [OpenVINO](https://github.com/openvinotoolkit/openvino) - Intel toolkit for optimized inference on CPUs and GPUs.
- [ROCm](https://github.com/ROCm/TheRock) - AMD open software platform for GPU computing, built and distributed through TheRock.

## Deployment & infra

- [GPUStack](https://github.com/gpustack/gpustack) - GPU cluster manager for high-performance model serving.
- [KServe](https://github.com/kserve/kserve) - Standardized model serving on Kubernetes.
- [KubeRay](https://github.com/kuberay-project/kuberay) - Toolkit to run Ray applications on Kubernetes.
- [LiteLLM](https://github.com/BerriAI/litellm) - OpenAI-compatible gateway across 100+ model backends.
- [llm-d](https://github.com/llm-d/llm-d) - Kubernetes-native distributed LLM inference.
- [MLflow](https://github.com/mlflow/mlflow) - Open-source platform for the ML lifecycle and model serving.
- [OpenLLM](https://github.com/bentoml/OpenLLM) - Operate LLMs in production with an OpenAI-compatible API.
- [Portkey Gateway](https://github.com/Portkey-AI/gateway) - Open-source AI gateway with guardrails.
- [Ray Serve](https://github.com/ray-project/ray) - Scalable model serving library within Ray.
- [SkyPilot](https://github.com/skypilot-org/skypilot) - Run AI workloads on any cloud or cluster.

## Learning

- [Agents Course](https://github.com/huggingface/agents-course) - Free Hugging Face course on building AI agents.
- [AI Agent Memory Architecture](https://dev.to/actiandev/what-you-need-to-know-about-ai-agent-memory-architecture-49ek) - Overview of agent memory architecture patterns.
- [Comparing Embedded Vector Databases](https://www.actian.com/blog/developer/comparing-embedded-vector-databases/) - Comparison of embedded vector database options for local stacks.
- [GenAI Agents](https://github.com/NirDiamant/GenAI_Agents) - Notebook tutorials covering agent techniques from simple bots to multi-agent systems.
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) - Microsoft course of 21 lessons on building generative AI applications.
- [How to Evaluate Vector Databases](https://www.actian.com/blog/databases/how-to-evaluate-vector-databases-in-2026/) - Practical criteria for evaluating vector databases.
- [How to Measure RAG System Performance](https://dev.to/actiandev/how-to-measure-rag-system-performance-1i1h) - Guide to measuring retrieval and generation quality.
- [Hugging Face course](https://github.com/huggingface/course) - Free course on Transformers and modern NLP.
- [LLM Course](https://github.com/mlabonne/llm-course) - Roadmaps and notebooks to learn large language models.
- [llm.c](https://github.com/karpathy/llm.c) - LLM training implemented in raw C and CUDA.
- [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) - Build a GPT-style model in PyTorch step by step.
- [nanoGPT](https://github.com/karpathy/nanoGPT) - Minimal, fast repository for training medium-sized GPTs.
- [Quantization Levels for Edge LLM Deployment](https://www.actian.com/blog/developer/which-quantization-level-should-you-use-for-edge-llm-deployment/) - Guidance on choosing quantization levels for edge LLMs.
- [RAG Techniques](https://github.com/NirDiamant/RAG_Techniques) - Notebook tutorials for advanced retrieval-augmented generation techniques.
- [Should You Use RAG or Fine-Tune](https://www.actian.com/blog/databases/should-you-use-rag-or-fine-tune-your-llm/) - Decision guide between RAG and fine-tuning.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) - Visual walkthrough of how the Transformer architecture works.
- [What Is a Vector Database](https://www.youtube.com/watch?v=pesWa2wod0k) - Plain-English introduction to vector databases.
- [What Is Agent Memory](https://www.youtube.com/watch?v=lq9AVW87B-g) - Video on agent memory architecture and deployment patterns.

## Communities

- [Hugging Face Discord](https://discord.com/invite/hugging-face-879548962464493619) - Community Discord for Hugging Face users and model builders.
- [Hugging Face Forums](https://discuss.huggingface.co/) - Open-model Q&A and community support.
- [Latent Space](https://www.latent.space/) - AI engineering podcast, newsletter, and community.
- [MLOps Community](https://mlops.community/) - Practitioner community and events around MLOps.
- [Ollama Discord](https://discord.com/invite/ollama) - Community server for Ollama users.
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) - Largest community focused on local LLMs.
- [r/selfhosted](https://www.reddit.com/r/selfhosted/) - Community for running software on your own hardware.

## Privacy & offline

- [Cloaked AI (IronCore Alloy)](https://github.com/IronCoreLabs/ironcore-alloy) - Encrypt embeddings while preserving vector search.
- [Khoj](https://github.com/khoj-ai/khoj) - Self-hostable personal AI second brain.
- [localGPT](https://github.com/PromtEngineer/localGPT) - Chat with documents on your own device with no data leaving.
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - Programmable guardrails for LLM conversational systems.
- [Presidio](https://github.com/data-privacy-stack/presidio) - Detect, redact, and anonymize PII in text and images.
- [PrivateGPT](https://github.com/zylon-ai/private-gpt) - Private document Q&A API that runs fully offline.
- [PurpleLlama](https://github.com/meta-llama/PurpleLlama) - Meta safety tools including Llama Guard.
- [Speaches](https://github.com/speaches-ai/speaches) - OpenAI-compatible local speech-to-text and text-to-speech.

## Open-weight models

- [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) - Open-weight reasoning model family and paper.
- [Gemma](https://github.com/google-deepmind/gemma) - Google DeepMind open-weight model library.
- [GLM-4](https://github.com/zai-org/GLM-4) - Zhipu AI open-weight bilingual model series.
- [gpt-oss](https://github.com/openai/gpt-oss) - OpenAI open-weight models and reference code.
- [Llama models](https://github.com/meta-llama/llama-models) - Meta Llama model cards and utilities.
- [Phi](https://huggingface.co/microsoft/phi-4) - Microsoft Phi open-weight small language models.
- [Qwen3](https://github.com/QwenLM/Qwen3) - Alibaba open-weight large language model family.

## Embeddings

- [FastEmbed](https://github.com/qdrant/fastembed) - Lightweight ONNX-based embedding generation.
- [FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) - BGE embedding and reranker models.
- [Infinity](https://github.com/michaelfeil/infinity) - High-throughput embedding and reranking server.
- [Jina Embeddings](https://huggingface.co/jinaai/jina-embeddings-v3) - Multilingual embedding models from Jina AI.
- [Sentence Transformers](https://github.com/huggingface/sentence-transformers) - Library for computing and fine-tuning text embeddings.
- [Text Embeddings Inference](https://github.com/huggingface/text-embeddings-inference) - Hugging Face server for embedding and reranker models.

## Related

Tools from the Actian developer community that support self-hosted AI stacks.

- [Vector DB sizing calculator](https://github.com/actian-devs/vector-db-calculator) - Estimate memory and storage for any vector workload in about 30 seconds.

## Footnotes

This list is maintained with support from the Actian developer community. Actian products appear under the same inclusion rules as every other project: alphabetical order, factual one-line descriptions, and honest license tags (`⊘ Proprietary` when the software is not open source).

Some Learning entries are Actian-authored concept guides; they are included as educational resources, not as peer software, and do not replace independent courses.

Discussions happen in the Actian Discord linked at the top of this page. Contributions: see [CONTRIBUTING.md](CONTRIBUTING.md).
