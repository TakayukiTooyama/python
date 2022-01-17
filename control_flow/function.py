# 関数定義
from ast import List


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


# 位置引数のタプル化（位置引数と併用可）
def say_something(word, *args):
    print(word) # 'Hi'
    print(args) # ('Mike', 'Nance')
    for arg in args:
        print(arg)
        # Mike
        # Nance

say_something('Hi', 'Mike', 'Nance')


# キーワード引数の辞書化
def menu(**kwargs):
    print(kwargs) # {'entree': 'chiken', 'dessert': 'ice'}
    for k, v in kwargs.items():
        print(k, v)
        # entree chiken
        # dessert ice

# パターン①
menu(entree='chiken', dessert='ice')

# パターン②
d = {
    'entree': 'chiken',
    'dessert': 'ice'
}
menu(**d)


# 関数内関数
# outer関数内だけで使うものを定義
def outer(a, b):

    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r) # 3

outer(1, 2)


# クロージャー
# 初めに設定した引数をもとに後々用途によって使い分けたい時に使う
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)

print(cal1(10)) # 314.0
print(cal2(10)) # 314.1592


# デコレーター
# 関数を実行する前や後に何かしら機能を付け加えたい時に使う
def print_more(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(*args)
        print(*kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)


# ラムダ（lambda）
# 単純な2行くらいの関数はlambdaを使って書ける！
l = ['Mon', 'tue', 'wed', 'Thu', 'fri', 'Sat', 'sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())


# ジェネレーター
# ・反復処理をするときに1要素取り出してそれを生成していく
# ・nextを使って呼び出すことができ、毎回関数を抜ける
# ・returnはない
# ・yieldがあるとその関数はジェネレーターとして判断される

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
print(next(g))
print('###########')
print(next(g))
print('###########')
print(next(g))
# =>
# Good morning
# ###########
# Good afternoon
# ###########
# Good night
