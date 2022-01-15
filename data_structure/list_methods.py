# リストメソッド
r = [1, 2, 3, 4, 5, 1, 2, 3]

# 指定した要素のインデックスの場所（index）
# index(検索要素, 検索を始める位置)
print(r.index(3)) # 2
print(r.index(3, 4)) # 7

# 要素の数（count）
print(r.count(3)) # 2

# ソート（sort, reverse）
r.sort()
print(r) # [1, 1, 2, 2, 3, 3, 4, 5]
r.reverse()
print(r) # [5, 4, 3, 3, 2, 2, 1, 1]

# 区切る（split）
s = 'My name is Mike'
to_split = s.split(' ')
print(to_split) # ['My', 'name', 'is', 'Mike']

# 結合（join）
x = ' '.join(to_split) # My name is Mike
print(x)
