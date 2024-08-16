# -*- coding: utf-8 -*-

import argparse
import os
import csv
import unicodedata

DEFAULT_ALIGN = 0
LEFT_ALIGN = 1
CENTER_ALIGN = 2
RIGHT_ALIGN = 3


def get_east_asian_width_count(text: str) -> int:
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in "FWA":
            count += 2
        else:
            count += 1
    return count


def calc_space_count(text_len: int, len_max: int, align: int):
    left_space = 0
    right_space = 0
    total_space = len_max - text_len

    if align == RIGHT_ALIGN:
        left_space = total_space
    elif align == CENTER_ALIGN:
        left_space = total_space // 2
        right_space = total_space - left_space
    else:  # (align==LEFT_ALIGN) or (align==DEFAULT_ALIGN)
        right_space = total_space

    return left_space, right_space


def Csv2Mdtable(input_file_name: str, output_file_name: str, align_flag: bool) -> bool:
    # 入力ファイルの存在チェック
    if not os.path.exists(input_file_name):
        print("指定された入力ファイルが存在しません")
        return False

    mdtable_list = []
    with open(input_file_name) as input_f:
        input_reader = csv.reader(input_f)

        # 1行目のデータを取得
        row = next(input_reader)

        # カラム数を取得
        col_cnt = len(row)

        # アライメントの設定を取得
        align_list = []
        if align_flag:
            for align_setting in row:
                align_setting = align_setting.upper()
                if align_setting == "L":
                    align_list.append(LEFT_ALIGN)
                elif align_setting == "C":
                    align_list.append(CENTER_ALIGN)
                elif align_setting == "R":
                    align_list.append(RIGHT_ALIGN)
                else:
                    align_list.append(DEFAULT_ALIGN)
        else:
            align_list = [DEFAULT_ALIGN] * col_cnt
            input_f.seek(0)

        # 文字列長を取得
        len_list = []
        len_max_list = [1] * col_cnt
        for row in input_reader:
            len_row = []
            for i in range(col_cnt):
                if i < len(row):
                    val_cnt = get_east_asian_width_count(row[i].strip())
                    len_row.append(val_cnt)
                    if len_max_list[i] < val_cnt:
                        len_max_list[i] = val_cnt
                else:
                    len_row.append(0)
            len_list.append(len_row)

        # Markdown に変換
        mdtable_row = "|"
        input_f.seek(0)
        if align_flag:
            next(input_reader)  # 1行目を読み飛ばす
        row = next(input_reader)
        for i in range(col_cnt):
            mdtable_row += " "
            left_space, right_space = calc_space_count(
                len_list[0][i], len_max_list[i], align_list[i]
            )
            for j in range(left_space):
                mdtable_row += " "
            mdtable_row += row[i].strip()
            for j in range(right_space):
                mdtable_row += " "
            mdtable_row += " |"
        mdtable_list.append(mdtable_row)
        print(mdtable_row)

        mdtable_row = "|"
        for i in range(col_cnt):
            if (align_list[i] == LEFT_ALIGN) or (align_list[i] == CENTER_ALIGN):
                mdtable_row += ":"
            else:
                mdtable_row += "-"
            for j in range(len_max_list[i]):
                mdtable_row += "-"
            if (align_list[i] == RIGHT_ALIGN) or (align_list[i] == CENTER_ALIGN):
                mdtable_row += ":"
            else:
                mdtable_row += "-"
            mdtable_row += "|"
        mdtable_list.append(mdtable_row)
        print(mdtable_row)

        len_list_idx = 1
        for row in input_reader:
            mdtable_row = "|"
            for i in range(col_cnt):
                mdtable_row += " "
                if i < len(row):
                    left_space, right_space = calc_space_count(
                        len_list[len_list_idx][i], len_max_list[i], align_list[i]
                    )
                    for j in range(left_space):
                        mdtable_row += " "
                    mdtable_row += row[i].strip()
                    for j in range(right_space):
                        mdtable_row += " "
                else:
                    for j in range(len_max_list[i]):
                        mdtable_row += " "
                mdtable_row += " |"
            mdtable_list.append(mdtable_row)
            print(mdtable_row)
            len_list_idx += 1
        print("")

    with open(output_file_name, mode="w") as output_f:
        output_f.write("\n".join(mdtable_list))

    return True


def main():
    parser = argparse.ArgumentParser(description="CSV を Markdown の表に変換する")

    parser.add_argument("input_file_name", type=str, help="入力ファイル名(CSV)")
    parser.add_argument("output_file_name", type=str, help="出力ファイル名")
    parser.add_argument(
        "--alignment",
        action="store_true",
        help="1行目を 左寄せ(L)/中央寄せ(C)/右寄せ(R) の判定に使用する",
    )

    args = parser.parse_args()

    input_file_name = args.input_file_name
    output_file_name = args.output_file_name
    align_flag = args.alignment

    Csv2Mdtable(input_file_name, output_file_name, align_flag)


if __name__ == "__main__":
    main()
