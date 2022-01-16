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
