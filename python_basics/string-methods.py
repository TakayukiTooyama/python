# ⭐️文字列メソッド
s = 'My name is Mike. Hi Mike'

# 最初の文字のみ大文字
print(s.capitalize()) # My name is mike. hi mike

#文字列をタイトルケースにする
print(s.title()) # My Name Is Mike. Hi Mike

# 小文字変換
print(s.lower()) # my name is mike. hi mike

# 大文字変換
print(s.upper()) # MY NAME IS MIKE. HI MIKE

# 文字列の登場回数
print(s.count('Mike')) # 2

# 文字列が初めて登場する位置
print(s.find('Mike')) # 11

# 文字列が最後に見つかった位置
print(s.rfind('Mike')) # 20

# 文字列に部分文字列が含まれているかどうか
print('Mike' in s) # True

# 文字列の末尾に検索文字列があれば True なければ False
print(s.endswith('Mike')) # True

# 文字列の先頭に検索文字列があれば True なければ False
print(s.startswith('My')) # True

# 文字列が初めて登場する位置 + 文字列が見つからなかったときにValueError
print(s.index('Mike')) # 11

# 置換
print(s.replace('Mike', 'Takayuki')) # My name is Takayuki. Hi Takayuki

# 文字列分割
print(s.split('. ')) # ['My name is Mike', 'Hi Mike']

# 文字列結合
print(','.join(['Hi', 'Mike'])) # Hi,Mike
print(' '.join(s)) # M y   n a m e   i s   M i k e .   H i   M i k e

# 両端の空白削除
print(' x '.strip()) # 'x'
