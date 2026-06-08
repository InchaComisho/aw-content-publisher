from __future__ import annotations

import json
from pathlib import Path

from content_analyzer import analyze_documents
from note_generator import generate_note_article_ja
from repo_reader import read_markdown_repositories
from sns_generator import generate_x_posts


def main() -> None:
    base_dir = Path(__file__).resolve().parents[1]
    config = _load_config(base_dir / "config.json")

    _assert_guardrails(config)

    documents = read_markdown_repositories(base_dir, config["repositories"])
    analysis = analyze_documents(documents)

    outputs = config["outputs"]
    _write_output(base_dir / outputs["note_ja"], generate_note_article_ja(analysis, config))
    _write_output(base_dir / outputs["x_posts"], generate_x_posts(analysis, config))
    _write_output(base_dir / outputs["analysis_summary"], _generate_analysis_summary(analysis, config))

    print(f"Loaded Markdown documents: {analysis.document_count}")
    print(f"Generated: {outputs['note_ja']}")
    print(f"Generated: {outputs['x_posts']}")
    print(f"Generated: {outputs['analysis_summary']}")


def _load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _assert_guardrails(config: dict) -> None:
    policy = config["generation_policy"]
    forbidden_flags = [
        "external_posting_api_allowed",
        "auto_reply_allowed",
        "auto_mention_allowed",
        "auto_like_allowed",
        "auto_follow_allowed",
        "trend_hijacking_allowed",
        "ban_evasion_allowed",
        "human_impersonation_allowed",
        "multi_account_operation_allowed",
    ]
    if not policy.get("human_review_required", False):
        raise ValueError("Guardrail violation: human_review_required must be true.")
    enabled = [flag for flag in forbidden_flags if policy.get(flag, False)]
    if enabled:
        raise ValueError(f"Guardrail violation: forbidden capabilities enabled: {', '.join(enabled)}")


def _write_output(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _generate_analysis_summary(analysis, config: dict) -> str:
    repos = "\n".join(f"- {repo}" for repo in analysis.repositories) or "- No repositories loaded."
    concepts = "\n".join(
        f"- {name}: {count}" for name, count in analysis.concept_counts.items() if count > 0
    ) or "- No configured concepts found yet."
    headings = []
    for repo, repo_headings in analysis.headings_by_repo.items():
        headings.append(f"## {repo}")
        headings.extend(f"- {heading}" for heading in repo_headings)
        headings.append("")

    return f"""# Analysis Summary

Human review required: {config["generation_policy"]["human_review_required"]}
External posting API allowed: {config["generation_policy"]["external_posting_api_allowed"]}

Loaded Markdown documents: {analysis.document_count}

## Repositories

{repos}

## Important Concept Counts

{concepts}

## Extracted Headings

{chr(10).join(headings).strip() or "No headings extracted yet."}

## License

{config["project"]["license"]}
"""


if __name__ == "__main__":
    main()

