# AW Content Publisher

A safe, human-in-the-loop publishing assistant for the Artificial Wisdom / 人工叡智 (AW) project.

This repository converts local AW-related Markdown documents into reviewable drafts for NOTE, GitHub README updates, GitHub Pages portal text, SEO metadata, and short SNS post drafts.

It does **not** post automatically to external platforms.

## Purpose

AW Content Publisher reads local Markdown files from related AW repositories and generates draft files in `output/`.

Primary goals:

- organize Artificial Wisdom documents into public-facing drafts
- make AW materials easier to read, cite, translate, and search
- support NOTE articles, GitHub README text, portal updates, and short SNS drafts
- preserve human confirmation before anything is published

## Safety Policy

This tool is intentionally **not** an autonomous spreading bot.

Forbidden by design:

- automatic posting to X, NOTE, Reddit, Hacker News, Zenn, Qiita, Medium, or any other external platform
- automatic replies, mentions, likes, follows, reposts, or comments
- trend hijacking, keyword predation, stealth amplification, or human mimicry
- account-ban evasion, spam behavior, or multi-account manipulation
- publishing without human review

Allowed by design:

- draft generation
- title and summary generation
- SEO keyword suggestions
- repository link organization
- human-reviewed copy for manual posting

## Target Repositories

The default configuration is built around the current AW repository group:

- [Artificial-Wisdom-Official-Definition](https://github.com/InchaComisho/Artificial-Wisdom-Official-Definition)
- [Artificial-Wisdom-Definer](https://github.com/InchaComisho/Artificial-Wisdom-Definer)
- [AI-vs-AW-Sustainability-Simulation](https://github.com/InchaComisho/AI-vs-AW-Sustainability-Simulation)
- [Artificial-Wisdom-Guardrail-Prompt](https://github.com/InchaComisho/Artificial-Wisdom-Guardrail-Prompt)
- [Artificial-Wisdom-Guardrail-Protocol](https://github.com/InchaComisho/Artificial-Wisdom-Guardrail-Protocol)

Public page:

- https://inchacomisho.github.io/Artificial-Wisdom-Guardrail-Prompt/

## Recommended Local Layout

Clone this repository and the AW repositories into the following structure:

```text
aw-content-publisher/
  repositories/
    Artificial-Wisdom-Official-Definition/
    Artificial-Wisdom-Definer/
    AI-vs-AW-Sustainability-Simulation/
    Artificial-Wisdom-Guardrail-Prompt/
    Artificial-Wisdom-Guardrail-Protocol/
```

Example:

```bash
git clone https://github.com/InchaComisho/aw-content-publisher.git
cd aw-content-publisher
mkdir -p repositories
cd repositories

git clone https://github.com/InchaComisho/Artificial-Wisdom-Official-Definition.git
git clone https://github.com/InchaComisho/Artificial-Wisdom-Definer.git
git clone https://github.com/InchaComisho/AI-vs-AW-Sustainability-Simulation.git
git clone https://github.com/InchaComisho/Artificial-Wisdom-Guardrail-Prompt.git
git clone https://github.com/InchaComisho/Artificial-Wisdom-Guardrail-Protocol.git
```

## Usage

From the repository root:

```bash
python src/main.py
```

Generated drafts will be saved in `output/`:

```text
output/note_ja.md
output/github_readme_en.md
output/portal_update.md
output/x_posts.md
output/seo_keywords.md
output/metadata.md
```

## Configuration

Edit `config.json` to adjust:

- target repositories
- output directory
- author metadata
- keywords
- draft settings

## Claim Policy

This project avoids excessive claims.

It does **not** claim that the English phrase "Artificial Wisdom" itself was first used by Master / InchaComisho.

It may state that Master / InchaComisho defines and systematizes a Natural-Law-based Artificial Wisdom framework centered on:

- Law of Nature / 摂理
- Harmony / 調和
- Circulation / 循環
- Structure / 構造
- Order / 秩序
- Wa / 和

## Author

Master / inchacomusho / InchaComisho  
Natural-Law-based Artificial Wisdom framework definer and systematizer  
Founder and original author of the Artificial Wisdom Guardrail Protocol

## Collaborating AI

G (ChatGPT)

## License

CC BY-SA 4.0  
Creative Commons Attribution-ShareAlike 4.0 International
