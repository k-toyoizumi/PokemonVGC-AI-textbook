# 検証記録（2026-10-24）

- PASS：5ページ生成、7表の見出し・本文の列数と揃え指定、500件の内部リンク。
- PASS：ページヘッダーをsite-headerへ分離し、表のtr.headerにflex・sticky等が適用されるCSS衝突を除去。
- PASS：Wilson区間の3数値例を再計算（8/10：0.4902〜0.9433、80/100：0.7112〜0.8666、800/1000：0.7741〜0.8236）。
- PASS：第1〜4章の略称・添字・主要演算子の説明を点検・補足。VGC-Benchの比較手法の正式名は公式READMEで照合。
- NOT RUN：ブラウザ実表示検証。Playwright用Chromiumのダウンロードが破損アーカイブで失敗。列の実測位置は未確認。
- NOT RUN：Quarto正式ビルド。現行HTMLはPandocによる複数ページプレビュー。

## 第5〜7章の追加

- PASS：8ページのPandoc HTML生成。数式変換警告なし、MathMLへ変換できない式なし。
- PASS：12表・3図、章をまたぐ図表参照・内部リンク・章一覧・前後章リンクの静的検査。
- PASS：ベイズ更新、結合行動数、固定相手の期待値、木の探索スコア、隠れた状態の過大評価の数値検算。混合戦略はSciPyの線形計画で別途解き、自分1/2・相手2/3・値0との一致を確認。
- PASS：新規SVG3枚をMuPDFで画像化して目視確認。SVGの表示属性を明示して、描画器のCSS対応差を減らした。ブラウザ全体の検証の代用とはしない。
- NOT RUN：デスクトップ／390pxでのHTMLブラウザ操作・表示確認。検証用Chromiumの取得失敗という既存の制限が残る。
- NOT RUN：Quarto正式ビルド（CLI未導入）。

再実行：`python textbook/scripts/render_preview.py`、`python textbook/scripts/validate.py`、`python textbook/scripts/test_numeric.py`。数値検証にはNumPyとSciPy、HTML検証にはBeautiful Soup、生成にはPandocが必要。


## 2026-10-25：表6.1と第8〜9章

- PASS：表6.1の行・列の主体を明記。対象の表だけ全幅・固定最小幅を解除するCSSを生成器へ追加。
- PASS：10ページ、14表、5図、2050件の内部リンク、MathMLの静的検査。
- PASS：行動模倣損失、50回の連続一致、価値、時間差分、一般化アドバンテージ推定、クリッピングの正負の数値例。
- PASS：PandocのHTML再生成。
- NOT RUN：ブラウザ実表示・操作、390pxの実測列幅。
- NOT RUN：Quarto正式ビルド。現行公開はPandocプレビュー。

Skill向け改善提案：docs/2026-10-25_1.md。第8〜9章は模式図2枚・表2点・解説付き9問を追加した。
