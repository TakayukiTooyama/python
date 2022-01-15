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
print(s)

# 削除（remove, clear, pop）
s.remove(6)
print(s)
s.clear()
print(s)
s.pop()
print(s)
