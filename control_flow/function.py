# 関数定義
def say_something():
    print('実行')

# 実行方法①
say_something()

# 実行方法②
f = say_something
f()

# 型
print(type(say_something)) # <class 'function'>


# 返り値
def say_something():
    s = '返り値'
    return s

result = say_something()
print(result) # 返り値


# 引数
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don'n know"

result1 = what_is_this('red')
result2 = what_is_this('green')
print(result1) # tomato
print(result2) # green pepper


def menu(entree='chcken', drink='beer', dessert='ice'):
    print('entree', entree)
    print('drink', drink)
    print('dessert', dessert)

# 位置引数
menu('beef', 'beer', 'ice')

# キーワード引数
menu(entree='beef', drink='beer', dessert='ice')

# 位置引数とキーワード引数を混ぜることも可能
menu('beef', drink='beer', dessert='ice')

# デフォルト引数
menu()

# ⭐️デフォルト引数の注意点
# リストや辞書をデフォルト引数に渡すと参照渡しになってしまうため使わない
def test_func(x, l=[]):
    l.append(x)
    return l
r = test_func(100)
print(r) # [100]
r = test_func(100)
print(r) # [100, 100]

# ⭐️関数内でリストが使いたい場合
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l
r = test_func(100)
print(r) # [100]
r = test_func(100)
print(r) # [100]
