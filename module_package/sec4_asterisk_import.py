# アスタリスクインポート, __init__.py, __all__ = []

# 読み込むファイルと同じ階層の__init__.pyに
# __all__ = ['human', 'animal']とすることで*が使えるよになる

# しかし、「非推奨」
# *を使うことでどこのモジュールからインポートしたかわからなくなってしまう
from my_package.talk import *

print(animal.sing())
print(animal.cry())

print(human.sing())
print(human.cry())
