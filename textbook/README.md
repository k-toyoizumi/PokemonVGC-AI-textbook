# ポケモン対戦AIを研究する

第1〜7章を収録した複数ページHTML教科書。左側に階層型ナビゲーション、右側にページ内目次、数式はMathMLで表示します。

- 閲覧URL：https://k-toyoizumi.github.io/PokemonVGC-AI-textbook/
- `source/`：編集用Quartoソース。本文の正本。
- `index.html`、`chapters/`：公開用HTML。
- `scripts/render_preview.py`：現行のオフラインHTML生成器。

## 更新

1. `source/` の章別qmdを編集する。
2. PandocとPythonのbeautifulsoup4を導入し、リポジトリのルートで `python textbook/scripts/render_preview.py` を実行する。
3. 本文・数式・リンク・表を確認し、ソースとHTMLを一緒にcommitしてmainへpushする。
4. GitHub ActionsがHTMLをPagesへ配信する。初回のみSettings → Pages → SourceをGitHub Actionsにする。

現行HTMLはPandocによるプレビューで、Quarto正式ビルドではありません。Quartoへ移行する場合は `quarto render textbook/source` で生成し、公開先を揃えて検証してください。

## 編集方針

ポケモンAI全般を俯瞰し、研究結果を批判的に読めることを目標とする。一般数学の復習は省き、ゲーム理論・強化学習の基礎を厚くする。数式→直感・具体例→論文で説明し、コード・疑似コードは原則不要。1レッスン45〜60分を目安に、概要は簡潔に、理解の分かれ目は詳しく説明する。


## 検証

`python textbook/scripts/validate.py` でHTML・内部参照を検査し、`python textbook/scripts/test_numeric.py` で教材の数値例を確認できます。詳細は `textbook/QA.md`。前者はBeautiful Soup、後者はNumPyとSciPyを使用します（コマンドはリポジトリのルートで実行）。
