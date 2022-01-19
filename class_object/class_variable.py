# クラス変数

class Person:
    # ⭐️クラス変数
    # クラス内で共通して使える、変化しないもの
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

person = Person('A')
person.who_are_you() # A human
person = Person('B')
person.who_are_you() # B human


# ⭐️配列などはクラス変数にはせずにinitで作成
# インスタンスを作り直しても引き継がれてしまう
class T:
    # words = []

    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = T()
c.add_word('add1')
c.add_word('add2')
print(c.words) # ['add1', 'add2']

d = T()
d.add_word('add3')
d.add_word('add4')
print(d.words) # ['add3', 'add4']
