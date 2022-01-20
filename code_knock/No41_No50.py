# 41.privateとpublic
# 外部から呼び出せないがクラス内からはアクセスはできる
class Person:
    __nationality = 'japan'

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.__nationality}です。')

    def __say_my_name(self):
        print(f'私の名前は{self.name}です。')

person = Person('宜志')
# print(person.__nationality)
# person.say_my_name()
person.say_hello()


# 42.ファイル操作の基本
f = open('sample.txt')
print(f.read())
f.close()


# 43.with構文
with open('sample.txt', 'r') as f:
    print(f.read())


# 44.jsonモジュール
# import json
# with open('sample.json', 'r') as f:
#     data = json.load(f)
#     print(data)
#     print(data['store_name'])


# 45.全ファイルの情報取得
import os
# for curDir, dirs, files in os.walk('.'):
#     for file in files:
#         print(f'{curDir}/{file}')


# 46.ファイル情報の取得
file_list = os.listdir('code_knock')
print(file_list)


# 47.絶対パスを含んだファイル名の取得
path = './No41_No50.py'
print(os.path.abspath(path))
# /Users/takayuki/Documents/larning-guide/python/No41_No50.py


# 48.ファイル名の取得
print(os.path.basename(path))
# No41_No50.py


# 49.ファイル・ディレクトリの存在確認
dir = 'code_knock'
print(os.path.exists(dir))
# True
print(os.path.exists('aaa'))
# False

# 50.ディレクトリの存在確認
print(os.path.isdir(dir))
# True
