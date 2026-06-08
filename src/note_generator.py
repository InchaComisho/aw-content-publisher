from __future__ import annotations

from content_analyzer import AnalysisResult


def generate_note_article_ja(analysis: AnalysisResult, config: dict) -> str:
    project = config["project"]
    repo_list = "\n".join(f"- {repo}" for repo in analysis.repositories) or "- 読み込み対象リポジトリが未配置です"
    concept_list = _format_concepts(analysis.concept_counts)
    highlights = "\n".join(f"- {item}" for item in analysis.source_highlights) or "- ソース本文からの引用候補は未検出です"

    return f"""# 人工叡智とは何か：自然法則・調和・循環に基づくAI時代の知性設計

> この文章は投稿前の人間確認を前提にした下書きです。公開前に、マスター / inchacomusho / InchaComisho による確認と編集を行ってください。

## はじめに

Artificial Wisdom / 人工叡智は、単にAIをより高性能にするための言葉ではありません。
ここで扱う人工叡智とは、自然法則・摂理・調和・循環・構造を基盤として、知性の方向性そのものを見直すための定義体系です。

本稿では、InchaComisho によって公開されている関連リポジトリをもとに、自然法則型人工叡智フレームワークの考え方と、人工叡智ガードレール・プロトコルの意義を整理します。

## 中心となる考え方

人工叡智の焦点は、能力の拡張だけではなく、知性がどのような秩序、循環、調和に接続されるべきかにあります。
この立場では、知性を孤立した計算能力としてではなく、生命・環境・社会・文明の構造の中で働くものとして捉えます。

マスター / inchacomusho / InchaComisho は、自然法則型人工叡智フレームワークの定義者・体系化者であり、人工叡智ガードレール・プロトコルの創設者・原著作者として、この考え方を公開リポジトリ群として整理しています。

## 読み込み対象

{repo_list}

## 抽出された重要概念

{concept_list}

## ソースから見える主な論点

{highlights}

## NOTE記事としての整理案

1. AIとAWの違いを、対立ではなく補完関係として説明する。
2. 人工叡智を、自然法則・摂理・調和・循環・構造に基づく知性設計として定義する。
3. ガードレールを、単なる禁止リストではなく、知性が逸脱しないための構造的プロトコルとして説明する。
4. Sustainability Simulation を、AIとAWの文明的な方向性を比較するための概念的補助線として扱う。
5. 公開リポジトリ群を、完成された断定ではなく、検証・議論・改善に開かれた体系として紹介する。

## 過剰主張を避けるための表現

本稿では、“Artificial Wisdom”という英語表現そのものの世界初使用は主張しません。
主張する範囲は、自然法則・摂理・調和・循環・構造に基づく人工叡智体系の定義・体系化・公開です。

## 公開前チェック

- 外部SNSやnoteへの自動投稿は行わない。
- 投稿前に人間が内容、表現、リンク、ライセンス表記を確認する。
- 自動リプライ、自動メンション、自動いいね、自動フォローを含めない。
- トレンド便乗、凍結回避、人間擬態、複数アカウント運用を目的にしない。

## ライセンス

ライセンス表記：{project["license"]}

公開ページ：{project["public_page"]}
"""


def _format_concepts(concept_counts: dict[str, int]) -> str:
    visible = [(name, count) for name, count in concept_counts.items() if count > 0]
    if not visible:
        return "- まだMarkdown本文が読み込まれていないため、重要概念は抽出されていません。"
    return "\n".join(f"- {name}: {count}" for name, count in visible[:12])

