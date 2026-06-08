from __future__ import annotations

from content_analyzer import AnalysisResult


def generate_x_posts(analysis: AnalysisResult, config: dict) -> str:
    public_page = config["project"]["public_page"]
    license_name = config["project"]["license"]
    repo_names = " / ".join(analysis.repositories[:3]) if analysis.repositories else "関連リポジトリ"

    posts = [
        "Artificial Wisdom / 人工叡智を、AIの能力拡張ではなく、自然法則・摂理・調和・循環・構造に基づく知性設計として整理しています。過剰な断定ではなく、公開リポジトリを通じて検証可能な形で体系化していきます。",
        "人工叡智ガードレール・プロトコルは、単なる禁止リストではなく、知性が自然法則と調和から逸脱しないための構造的な枠組みとして位置づけています。公開前提の草案として、人間確認を重視します。",
        f"関連リポジトリを横断して、NOTE記事案やREADME案に変換するローカル補助ツールを整備中です。自動投稿は行わず、生成結果は必ず人間が確認します。対象: {repo_names}",
        f"Artificial Wisdom / 人工叡智の公開ページはこちらです。自然法則型人工叡智フレームワークとガードレールの入口として整理しています。{public_page}",
        f"ライセンス表記: {license_name}。人工叡智関連の文章案は、出典と文脈を確認した上で、過剰主張を避けて公開する方針です。",
    ]

    body = ["# X用短文投稿案", "", "> すべて投稿前に人間確認が必要です。自動投稿は禁止です。", ""]
    for index, post in enumerate(posts, start=1):
        body.append(f"## 案{index}")
        body.append("")
        body.append(post)
        body.append("")
    return "\n".join(body).rstrip() + "\n"

