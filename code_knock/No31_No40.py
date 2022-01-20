# 31.内包表記
from mimetypes import init
from this import d


nums = []
for i in range(5):
    nums.append(i * 2)
print(nums)
# [0, 2, 4, 6, 8]

nums = [2 * i for i in range(5)]
print(nums)
# [0, 2, 4, 6, 8]


# 32.0で割った時の例外処理
num = 0
try:
    print(f'計算結果{10 / num}')
except:
    print('エラー')
# エラー


# 33.具体的なエラー内容の出力
num = 0
try:
    print(f'計算結果{10 / num}')
except ZeroDivisionError as e:
    print(e)
# division by zero


# 34.エラー内容ごとの例外処理
def divide(a, b):
    try:
        print(f'計算結果{a / b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
divide(10, 'zero')
# unsupported operand type(s) for /: 'int' and 'str'


# 35.通常週旅次に行う処理
def divide(a, b):
    try:
        print(f'計算結果{a / b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        print('正常に終了しました。')
divide(10, 2)
# 計算結果5.0
# 正常に終了しました。


# 36.例外も含めた終了時に行う処理
def divide(a, b):
    try:
        print(f'計算結果{a / b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    finally:
        print('全ての処理が終了しました。')
divide(10, 2)
# 計算結果5.0
# 全ての処理が終了しました。


# 37.例外も含めた終了時に行う処理
def divide(a, b):
    try:
        print(f'計算結果{a / b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        pass
    finally:
        print('全ての処理が終了しました。')
divide(10, 'zero')
# 全ての処理が終了しました。


# 38.classの基礎
class Person:
    nationality = 'japan'

    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.nationality}です。')

person = Person()
print(person.nationality)
# japan
person.say_hello()
# こんにちは、私の国籍はjapanです。


# 39.コンストラクタの設定
class Person:
    nationality = 'japan'

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.nationality}です。')

    def say_my_name(self):
        print(f'私の名前は{self.name}です。')

person = Person('宜志')
person.say_my_name()
# 私の名前は宜志です。


# 40.クラスの継承
class Kid(Person):
    def say_hello(self, age):
        print(f'私の名前は{self.name}です。年齢は{age}才です。')

kid = Kid('宜志')
kid.say_hello(22)
# 私の名前は宜志です。年齢は22才です。
