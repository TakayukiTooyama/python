# リスト
l = [1, 20, 4, 50, 2, 1, 2]
print(l[0]) # 1
print(l[1]) # 20
print(l[-1]) # 2
print(l[:2]) # [1, 20]
print(l[2:5]) # [4, 50, 2]
print(l[:]) # [1, 20, 4, 50, 2, 1, 2]
print(len(l)) # 7
print(type(l)) # <class 'list'>


n = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
# ⭐️一つ飛ばし
print(n[::2]) # [1, 3, 4, 6, 8, 10]
# ⭐️逆順
print(n[::-1]) # [10, 9, 8, 7, 6, 5, 4, 4, 3, 2, 1]


# ネスト
str = ['a', 'b', 'c']
num = [1, 2, 3]
nest = [str, num]
print(nest) # [['a', 'b', 'c'], [1, 2, 3]]
print(nest[0]) # ['a', 'b', 'c']
print(nest[0][1]) # b
print(nest[1][2]) # 3


# リスト操作
# リスト要素変更
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s[0] = 'X'
s[2:5] = ['C', 'D', 'E']
print(s[0]) # 'X'
print(s) # ['X', 'b', 'C', 'D', 'E', 'f', 'g']

# ⭐️空のリストへ
s[:] = []
print(s) # []


# リスト要素追加・取得
num_list = [1, 2, 3, 4, 5]
# 末尾に追加
num_list.append(100)
print(num_list) # [1, 2, 3, 4, 5, 100]

# 指定したインデックスに追加
num_list.insert(0, 200)
print(num_list) # [200, 1, 2, 3, 4, 5, 100]

# 末尾の要素取得
num_list.pop()
print(num_list) # [200, 1, 2, 3, 4, 5]

# 先頭の要素取得
num_list.pop(0)
print(num_list) # [1, 2, 3, 4, 5]


# リスト要素削除
# del
# 指定したものを削除
del num_list[0]
print(num_list) # [2, 3, 4, 5]

# remove
# 指定したものを削除
num_list.remove(2)
print(num_list) # [3, 4, 5]
num_list.remove(3)
print(num_list) # [4, 5]


# リストの結合
# a + b
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
x = a + b
print(x) # [1, 2, 3, 4, 5, 6, 7, 8]

# extend
a.extend(b)
print(a) # [1, 2, 3, 4, 5, 6, 7, 8]
