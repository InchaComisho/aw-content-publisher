# Artificial Wisdom Content Publisher Assistant

InchaComisho / inchacomusho の Artificial Wisdom / 人工叡智 関連リポジトリを読み込み、投稿前の人間確認を前提とした Markdown 投稿案を生成するローカル補助ツールです。

## Important Guardrails

- 外部SNS、note、GitHub への自動投稿は行いません。
- 外部投稿API、自動リプライ、自動メンション、自動いいね、自動フォローは実装しません。
- トレンド便乗投稿、凍結回避、人間擬態、複数アカウント運用を目的にしません。
- 生成結果は `output/` に保存するだけです。
- 公開前に必ず人間が内容を確認、編集、承認してください。

## Setup

Python 3.10 以上があれば追加ライブラリなしで動きます。

対象リポジトリは次のように `repositories/` 配下へ置いてください。

```text
aw-content-publisher/
  repositories/
    Artificial-Wisdom-Official-Definition/
    Artificial-Wisdom-Definer/
    AI-vs-AW-Sustainability-Simulation/
    Artificial-Wisdom-Guardrail-Prompt/
    Artificial-Wisdom-Guardrail-Protocol/
```

`config.json` の `repositories[].path` を変更すれば、別の場所にある Markdown も読み込めます。

## Usage

```bash
python src/main.py
```

生成結果は `output/` に保存されます。

最小実装版では次を生成します。

- `output/note_ja.md`
- `output/x_posts.md`
- `output/analysis_summary.md`

## Current Scope

この初期版は、ローカル Markdown ファイルの読み込み、重要概念の抽出、NOTE日本語記事案、X用短文投稿案、Markdown保存に対応しています。

今後の拡張予定:

- GitHub用英語README案
- GitHub Pages用ポータル文案
- SEOタイトル案
- メタディスクリプション案
- 検索キーワード案
- 関連リポジトリ横断リンク一覧

## Published Article

This tool was used to support the creation of the following Japanese introductory article:

- [人工叡智とは何か：自然法則・調和・循環に基づくAI時代の知性設計](https://note.com/inchacomusho/n/n93631397ac20)

## License Notice

Generated drafts should include attribution under CC BY-SA 4.0 where appropriate.

