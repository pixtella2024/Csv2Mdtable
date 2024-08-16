# Csv2Mdtable
CSV を Markdown のテーブルに変換するサンプルプログラム

## CUI

CUI での実行コマンドは下記の通り

```sh
python3 csv2mdtable.py --alignment input_file_name output_file_name
```

- 引数
    * input_file_name
        - 入力ファイル名(CSV)
    * output_file_name
        - 出力ファイル名
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

`TestData` ディレクトリにテスト用の入力データファイル `input.csv` と CUI で下記のとおりに実行して得た出力データファイル `output.md` を同封している。

```sh
python3 csv2mdtable.py --alignment TestData/input.csv TestData/output.md 
```
