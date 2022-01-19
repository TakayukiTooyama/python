# クラス定義（インスタンス化, 初期化, メソッド, デストラクタ）

# クラス
class Person:

    # 初期化（コンストラクタ）
    # インスタンスが作られた時一番最初に呼ばれる
    def __init__(self, name, age, nationality) -> None:
        self.name = name
        self.age = age
        self.nationality = nationality

    # メソッド
    def say_something(self, name):
        print(f'I am {self.name}. hello, {name}')
        # クラス内で定義したメソッドをselfを使って実行可能
        print(f'I like {self.run()}')

    def run(self):
        return 'run'

    # デストラクタ
    def __del__(self):
        print('End')

# インスタンス化
person = Person('takayuki', 22, 'japan')

# 実行方法
print(person.name)
print(person.age)
print(person.nationality)
person.say_something('akane')

# 明示的にデストラクタを使いたい場合
del person

print('##########')

# =>
# takayuki
# 22
# japan
# I am takayuki. hello, akane
# I like run
# End
# ##########
# del personを書かない場合ここに「End」と出力される
