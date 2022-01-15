# 集合型
# ⭐️setでは同一の要素は重複できない
# ⭐️setはインデックス番号で要素を管理していない
a = {1, 2, 3, 4, 4, 5, 6}
b = {2, 3, 6, 7}

print(a, type(a)) # {1, 2, 3, 4, 5, 6} <class 'set'>

# 差集合（-）
print(a - b) # {1, 4, 5}
print(b - a) # {7}

# 積集合（&）
print(a & b) # {2, 3, 6}

# 和集合（|）
print(a | b) # {1, 2, 3, 4, 5, 6, 7}

# 対象差集合（^）
# aかbどちらかにはあるが重複はしていないもの
print(a ^ b) # {1, 4, 5, 7}


# 集合型メソッド
s = {1, 2, 3, 4, 5}

# 追加（add）
s.add(6)
print(s) # {1, 2, 3, 4, 5, 6}

# 削除（remove, clear, pop）
s.remove(6)
print(s) # {1, 2, 3, 4, 5}
s.pop()
print(s) # {2, 3, 4, 5}
s.clear()
print(s) # set()


# 集合型の使い所
# 共通の友達
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends) # {'D'}

# 重複をなくユニークなものだけを取得したい時
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind) # {'apple', 'banana'}
