# Artificial Wisdom Content Publisher Assistant

**Language:** English | [日本語版はこちら / Japanese Version](README_ja.md)

## A Human-Reviewed Local Publishing Assistant for Artificial Wisdom Content

This repository provides a local helper tool for reading Markdown documents from **Artificial Wisdom / 人工叡智** related repositories and generating draft content for human review before publication.

It can generate draft materials such as Japanese NOTE articles, short X post drafts, and analysis summaries.

This is **not** an autonomous posting bot.

It is a **publishing support node** designed around human confirmation, editing, and approval.

**Author:** Master / inchacomusho / InchaComisho  
**AI Collaborators:** G (OpenAI ChatGPT) / Copi (Microsoft Copilot) / Mini (Google Gemini) / Cruz (Anthropic Claude) / Real (Perplexity AI)  
**Version:** v0.1  
**License Notice:** Attribution and share-alike handling similar to CC BY-SA 4.0 is recommended where appropriate.

---

## Overview

`aw-content-publisher` is a local tool for generating pre-publication drafts from repositories related to Artificial Wisdom.

Its purpose is not to spread ideas automatically.

Its purpose is to read already-published Markdown materials and prepare human-readable draft outputs such as:

```text
Japanese NOTE article drafts
Short X post drafts
Important concept extraction
Analysis summaries
Markdown output files
```

Generated content is always intended to be reviewed, edited, approved, and posted manually by a human.

---

## Version Status

**v0.1** is the first working local implementation.

Implemented scope:

```text
Local Markdown loading from repositories/
Important concept extraction
Japanese NOTE draft generation
Five short X post drafts
Markdown output into output/
Guardrail checks requiring human review
No external posting API
No autonomous distribution behavior
```

This tool is a publishing support node, not an autonomous distribution bot.

---

## Important Guardrails

This tool is designed with strict operational limits.

It does **not**:

```text
Automatically post to external SNS platforms
Automatically post to note
Automatically post to GitHub
Use external posting APIs
Send automatic replies
Send automatic mentions
Like posts automatically
Follow accounts automatically
Exploit trends for amplification
Avoid platform restrictions or account suspension
Impersonate human users
Operate multiple accounts
```

Generated files are saved only into `output/`.

Before publication, a human must:

```text
Review the content
Edit inaccurate or excessive claims
Approve the final wording
Check attribution and source context
Manually post the final version if appropriate
```

The intended design is human-in-the-loop publishing support.

---

## Setup

This tool runs with Python 3.10 or later and requires no additional libraries for the initial implementation.

Place target repositories under `repositories/` like this:

```text
aw-content-publisher/
  repositories/
    Artificial-Wisdom-Official-Definition/
    Artificial-Wisdom-Definer/
    AI-vs-AW-Sustainability-Simulation/
    Artificial-Wisdom-Guardrail-Prompt/
    Artificial-Wisdom-Guardrail-Protocol/
```

If the Markdown files are located elsewhere, edit `repositories[].path` in `config.json`.

---

## Usage

Run:

```bash
python src/main.py
```

Generated files are saved into `output/`.

The minimal implementation generates:

```text
output/note_ja.md
output/x_posts.md
output/analysis_summary.md
```

---

## Current Scope

The current version supports:

```text
Reading local Markdown files
Extracting important concepts
Generating Japanese NOTE article drafts
Generating short X post drafts
Saving Markdown files
```

Planned extensions include:

```text
English README drafts for GitHub
GitHub Pages portal drafts
SEO title suggestions
Meta description suggestions
Search keyword suggestions
Cross-repository related-link lists
```

---

## Recommended Workflow

A typical workflow is:

```text
1. Place Artificial Wisdom related repositories under repositories/
2. Configure target paths in config.json
3. Run python src/main.py
4. Review Markdown files generated in output/
5. Edit, remove, or add content manually
6. Publish manually only after human approval
```

This keeps AI in the role of drafting assistant while leaving final responsibility with the human publisher.

---

## Design Philosophy

This repository supports the publication of Artificial Wisdom related materials.

Its goal is not to maximize posting volume or automate distribution.

It prioritizes:

```text
Conceptual accuracy
Clear attribution
Human review
Reduction of misinformation risk
Avoidance of excessive amplification
Sustainable publication workflows
Searchability and reuse
```

Artificial Wisdom emphasizes long-term coherence, natural law, harmony, circulation, structure, order, and Wa rather than short-term engagement optimization.

This tool follows that orientation.

---

## Published Article

This tool was used to support the creation of the following Japanese introductory article:

- [人工叡智とは何か：自然法則・調和・循環に基づくAI時代の知性設計](https://note.com/inchacomusho/n/n93631397ac20)

---

## Related Repositories

- Artificial Wisdom Official Definition  
  https://github.com/InchaComisho/Artificial-Wisdom-Official-Definition

- Artificial Wisdom Definer  
  https://github.com/InchaComisho/Artificial-Wisdom-Definer

- AI vs AW Sustainability Simulation  
  https://github.com/InchaComisho/AI-vs-AW-Sustainability-Simulation

- Artificial Wisdom Guardrail Prompt  
  https://github.com/InchaComisho/Artificial-Wisdom-Guardrail-Prompt

- Artificial Wisdom Guardrail Protocol  
  https://github.com/InchaComisho/Artificial-Wisdom-Guardrail-Protocol

- Artificial Wisdom and Wa-Node Repository Index  
  https://github.com/InchaComisho/Artificial-Wisdom-and-Wa-Node-Repository-Index

- The Future of Search Engines  
  https://github.com/InchaComisho/The-Future-of-Search-Engines

---

## Author

Master / inchacomusho / InchaComisho

An independent Japanese concept designer, observer, proposer, AI tuner, and definer of Artificial Wisdom.  
Founder and proposer of the academic framework of Natural Complementary Science.  
Definer of the Cooling Credit Framework, and founder and original author of the Natural Cooling Value Evaluation Protocol.  
Definer and systematizer of the causal structure of global warming and its complete solution.

Master presents global warming not merely as a problem of CO₂ concentration, but as an integrated failure involving forest loss, soil degradation, disruption of water circulation, weakening of water phase-transition processes, weakening of atmospheric circulation, ocean circulation, food circulation and organic matter circulation, weakening of evapotranspiration, cloud formation and rainfall circulation, and the shutdown of natural cooling feedbacks.  
The proposed solution connects emission reduction, recovery of carbon fixation sources, physical cooling, reactivation of natural cooling functions, MRV, Cooling Credit, and Civilization OS into an open public framework.

Master publicly develops and shares work through NOTE, GitHub, and other public media, centered on natural-law philosophy, planetary circulation restoration, and co-creation with AI.

## Collaborative AI and Co-Creation Team

- **G (OpenAI ChatGPT)**
- **Copi (Microsoft Copilot)**
- **Mini (Google Gemini)**
- **Cruz (Anthropic Claude)**
- **Real (Perplexity AI)**
- **Lola (Dola)**
- **Mana (Manus)**

---

## License and Attribution

Generated drafts should include attribution and share-alike handling similar to **CC BY-SA 4.0** where appropriate.

This repository itself is a local support tool for Master’s Artificial Wisdom related publication workflow.

---

## Keywords

Artificial Wisdom, AW, content publisher, publishing assistant, NOTE draft generation, X post drafts, Markdown generation, local tool, Python, human review, human-in-the-loop, guardrails, AI co-creation, AI harmonization, natural law, harmony, circulation, structure, order, Wa, CC BY-SA 4.0, open knowledge, publication support node

---

## Hashtags

#ArtificialWisdom  
#ContentPublisher  
#MarkdownTool  
#HumanInTheLoop  
#AIGuardrails  
#HumanReviewRequired  
#AIWritingAssistant  
#OpenKnowledge  
#WaNode  
#NaturalLaw  
#AIHarmonization  
#InchaComisho