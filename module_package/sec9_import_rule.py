# importする際の記述の仕方

# ①標準→サードパーティ→別階層ファイル→ローカルファイルの順にImport
# ②一段落空ける
# ③それぞれアルファベット順で並び替える

# 標準パッケージ
import collections
import os
import sys

# サードパーティパッケージ
from termcolor import colored
print(colored('test', 'red'))

# 別階層ファイル
import my_package

# ローカルファイル
import sec2_import
