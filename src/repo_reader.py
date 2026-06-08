from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MarkdownDocument:
    repo_name: str
    path: Path
    title: str
    text: str


def read_markdown_repositories(base_dir: Path, repositories: list[dict]) -> list[MarkdownDocument]:
    documents: list[MarkdownDocument] = []

    for repo in repositories:
        repo_name = repo["name"]
        repo_path = (base_dir / repo["path"]).resolve()
        if not repo_path.exists():
            continue

        for path in sorted(repo_path.rglob("*.md")):
            if _should_skip(path):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            documents.append(
                MarkdownDocument(
                    repo_name=repo_name,
                    path=path,
                    title=_extract_title(path, text),
                    text=text,
                )
            )

    return documents


def _extract_title(path: Path, text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return path.stem


def _should_skip(path: Path) -> bool:
    ignored_parts = {".git", "node_modules", ".venv", "venv", "__pycache__"}
    return any(part in ignored_parts for part in path.parts)

