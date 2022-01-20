# 21.情報の取得
d = {
    'A' : '遠山',
    'B' : '宜志',
    'C' : '男性',
    'D' : '新潟県',
    'E' : '海外旅行',
}
# キーのみの表示
print(d.keys())
# dict_keys(['A', 'B', 'C', 'D', 'E'])

# 値の中に男性という文字列が存在するか
print('男性' in d.values())
# True

# 全てのキーと値の表示
for k, v in d.items():
    print(f'key: {k}, value: {v}')
# key: A, value: 遠山
# key: B, value: 宜志
# key: C, value: 男性
# key: D, value: 新潟県
# key: E, value: 海外旅行


# 22.辞書内の要素検索
print(d.get('C'))
# 男性
print(d.get('E'))
# 海外旅行


# 23.if文を使って条件分岐
num = 0
if num > 0:
    print('正の値です')
elif num == 0:
    print('0です')
else:
    print('負の値です')
# 0です


# 24.論理演算子を使って複数条件の指定
a = -3
if 0 <= a < 10 and a % 2 == 0:
    print('一桁の偶数です')
elif (a < 0 and a % 2 == 1):
    print('負の奇数です')
else:
    print('整数です')
# 負の奇数です


# 25.リストの要素を表示
names = ['John', 'Kevin', 'Louis']
for name in names:
    print(name)
# John
# Kevin
# Louis


# 26.range関数
for num in range(10):
    print(num)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


# 27.強制終了
for num in range(10):
    if num == 6:
        break
    print(num)
# 0
# 1
# 2
# 3
# 4
# 5


# 28.ループの途中で特定の処理を実行
for num in range(10):
    if num == 3:
        continue
    print(num)
# 0
# 1
# 2
# 4
# 5
# 6
# 7
# 8
# 9


# 29.複数のリストを同時に処理
lasts = ['加藤', '佐藤', '田中']
firsts = ['雄一', '拓也', '太朗']

for last, first in zip(lasts, firsts):
    print(last, first)
# 加藤 雄一
# 佐藤 拓也
# 田中 太朗


# 30.要素と同時にインデックス情報の取得
for index, last in enumerate(lasts):
    print(f'{index}番の{last}です')
# 0番の加藤です
# 1番の佐藤です
# 2番の田中です
