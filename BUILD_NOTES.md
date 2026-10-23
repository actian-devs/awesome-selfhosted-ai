# Build notes

Built: 2026-10-23 (Africa/Lagos)
Revised: 2026-10-23 after Henry's scaffold review

**Total entries:** 166

## Per category

- Agents & memory: 18
- Vector databases: 15
- RAG & orchestration: 14
- Eval & observability: 10
- UIs: 11
- Datasets & benchmarks: 11
- Local runtimes: 12
- Inference servers: 9
- Compute & GPUs: 9
- Deployment & infra: 10
- Learning: 18
- Communities: 7
- Privacy & offline: 8
- Open-weight models: 7
- Embeddings: 6
- Related: 1

## Dropped / fixed during URL verify

- Dropped: https://github.com/ironcorelabs/cloaked-ai (404) → replaced with IronCoreLabs/ironcore-alloy
- Dropped: https://github.com/jina-ai/jina-embeddings-v3 (404) → replaced with huggingface.co/jinaai/jina-embeddings-v3
- Fixed: Phi collection URL 404 → https://huggingface.co/microsoft/phi-4
- Fixed: KubeRay → https://github.com/kuberay-project/kuberay
- Replaced weak vLLM Slack (repo link) with Hugging Face Discord

## Review changes (2026-10-23)

- Renamed: Perplexica → Vane (ItzCrazyKns/Vane); Aphrodite Engine → Sonar (dphnAI/sonar). Both re-sorted alphabetically.
- ROCm: ROCm/ROCm now redirects to the archived ROCm/legacy-rocm-build; entry points at ROCm/TheRock, the maintained build and distribution repo.
- Quivr: moved to The-Vibe-Company/quivr (active); description updated because the project changed scope.
- Canonical URLs: OpenHands/OpenHands, openinterpreter/openinterpreter, Giskard-AI/giskard-oss, zai-org/GLM-4.
- Removed: Voyage AI (client for a hosted API, not self-hostable).
- Removed: Actian Discord entry under Communities (awesome-lint duplicate-link error; the Discord badge at the top remains).
- Removed: "How to Self-Host mem0 with a Local Vector Store" from Learning (effectively a VectorAI DB product how-to).
- Added to Learning (vendor-neutral): Agents Course, GenAI Agents, Generative AI for Beginners, RAG Techniques, The Illustrated Transformer. Actian entries are now 8 of 18 and interleave alphabetically.
- Moved: Vector DB sizing calculator from Compute & GPUs to a new Related section.
- Dropped trailing license/language tags (awesome-lint punctuation rule). `⊘ Proprietary` stays inside the sentence for VectorAI DB and LobeHub (LobeHub Community License is not open source).
- Awesome badge moved onto the heading line (awesome-lint requirement).
- lint.yml runs on pull requests only until the repo is 30 days old; links.yml uses lychee.toml, which excludes actian.com and reddit.com (403 to bots).

## Pruned after first snapshot (2026-W43)

Removed 13 entries that broke CONTRIBUTING.md rule 2:

- Archived: AutoAWQ, AutoGPTQ, Flowise (wound down by its team; archived 2026-08-13), Hugging Face TGI (its README recommends vLLM and SGLang instead), LLM Guard, Mistral (mistral-inference).
- Software with no push in 6+ months: ExLlamaV2, GPT4All, MetaGPT, Nomic Embed, Ragas, Seldon Core, SuperAGI.

Added the `kind` field. Models, datasets, learning resources, and communities are exempt from the push rule, so DeepSeek-R1, Llama models, Qwen3, EleutherAI The Pile, BEIR, LLM Course, llm.c, and nanoGPT stay.

## Notes

- `README.md` is generated from `data/` by `scripts/build_readme.py`; see CONTRIBUTING.md. A weekly workflow records activity in `data/history/` (first snapshot: 2026-W43).
- Descriptions are drafts; humans rewrite before sindresorhus submission (see MAINTAINERS.md).
- Learning includes a curated Actian concept-guide subset (disclosed in Footnotes); Actian product how-tos excluded.
- VectorAI DB listed alphabetically under Vector databases with `⊘ Proprietary`.
- Publish by creating actian-devs/awesome-selfhosted-ai and pushing this folder, as described in AGENT_INSTRUCTIONS.md.
