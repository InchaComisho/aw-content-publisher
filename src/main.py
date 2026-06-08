from __future__ import annotations

import json
from pathlib import Path

from content_analyzer import analyze_documents
from generators import (
    generate_github_readme_en,
    generate_metadata,
    generate_note_ja,
    generate_portal_update,
    generate_seo_keywords,
    generate_x_posts,
)
from repo_reader import read_markdown_documents


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config.json"


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def write_output(output_dir: Path, filename: str, content: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / filename).write_text(content, encoding="utf-8")


def main() -> None:
    config = load_config()
    repo_root = ROOT / config.get("repository_root", "repositories")
    output_dir = ROOT / config.get("output_dir", "output")
    repo_names = [repo["name"] for repo in config.get("repositories", [])]

    documents = read_markdown_documents(repo_root, repo_names)
    analysis = analyze_documents(documents)

    write_output(output_dir, "note_ja.md", generate_note_ja(analysis, config))
    write_output(output_dir, "github_readme_en.md", generate_github_readme_en(analysis, config))
    write_output(output_dir, "portal_update.md", generate_portal_update(analysis, config))
    write_output(output_dir, "x_posts.md", generate_x_posts(analysis, config))
    write_output(output_dir, "seo_keywords.md", generate_seo_keywords(analysis, config))
    write_output(output_dir, "metadata.md", generate_metadata(analysis, config))

    print("AW Content Publisher completed.")
    print(f"Documents read: {analysis.document_count}")
    print(f"Output directory: {output_dir}")
    print("Review all generated files before publishing anything.")


if __name__ == "__main__":
    main()
