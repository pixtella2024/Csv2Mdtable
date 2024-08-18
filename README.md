# Csv2Mdtable
CSV を Markdown のテーブルに変換するサンプルプログラム

## CUI

CUI での実行コマンドは下記の通り

```sh
python3 csv2mdtable.py --alignment input_file_name output_file_name encoding
```

- 引数
    * input_file_name
        - 入力ファイル名(CSV)
    * output_file_name
        - 出力ファイル名
    * encoding
        - ファイルの文字コード
            * 0: UTF-8
            * 1: Shift_JIS
- オプション
    * -h, --help
        - ヘルプ
    * --alignment
        - 1行目を 左寄せ(L)/中央寄せ(C)/右寄せ(R) の判定に使用する
        - このオプションがついてないとき、1行目はタイトルとして扱う

## GUI

GUI での実行コマンドは下記の通り

```sh
python3 csv2mdtable_gui.py
```

## テストデータ

`TestData` ディレクトリにテスト用の入力データファイルと実行結果のファイルを同封している。

- UTF-8
    * 入力: input_utf8.csv
    * 結果: output_utf8.md
    * 実行コマンド: `python3 csv2mdtable.py --alignment TestData/input_utf8.csv TestData/output_utf8.md 0`
- Shift_JIS
    * 入力: input_sjis.csv
    * 結果: output_sjis.md
    * 実行コマンド: `python3 csv2mdtable.py --alignment TestData/input_sjis.csv TestData/output_sjis.md 1`
