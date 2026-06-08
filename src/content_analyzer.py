from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

from repo_reader import MarkdownDocument


@dataclass
class AnalysisResult:
    document_count: int
    source_list: list[str]
    titles: list[str]
    key_terms: list[str]
    excerpts: list[str]


STOP_WORDS = {
    "the", "and", "for", "with", "that", "this", "from", "are", "was", "were", "have",
    "has", "not", "but", "you", "your", "our", "into", "about", "will", "can",
    "人工叡智", "する", "こと", "ため", "これ", "それ", "この", "その", "ます", "です"
}


IMPORTANT_TERMS = [
    "Artificial Wisdom",
    "人工叡智",
    "Natural Law",
    "Law of Nature",
    "摂理",
    "調和",
    "循環",
    "構造",
    "秩序",
    "和",
    "guardrail",
    "protocol",
    "sustainability",
    "AI alignment",
]


def _clean_excerpt(text: str, max_length: int = 220) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("|"):
            continue
        lines.append(stripped)
        if len(" ".join(lines)) >= max_length:
            break
    joined = " ".join(lines)
    return joined[:max_length].rstrip()


def analyze_documents(documents: list[MarkdownDocument]) -> AnalysisResult:
    combined = "\n".join(doc.content for doc in documents)
    words = re.findall(r"[A-Za-z][A-Za-z\-]{3,}|[一-龥ぁ-んァ-ン]{2,}", combined)
    counter = Counter(word for word in words if word.lower() not in STOP_WORDS)

    ranked_terms = []
    for term in IMPORTANT_TERMS:
        if term.lower() in combined.lower():
            ranked_terms.append(term)

    for term, _count in counter.most_common(30):
        if term not in ranked_terms:
            ranked_terms.append(term)
        if len(ranked_terms) >= 20:
            break

    source_list = sorted({doc.repo_name for doc in documents})
    titles = [doc.title for doc in documents[:30]]
    excerpts = [_clean_excerpt(doc.content) for doc in documents[:10]]

    return AnalysisResult(
        document_count=len(documents),
        source_list=source_list,
        titles=titles,
        key_terms=ranked_terms,
        excerpts=excerpts,
    )
