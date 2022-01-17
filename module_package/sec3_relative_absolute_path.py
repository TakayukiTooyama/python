# 絶対パス（推奨）
# 階層が深くなる場合は.で繋ぐ
from my_package.tools import utils

r = utils.say_twice('cry')
print(r) # cry!cry!

# 相対パス（非推奨）
# ..だと今自分がどのファイルにいるか探さないといけないから
# ..で一つ上の階層に行く
# from ..フォルダ import モジュール
