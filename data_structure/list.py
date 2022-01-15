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
