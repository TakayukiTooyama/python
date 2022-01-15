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
