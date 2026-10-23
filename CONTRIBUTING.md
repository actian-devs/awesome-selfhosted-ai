# Contributing

Thanks for helping grow Awesome Self-Hosted AI.

## Scope

In scope: software, models, datasets, learning resources, and communities that help people run AI on hardware they control (laptop, on-prem, edge, or air-gapped). Libraries and frameworks are welcome when they are useful for self-hosted stacks.

Out of scope: managed-only SaaS with no self-host path, affiliate or tracking links, and marketing pages without a runnable project.

## Inclusion criteria

1. Runs on hardware you control (self-host, offline, or air-gapped where claimed).
2. Software: at least one push in the last 6 months, not archived, with install docs that work. Models, datasets, learning resources, and communities (`kind` other than `software`) are exempt from the push rule but must not be archived or abandoned.
3. Free to self-host. Non-open-source projects must be tagged `⊘ Proprietary` (or the exact license).
4. Clear traction or a clear niche, explained in the PR.
5. One entry per project. No affiliate, referral, or tracking links in entries.
6. Descriptions are factual, human-written, one sentence, and end with a period. No marketing copy.

**AI-generated list content is not accepted.** Drafts may be assisted by tools, but a human must write and take responsibility for every description. The main Awesome lists reject AI-written entries; we follow that bar.

## Removal policy

Projects that are archived, abandoned (no push for 6–12 months), misleading about self-hosting, or repeatedly broken in the weekly link check may be removed after an issue is opened.

## How to add an entry

`README.md` is generated. Do not edit it by hand; add a data file instead.

1. Copy [`data/entries/_template.yml`](data/entries/_template.yml) to `data/entries/<slug>.yml`. The slug is the name in lowercase with other characters replaced by `-` (for example, `llama.cpp` becomes `llama-cpp.yml`).
2. Fill in the required fields: `name`, `url`, `category` (an id from [`data/categories.yml`](data/categories.yml)), `description`, `proprietary`, and `added`. Set `kind` to `model`, `dataset`, `learning`, or `community` when the entry is not software; it defaults to `software`.
3. Fill in optional fields only when you have checked them yourself: `license`, `language`, `self_host`, `hardware`, `offline_capable`, `openai_compatible_api`, `commercial_use_ok`. If you installed and ran the project, add `last_verified`, `verified_by`, and `verified_on`.
4. Run the checks and regenerate the README:

```bash
pip install -r requirements.txt
python3 scripts/validate.py
python3 scripts/build_readme.py
```

5. Commit both the data file and the regenerated `README.md`.

The generator sorts entries alphabetically and renders each one as:

```markdown
- [Name](https://example.com) - Short factual description.
```

Set `proprietary: true` for projects that are not open source; the README then shows `(`⊘ Proprietary`)` before the period. Do not write the tag in the description yourself.

## Verifying an entry

A verified entry means a person installed and ran the project on the hardware named in `verified_on`. Verification PRs that only add `last_verified`, `verified_by`, and `verified_on` to an existing entry are welcome, and project maintainers can verify their own entries.

## Activity tracking

A weekly workflow records stars, last push, releases, and contributor counts for every GitHub entry in `data/history/`, and opens a PR that lists archived, stale (software only), renamed, or missing projects. Maintainers use that PR to apply the removal policy below.

## New categories

Propose a new category only with at least three qualifying entries and a short rationale in the PR.

## Discuss first

Open a thread in the [#self-hosted-ai](https://discord.gg/t26wZw22X) Discord channel before large changes or category proposals.

## Review SLA

Maintainers aim to triage PRs within **72 hours**.

## Code of conduct

See [code-of-conduct.md](code-of-conduct.md).
