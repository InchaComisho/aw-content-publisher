from dataclasses import dataclass
from pathlib import Path


@dataclass
class MarkdownDocument:
    repo_name: str
    path: str
    title: str
    content: str


def extract_title(content: str, fallback: str) -> str:
    for line in content.splitlines():
        text = line.strip()
        if text.startswith("# "):
            return text[2:].strip()
    return fallback


def read_markdown_documents(repo_root: Path, repo_names: list[str]) -> list[MarkdownDocument]:
    documents = []

    for repo_name in repo_names:
        repo_path = repo_root / repo_name
        if not repo_path.exists():
            continue

        for md_path in sorted(repo_path.glob("**/*.md")):
            content = md_path.read_text(encoding="utf-8", errors="replace")
            relative_path = str(md_path.relative_to(repo_path))
            title = extract_title(content, md_path.stem)
            documents.append(MarkdownDocument(repo_name, relative_path, title, content))

    return documents
