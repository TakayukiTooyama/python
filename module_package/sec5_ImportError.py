# ImportErrorの使い所
# 古いバージョンでも新しいバージョンでもどちらでもインポートできるようにする時に使う
try:
    from my_package import utils
except ImportError:
    from my_package.tools import utils

utils.say_twice('word')
