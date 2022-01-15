# 辞書型
d = {'x': 10, 'y': 20}
print(d, type(d)) # {'x': 10, 'y': 20} <class 'dict'>
d2 = dict(a=10, b=20)
print(d2) # {'a': 10, 'b': 20}

# 要素取得
print(d['x']) # 10
print(d.get('x')) # 10

# 要素変更
d['x'] = 100
print(d) # {'x': 100, 'y': 20}

# 要素追加
d['z'] = 200
print(d) # {'x': 100, 'y': 20, 'z': 200}

# 要素削除（pop, del）
d.pop('x')
print(d) # {'y': 20, 'z': 200}
del d['y']
print(d) # {'z': 200}


# 辞書メソッド
d3 = {'x': 10, 'y': 20, 'z': 30}
d4 = {'x': 100, 'o': 300, 'p':400}

# キーと値の取得（keys, values）
print(d3.keys()) # dict_keys(['x', 'y', 'z])
print(d3.values()) # dict_values([10, 20, 30])

# 辞書の更新（update）
d3.update(d4)
print(d3) # {'x': 100, 'y': 20, 'z': 30, 'o': 300, 'p': 400}

# 辞書を空にする（clear）
d3.clear()
print(d3) # {}

# キーがあるかどうか確かめる（in）
print('p' in d4) # True
print('j' in d4) # False
