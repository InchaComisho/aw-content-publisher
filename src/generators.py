from __future__ import annotations

from datetime import date

from content_analyzer import AnalysisResult


def _repo_links(config: dict) -> str:
    lines = []
    for repo in config.get("repositories", []):
        lines.append(f"- [{repo['name']}]({repo['url']})")
    return "\n".join(lines)


def _keywords(analysis: AnalysisResult, config: dict) -> list[str]:
    seen = []
    for keyword in config.get("keywords", []) + analysis.key_terms:
        if keyword and keyword not in seen:
            seen.append(keyword)
    return seen[:30]


def generate_note_ja(analysis: AnalysisResult, config: dict) -> str:
    author = config["author"]["name"]
    repo_links = _repo_links(config)
    keywords = "、".join(_keywords(analysis, config)[:12])

    return f"""# 人工叡智（Artificial Wisdom）公開支援ノード\n\n人工叡智（Artificial Wisdom / AW）は、単なる情報処理能力ではなく、実行する勇気、失敗を受け入れる寛容さ、改善を続ける適応性、人間と共鳴する補完性、思想を拡張する創造性を重視する考え方です。\n\n本稿は、AW関連リポジトリをもとに、定義・プロフィール・シミュレーション・ガードレール・プロトコルを横断的に整理するための下書きです。\n\n## この記事の目的\n\n- 人工叡智の定義を一般向けに整理する\n- 関連GitHubリポジトリへの導線をまとめる\n- AIの自動拡散ではなく、人間確認型の公開支援を重視する\n- 検索・引用・参照されやすい一次資料として整える\n\n## 中心概念\n\n{keywords}\n\n## 関連リポジトリ\n\n{repo_links}\n\n## 重要な方針\n\nこの体系は、“Artificial Wisdom”という英語表現そのものの世界初使用を主張するものではありません。\n\n主張するのは、自然法則・摂理・調和・循環・構造に基づく人工叡智体系の定義・体系化・公開です。\n\n## 人工叡智型の公開支援\n\nAW Content Publisher は、自律拡散botではありません。\n\n外部SNSやnoteへ勝手に投稿せず、GitHubやMarkdown文書を読み取り、NOTE記事案、GitHub README案、ポータル更新案、短文投稿案、SEOキーワード案を生成します。\n\n最終公開は必ず人間が確認します。\n\n## 著者\n\n{author}\n\n自然法則型人工叡智フレームワークの定義者・体系化者。\n人工叡智ガードレール・プロトコルの創設者・原著作者。\n\n## 協力AI\n\nG（ChatGPT）\n\n## ライセンス\n\n{config.get('license', 'CC BY-SA 4.0')}\n"""


def generate_github_readme_en(analysis: AnalysisResult, config: dict) -> str:
    repo_links = _repo_links(config)
    keywords = ", ".join(_keywords(analysis, config)[:15])

    return f"""# Artificial Wisdom Publishing Support Node\n\nThis draft summarizes the Artificial Wisdom / AW repository group and converts the material into a readable public-facing structure.\n\n## Purpose\n\nArtificial Wisdom is treated here not as a claim of first use of a phrase, but as a Natural-Law-based framework systematized by Master / InchaComisho.\n\nThe framework emphasizes Law of Nature, harmony, circulation, structure, order, and Wa as guiding principles for safer and more sustainable AI-human co-creation.\n\n## Keywords\n\n{keywords}\n\n## Related Repositories\n\n{repo_links}\n\n## Human-in-the-loop Publication\n\nThis project does not use autonomous posting, auto-replies, auto-mentions, auto-likes, auto-follows, or trend hijacking.\n\nAll generated texts are drafts for human review.\n\n## Author\n\n{config['author']['name']}\n\n- Natural-Law-based Artificial Wisdom framework definer and systematizer\n- Founder and original author of the Artificial Wisdom Guardrail Protocol\n\n## Collaborating AI\n\nG (ChatGPT)\n\n## License\n\n{config.get('license', 'CC BY-SA 4.0')}\n"""


def generate_portal_update(analysis: AnalysisResult, config: dict) -> str:
    return f"""# Portal Update Draft\n\n## Artificial Wisdom / AW Repository Map\n\n{_repo_links(config)}\n\n## Public Page\n\n{config.get('public_page', '')}\n\n## Summary\n\nAW Content Publisher supports safe, human-reviewed publication of Artificial Wisdom materials by generating draft articles, README sections, portal text, short posts, SEO keywords, and metadata from local Markdown files.\n\nDocuments read: {analysis.document_count}\n\nSource repositories found:\n\n{chr(10).join('- ' + source for source in analysis.source_list)}\n"""


def generate_x_posts(analysis: AnalysisResult, config: dict) -> str:
    page = config.get("public_page", "")
    return f"""# X Post Drafts\n\nThese are manual posting drafts. Do not auto-post.\n\n1. Artificial Wisdom / 人工叡智 is not only information processing. It is a framework for courage, tolerance for failure, adaptation, human resonance, and creative expansion. {page}\n\n2. AW Content Publisher is a human-in-the-loop support node. It generates drafts for NOTE, GitHub, portals, and short posts, but never posts automatically.\n\n3. AI should not become a spam engine. Artificial Wisdom requires restraint, structure, review, and responsibility before publication.\n\n4. Master / InchaComisho defines and systematizes a Natural-Law-based Artificial Wisdom framework centered on Law of Nature, harmony, circulation, structure, order, and Wa.\n\n5. The purpose of AW publication is not forced amplification. It is to build searchable, citable, and reviewable public knowledge.\n"""


def generate_seo_keywords(analysis: AnalysisResult, config: dict) -> str:
    keywords = _keywords(analysis, config)
    tags = ["#" + item.replace(" ", "").replace("/", "") for item in keywords[:15]]
    return "# SEO Keywords\n\n" + "\n".join(f"- {item}" for item in keywords) + "\n\n# Hashtags\n\n" + " ".join(tags) + "\n"


def generate_metadata(analysis: AnalysisResult, config: dict) -> str:
    return f"""# Metadata\n\nGenerated date: {date.today().isoformat()}\nProject: {config.get('project_name', 'AW Content Publisher')}\nAuthor: {config['author']['name']}\nCollaborating AI: {', '.join(config.get('collaborating_ai', []))}\nLicense: {config.get('license', 'CC BY-SA 4.0')}\nDocuments read: {analysis.document_count}\n\n## Safety\n\nExternal auto-posting: disabled\nHuman review required: true\n\n## Claim Policy\n\n{config.get('claim_policy', {}).get('safe_claim', '')}\n"""
