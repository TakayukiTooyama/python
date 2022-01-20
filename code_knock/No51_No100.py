# 51.ファイルの存在確認
import os
print(os.path.isfile('code_knock/No41_No50.py'))
# True


# 52.パス名の結合
for curDir, dir, files in os.walk('code_knock'):
    for file in files:
        print(os.path.join(curDir, file))
# code_knock/No1_No10.py
# code_knock/No11_No20.py
# code_knock/No41_No50.py
# code_knock/No51_No60.py
# code_knock/No31_No40.py
# code_knock/No21_No30.py


# 53.ディレクトリの作成
# os.mkdir('test_dir')


# 54.ファイルの削除
# os.remove('sample.txt')


# 55.ディレクトリ名の変更
# os.rename('test_dir', 'test_dir2')


# 56.環境変数の確認
# print(os.environ['PATH'])


# 57.Unixコマンド
import subprocess
subprocess.run(['ls'])


# 93.現在の日時取得
import datetime

now = datetime.datetime.now()
print(now)
# 2022-01-20 19:37:26.634857

today = datetime.date.today()
print(today)
# 2022-01-20


# 94.任意の日付を取得
day = datetime.date(2021, 1, 1)
print(day)
# 2021-01-01


# 95.日付内の各情報
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.strftime('%A'))
# 2022
# 1
# 20
# 19
# 46
# 30
# Thursday


# 96.日付計算
# 一昨日
today = datetime.date.today()
print(today - datetime.timedelta(days=2))
# 2022-01-18


# 97.日付比較
print(datetime.date(2020, 1, 1) < datetime.date(2021, 1, 1))
# True


# 98.フォーマット変換
print(today.strftime('%Y/%m/%d'))


# 99.APIを叩く
import requests
url = 'https://jsonplaceholder.typicode.com/posts/1'

res = requests.get(url)
print(res.json())
