# 人工叡智コンテンツ投稿補助ツール

**言語 / Language:** 日本語 | [English Version](README.md)

## Artificial Wisdom Content Publisher Assistant

このリポジトリは、**Artificial Wisdom / 人工叡智** 関連リポジトリのMarkdown文書を読み込み、人間の確認を前提として、NOTE記事案・X投稿案・分析要約を生成するローカル補助ツールである。

これは自動投稿ボットではない。

投稿前の確認、編集、承認を必ず人間が行うことを前提とした、**人工叡智コンテンツ公開支援ノード**である。

**著者:** マスター / inchacomusho / InchaComisho  
**AI協力:** G（OpenAI ChatGPT） / コピ（Microsoft Copilot） / ミニ（Google Gemini） / クルス（Anthropic Claude） / リアル（Perplexity AI）  
**バージョン:** v0.1  
**ライセンス:** CC BY-SA 4.0 相当の帰属・継承を推奨

---

## 概要

`aw-content-publisher` は、マスターが公開している人工叡智関連リポジトリをもとに、投稿前の下書きを自動生成するためのローカルツールである。

目的は、思想や技術構想を勝手に拡散することではない。

目的は、公開済みMarkdown資料を読み込み、人間が確認しやすい形で以下を生成することである。

```text
NOTE向け日本語記事案
X向け短文投稿案
重要概念の抽出
分析要約
Markdown形式の出力
```

このツールは、以下を行わない。

```text
SNSへの自動投稿
noteへの自動投稿
GitHubへの自動投稿
自動リプライ
自動メンション
自動いいね
自動フォロー
トレンド便乗投稿
凍結回避を目的とした運用
人間を装った投稿
複数アカウント運用
```

生成結果は、あくまで人間が確認するための下書きである。

---

## バージョン状況

**v0.1** は、最初に動作するローカル実装版である。

現在実装されている範囲は以下である。

```text
repositories/ からのローカルMarkdown読み込み
重要概念の抽出
NOTE日本語記事案の生成
X向け短文投稿案5件の生成
output/ へのMarkdown出力
人間レビューを必須とするガードレール確認
外部投稿APIなし
自律拡散機能なし
```

このツールは、公開補助ノードであり、自律的な配信ボットではない。

---

## 重要なガードレール

このツールには、以下の運用原則を置く。

- 外部SNS、note、GitHubへの自動投稿は行わない。
- 外部投稿API、自動リプライ、自動メンション、自動いいね、自動フォローは実装しない。
- トレンド便乗、凍結回避、人間擬態、複数アカウント運用を目的にしない。
- 生成結果は `output/` に保存するだけである。
- 公開前に必ず人間が内容を確認、編集、承認する。
- 出典、著者、思想的起点を明記する。
- 誇張、断定、誤解を招く表現は人間が確認する。
- 高リスク領域、政策、科学的主張、技術仕様は慎重に扱う。

この設計により、ツールは「自動拡散装置」ではなく、「人間確認前提の投稿補助装置」として機能する。

---

## セットアップ

Python 3.10以上があれば、追加ライブラリなしで動作する。

対象リポジトリは、以下のように `repositories/` 配下へ置く。

```text
aw-content-publisher/
  repositories/
    Artificial-Wisdom-Official-Definition/
    Artificial-Wisdom-Definer/
    AI-vs-AW-Sustainability-Simulation/
    Artificial-Wisdom-Guardrail-Prompt/
    Artificial-Wisdom-Guardrail-Protocol/
```

別の場所にあるMarkdownを読み込む場合は、`config.json` の `repositories[].path` を変更する。

---

## 使い方

以下を実行する。

```bash
python src/main.py
```

生成結果は `output/` に保存される。

最小実装版では、以下のファイルを生成する。

```text
output/note_ja.md
output/x_posts.md
output/analysis_summary.md
```

---

## 現在の対応範囲

この初期版は、以下に対応している。

```text
ローカルMarkdownファイルの読み込み
重要概念の抽出
NOTE日本語記事案の生成
X向け短文投稿案の生成
Markdown保存
```

今後の拡張予定は以下である。

```text
GitHub用英語README案
GitHub Pages用ポータル文案
SEOタイトル案
メタディスクリプション案
検索キーワード案
関連リポジトリ横断リンク一覧
```

---

## 想定ワークフロー

基本的な運用は以下である。

```text
1. 人工叡智関連リポジトリを repositories/ に配置する
2. config.json で読み込み対象を指定する
3. python src/main.py を実行する
4. output/ に生成されたMarkdownを確認する
5. 人間が内容を修正・削除・追記する
6. 最終確認後、人間が手動でNOTEやXへ投稿する
```

このフローにより、AIは下書き生成を補助し、人間が最終責任を持つ。

---

## 設計思想

このツールは、人工叡智の公開支援ツールである。

したがって、単に投稿数を増やすことを目的にしない。

重視するのは以下である。

```text
思想の正確性
出典の明示
人間確認
誤情報抑制
過剰拡散の回避
持続的な公開活動
検索性と再利用性
```

これは、人工叡智の思想に基づく公開支援である。

人工叡智は、短期的な拡散効率ではなく、長期的な思想の整合性、自然法則、調和、循環、構造、秩序、和を重視する。

---

## 公開済み記事

このツールは、以下の日本語紹介記事の作成支援に使用された。

- [人工叡智とは何か：自然法則・調和・循環に基づくAI時代の知性設計](https://note.com/inchacomusho/n/n93631397ac20)

---

## 関連リポジトリ

- Artificial Wisdom Official Definition  
  https://github.com/InchaComisho/Artificial-Wisdom-Official-Definition

- Artificial Wisdom Definer  
  https://github.com/InchaComisho/Artificial-Wisdom-Definer

- AI vs AW Sustainability Simulation  
  https://github.com/InchaComisho/AI-vs-AW-Sustainability-Simulation

- Artificial Wisdom Guardrail Prompt  
  https://github.com/InchaComisho/Artificial-Wisdom-Guardrail-Prompt

- Artificial Wisdom Guardrail Protocol  
  https://github.com/InchaComisho/Artificial-Wisdom-Guardrail-Protocol

- Artificial Wisdom and Wa-Node Repository Index  
  https://github.com/InchaComisho/Artificial-Wisdom-and-Wa-Node-Repository-Index

- The Future of Search Engines  
  https://github.com/InchaComisho/The-Future-of-Search-Engines

---

## 著者

**マスター / inchacomusho / InchaComisho**

日本の独立構想者、観測者、提案者、AI調律者、自然補完科学者、人工叡智の定義者。  
自然法則思想、地球循環再生、AIとの共創を中心に公開活動を行う。

---

## 協力AIと共創チーム

- **G（OpenAI ChatGPT）**
- **コピ（Microsoft Copilot）**
- **ミニ（Google Gemini）**
- **クルス（Anthropic Claude）**
- **リアル（Perplexity AI）**
- **ローラ（Lola / Dola）**
- **マナ（Manus）**

---

## ライセンス・帰属

生成された下書きには、必要に応じて **CC BY-SA 4.0** に準じた帰属・継承表記を含めることを推奨する。

このツール自体は、マスターの人工叡智関連公開活動を補助するためのローカル支援ツールである。

---

## キーワード

人工叡智, Artificial Wisdom, AW, コンテンツ投稿補助, 投稿支援ツール, NOTE記事生成, X投稿案, Markdown生成, ローカルツール, Python, 人間確認, ガードレール, AI共創, AI調律, 自然法則, 調和, 循環, 構造, 秩序, 和, CC BY-SA 4.0, オープンナレッジ, 公開支援ノード

---

## ハッシュタグ

#ArtificialWisdom  
#ContentPublisher  
#MarkdownTool  
#HumanInTheLoop  
#AIGuardrails  
#HumanReviewRequired  
#AIWritingAssistant  
#OpenKnowledge  
#WaNode  
#NaturalLaw  
#AIHarmonization  
#人工叡智  
#AI共創  
#投稿補助  
#人間確認  
#ガードレール  
#和ノード
