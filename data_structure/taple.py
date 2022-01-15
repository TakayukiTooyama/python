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
