# タプル型
# カンマをつけた時点でタプルとなる
t = (1, 2, 3, 4, 5)
print(type(t)) # <class 'tuple'>
t = 1, 2, 3, 4, 5
print(type(t)) # <class 'tuple'>
t = ()
print(type(t)) # <class 'tuple'>
t = 1,
print(type(t)) # <class 'tuple'>

# 結合することは出来る
new_tuple = (1, 2, 3) + (4, 5, 6)

# タプルとリストの違い
# ⭐️タプルは操作できない
# ⭐️読み込み専用で使うことが多い
# t[0] = 2 ← できない
# new_tuple = (1) + (4, 5, 6)  ← できない


# ⭐️アンパッキング
# 変数宣言 = タプルを展開する
a, b = (10, 20)
print(a, b) # 10 20
min, max = 0, 100
print(min, max) # 0 100

# ⭐️要素の入れ替え
a = 10
b = 20
print(a, b) # 10 20
a, b = b, a
print(a, b) # 20 10
