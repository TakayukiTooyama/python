# クラスメソッド
# ・インスタンス化していなくても呼び出すことができる

# スタティックメソッド
# ・selfを書かなくていい
# ・あまり使うことはない
# ・関連性のあるものをクラス内に置くため

class Person:
    kind = 'human'

    @classmethod
    def what_is_your_kind(self):
        return self.kind

    @staticmethod
    def about():
        print('about human')

person = Person()

# クラスメソッド
print(Person.kind) # human
print(Person.what_is_your_kind()) # human

# スタティックメソッド
person.about() # about human
