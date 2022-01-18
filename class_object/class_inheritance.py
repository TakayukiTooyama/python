# クラス継承（継承, メソッドオーバライド, super）

class Car:
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

# ⭐️Carクラス継承
class ToyotaCar(Car):
    # ⭐️メソッドのオーバライド
    def run(self):
        print('fast')

# Carクラス継承
class TeslaCar(Car):
    # ⭐️親クラスの初期値を継承（super）しつつ、独自のクラス変数を定義
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    # 独自のメソッド
    def auto_run(self):
        print('auto_run')

car = Car()
car.run()
print('#############')
# デフォルト引数なし
toyotaCar = ToyotaCar('Lexus')
toyotaCar.run()
print('#############')
# デフォルト引数あり
teslaCar = TeslaCar()
teslaCar.run()
teslaCar.auto_run()

# =>
# run
# #############
# fast
# #############
# run
# auto_run


# 多重継承
class Person:
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Roboto:
    def run(self):
        print('roboto run')

# ⭐️重複があった場合、左の継承が優先される
class PersonRoboto(Person, Roboto):
    def fly(self):
        print('fly')

person_roboto = PersonRoboto()
person_roboto.talk()
person_roboto.run()
person_roboto.fly()
# =>
# talk
# person run
# fly
