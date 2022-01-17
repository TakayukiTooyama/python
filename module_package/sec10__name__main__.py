# __name__と__main__
import my_package.test

def main():
    print('sec10: ', __name__)


if __name__ == '__main__':
    main()

# 実行結果
# test.py:  my_package.test
# test.py:  誤った実行です
# sec10:  __main__

# ⭐️基本的には上のような書き方をする
# メインで実行された時しか実行できなくする
# ⭐️「importされた時点でprintが実行されてしまう」
# そのためテストのために書いていた関数などの実行に繋がってしまう
