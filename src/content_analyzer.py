from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass

from repo_reader import MarkdownDocument


KEY_CONCEPTS = [
    "Artificial Wisdom",
    "人工叡智",
    "自然法則",
    "摂理",
    "調和",
    "循環",
    "構造",
    "Natural Law",
    "harmony",
    "cycle",
    "circulation",
    "structure",
    "guardrail",
    "protocol",
    "sustainability",
    "持続可能性",
]


@dataclass(frozen=True)
class AnalysisResult:
    document_count: int
    repositories: list[str]
    concept_counts: dict[str, int]
    headings_by_repo: dict[str, list[str]]
    source_highlights: list[str]


def analyze_documents(documents: list[MarkdownDocument]) -> AnalysisResult:
    concept_counter: Counter[str] = Counter()
    headings_by_repo: dict[str, list[str]] = defaultdict(list)
    source_highlights: list[str] = []

    for doc in documents:
        lowered = doc.text.lower()
        for concept in KEY_CONCEPTS:
            concept_counter[concept] += lowered.count(concept.lower())

        headings = _extract_headings(doc.text)
        headings_by_repo[doc.repo_name].extend(headings[:8])

        highlight = _find_highlight_sentence(doc.text)
        if highlight:
            source_highlights.append(f"{doc.repo_name}: {highlight}")

    return AnalysisResult(
        document_count=len(documents),
        repositories=sorted({doc.repo_name for doc in documents}),
        concept_counts=dict(concept_counter.most_common()),
        headings_by_repo={key: values[:12] for key, values in headings_by_repo.items()},
        source_highlights=source_highlights[:10],
    )


def _extract_headings(text: str) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,4})\s+(.+)$", line.strip())
        if match:
            headings.append(match.group(2).strip())
    return headings


def _find_highlight_sentence(text: str) -> str:
    normalized = re.sub(r"\s+", " ", text)
    sentences = re.split(r"(?<=[。.!?])\s+", normalized)
    for sentence in sentences:
        if 40 <= len(sentence) <= 220 and any(term in sentence for term in KEY_CONCEPTS[:8]):
            return sentence.strip()
    return ""

