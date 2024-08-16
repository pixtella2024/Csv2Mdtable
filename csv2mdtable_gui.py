# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import csv2mdtable


class Csv2MdtableGuiClass:
    input_file_name: StringVar
    output_file_name: StringVar
    align_flag: StringVar

    def __init__(self) -> None:
        root = Tk()
        root.title("CSV → Markdown 変換ツール")
        root.resizable(False, False)
        frame_main = ttk.Frame(root, padding=(16))
        frame_main.pack()
        frame_setting = ttk.Frame(frame_main)
        frame_setting.pack()

        self.input_file_name = StringVar()
        self.output_file_name = StringVar()
        self.align_flag = StringVar()

        label_input_file = ttk.Label(frame_setting, text="入力ファイル", padding=(5, 2))
        label_input_file.grid(row=0, column=0, sticky=E)

        entry_input_file_name = ttk.Entry(
            frame_setting, textvariable=self.input_file_name, width=40, state="readonly"
        )
        entry_input_file_name.grid(row=0, column=1)

        button_input_file_dialog = ttk.Button(
            frame_setting, text="...", width=1, command=self.input_file_dialog
        )
        button_input_file_dialog.grid(row=0, column=2)

        label_output_file = ttk.Label(
            frame_setting, text="出力ファイル", padding=(5, 2)
        )
        label_output_file.grid(row=1, column=0, sticky=E)

        entry_output_file_name = ttk.Entry(
            frame_setting,
            textvariable=self.output_file_name,
            width=40,
            state="readonly",
        )
        entry_output_file_name.grid(row=1, column=1)

        button_output_file_dialog = ttk.Button(
            frame_setting, text="...", width=1, command=self.output_file_dialog
        )
        button_output_file_dialog.grid(row=1, column=2)

        label_check_align = ttk.Label(
            frame_setting, text="アライメント", padding=(5, 2)
        )
        label_check_align.grid(row=2, column=0, sticky=E)

        self.align_flag.set("1")
        check_align_flag = ttk.Checkbutton(frame_setting, variable=self.align_flag)
        check_align_flag.grid(row=2, column=1, sticky=W)

        frame_button = ttk.Frame(frame_main, padding=(0, 5))
        frame_button.pack(side=RIGHT)

        button_exec = ttk.Button(
            frame_button, text="実行", command=self.exec_csv2mdtable
        )
        button_exec.pack(side=LEFT)

        button_cancel = ttk.Button(frame_button, text="キャンセル", command=root.quit)
        button_cancel.pack(side=LEFT)

        root.mainloop()

    def exec_csv2mdtable(self):
        str_input_file_name = self.input_file_name.get()
        str_output_file_name = self.output_file_name.get()
        if str_input_file_name == "":
            messagebox.showerror("エラー", "入力ファイルが指定されていません")
            return
        if str_output_file_name == "":
            messagebox.showerror("エラー", "出力ファイルが指定されていません")
            return
        align_flag = self.align_flag.get() == "1"
        ret = csv2mdtable.Csv2Mdtable(
            str_input_file_name, str_output_file_name, align_flag
        )
        if ret:
            messagebox.showinfo("完了", "出力に成功しました")
        else:
            messagebox.showerror("エラー", "出力に失敗しました")

    def input_file_dialog(self):
        file_type = [("CSVファイル", "*.csv")]
        curr_file = self.input_file_name.get()
        file_name: str
        if os.path.isfile(curr_file):
            init_dir = os.path.abspath(os.path.dirname(curr_file))
            init_file = os.path.basename(curr_file)
            file_name = filedialog.askopenfilename(
                filetypes=file_type, initialdir=init_dir, initialfile=init_file
            )
        else:
            init_dir = os.path.abspath(os.path.dirname(__file__))
            file_name = filedialog.askopenfilename(
                filetypes=file_type, initialdir=init_dir
            )
        if len(file_name) != 0:
            self.input_file_name.set(file_name)

    def output_file_dialog(self):
        file_type = [("Markdownファイル", "*.md"), ("テキストファイル", "*.txt")]
        curr_file = self.output_file_name.get()
        file_name: str
        if os.path.isfile(curr_file):
            init_dir = os.path.abspath(os.path.dirname(curr_file))
            init_file = os.path.basename(curr_file)
            file_name = filedialog.asksaveasfilename(
                filetypes=file_type,
                initialdir=init_dir,
                initialfile=init_file,
                defaultextension="md",
            )
        else:
            init_dir = os.path.abspath(os.path.dirname(__file__))
            file_name = filedialog.asksaveasfilename(
                filetypes=file_type,
                initialdir=init_dir,
                defaultextension="md",
            )
        if len(file_name) != 0:
            self.output_file_name.set(file_name)


if __name__ == "__main__":
    Csv2MdtableGuiClass()
