# フルパス（推奨①）
import my_package.tools.utils
r = my_package.tools.utils.say_twice('hello')
print(r) # hello!hello!


# モジュールから読み込む（推奨②）
from my_package.tools import utils
r = utils.say_twice('hello')
print(r) # hello!hello!


# 関数だけを読み込む（非推奨）
# コードが長くなるとどこから読み込んだのかわからなくなってしまうため
from my_package.tools.utils import say_twice
r = say_twice('hello')
print(r) # hello!hello!


# asで違う名前で読み込む（非推奨）
# モジュール名すらわからなくなってしまう
# よっぽど長いくわかりづらいもの以外使わない
from my_package.tools import utils as u
r = u.say_twice('hello')
print(r) # hello!hello!
