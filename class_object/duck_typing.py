# ダックタイピング

# 例1
class Animal:
    def animal_ability(self, animal):
        animal.voice()
        animal.walking()

class Duck():
    def voice(self):
        print("ガーガー")
    def walking(self):
        print("アヒルがお尻をフリフリ歩きます。")

class Elephant():
    def voice(self):
        print("パオーン")
    def walking(self):
        print("象がゆったりと歩きます。")

class Horse():
    def voice(self):
        print("ヒヒーン")
    def walking(self):
        print("馬がパカパカと歩きます。")

animal = Animal()
animal.animal_ability(Duck())
animal.animal_ability(Elephant())
animal.animal_ability(Horse())
# =>
# ガーガー
# アヒルがお尻をフリフリ歩きます。
# パオーン
# 象がゆったりと歩きます。
# ヒヒーン
# 馬がパカパカと歩きます。

# 例2
# 18歳以上が車の運転が可能
class Person:
    def __init__(self, age):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('no drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Car:
    def __init__(self, model=None):
        self.model = model

    def ride(self, person):
        person.drive()

car = Car()
adult = Adult()
baby = Baby()

car.ride(adult) # ok
# car.ride(baby)
