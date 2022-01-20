# 11.文字列検索
message = '今日はとても夜空が綺麗だ。'
print(message.find('夜空'))


# 12.型変換
x = 1
print(str(x), type(str(x)))
# "1" <class 'str'>

x = 1.52
print(str(x), type(str(x)))
# "1.52" <class 'str'>

x = [1, 2, 3]
print(str(x), type(str(x)))
# "[1, 2, 3]" <class 'str'>

x = dict(nome='john', birth='US')
print(str(x), type(str(x)))
# "{'nome': 'john', 'birth': 'US'} <class 'str'>"


# 13.包含関係
A = 'sba'
B = 'gasba'
print(A in B)
# True

A = 'xdh'
B = 'orweit'
print(A in B)
# False


# 14.特定の値を抽出
numbers = [0, 3, 8, -4, 9, 1]
print(numbers[1])
# 3
print(numbers[-1])
# 1
numbers.append(2)
print(numbers)
# [0, 3, 8, -4, 9, 1, 2]


# 15.特定の値を挿入
numbers.insert(0, 5)
print(numbers)
# [5, 0, 3, 8, -4, 9, 1, 2]
numbers.insert(-1, -3)
print(numbers)
# [5, 0, 3, 8, -4, 9, 1, -3, 2]


# 16.特定の値を削除
# 値指定削除
numbers.remove(5)
print(numbers)
# [0, 3, 8, -4, 9, 1, -3, 2]

# 場所指定削除
numbers.pop(-3)
print(numbers)
# [0, 3, 8, -4, 9, -3, 2]


# 17.フィルター
even_list = list(filter(lambda num: num % 2 == 0, numbers))
print(even_list)
# [0, 8, -4, 2]


# 18.引数と一致する要素のインデックス
print(numbers.index(-4))
# 3


# 19.ソート
# 昇順
numbers.sort()
print(numbers)
# [-4, -3, 0, 2, 3, 8, 9]

# 降順
numbers.sort(reverse=True)
print(numbers)
# [9, 8, 3, 2, 0, -3, -4]


# 20.要素の削除
d = {
    'A' : '遠山',
    'B' : '宜志',
    'C' : '男性',
    'D' : '新潟県',
    'E' : '海外旅行',
}
d.pop('A')
d.pop('B')
print(d)
# {'C': '男性', 'D': '新潟県', 'E': '海外旅行'}
d.clear()
print(d)
# {}
