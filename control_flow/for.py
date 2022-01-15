# for文
some_list = [1, 2, 3, 4, 5]
for i in some_list:
    print(i)
# =>
# 1
# 2
# 3
# 4
# 5

for s in 'abcde':
    print(s)
# =>
# a
# b
# c
# d
# e

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break
    print(word)
# =>
# My


# for else文
for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('I ate all')
# =>
# apple
# banana
# orange
# I ate all


# ⭐️range関数
# range(始める数字, 終わる数字, 間隔)
for i in range(1, 7, 2):
    print(i)
# =>
# 1
# 3
# 5

# ⭐️回したいだけの時（_を使う）
for _ in range(5):
    print('hello')
# hello
# hello
# hello
# hello
# hello


# ⭐️enumerate関数
# インデックスの番号を振りたい場合
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 orange


# ⭐️zip関数
# 同時に複数のリストを使いたい時
# いちいちインデックスを書かなくてい
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


# 辞書とfor文
d = {'x': 100, 'y': 200}
for k, v in d.items():
    print(k, ':', v)

# 仕組み
print(d.items()) # dict_items([('x', 100), ('y', 200)])
# リストの中身がタプルになっている
# アンパッキングを行い、keyとvalueの要素を変数に入れている
# ↓
# k, v = ('x', 100)
