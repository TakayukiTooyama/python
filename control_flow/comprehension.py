# リスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

# これを1行で書くことができる
# r = []
# for i in t:
#     if i % 2 == 0:
#         r.append(i)
# print(r)

r = [i for i in t if i % 2 == 0]
print(r) # [2, 4]

# 2重ループ
# リスト内包表記でもかけるがコードが読みづらくなってしまう
# r = [i * j for i in t for j in t2]
# print(r)


# 辞書内包表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y
print(d) # {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}

d = {x: y for x, y in zip(w, f)}
print(d) # {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}
