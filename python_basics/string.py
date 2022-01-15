# ''と""の使い方
# ⭐️エラーになる時は前に\(バックスラッシュ)
print('hello')
print("hello")
print("I don't s")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don\'t know\"")

# 改行
print('hello. \nHow are you?')
# このままでは改行されてしまう
print('C:\name\nname')
# ⭐️rをつけることでrowデータにすることができる
print(r'C:\name\nname')

# 複数行の改行
# ⭐️\を入れることで次の行から実行となる
print("##############")
print("""\
line1
line2
line3\
""")
print("##############")
# =>
# ##############
# line1
# line2
# line3
# ##############

# 文字列連結
print('Hi' * 3 + 'Mike') # HiHiHiMike
print('py' + 'thon') # python
print('py''thon') # python

# ⭐️長い文章の時に''''を使う
s = ('aaaaaaaaaaa'
    'bbbbbbbbbbbb')
print(s) # aaaaaaaaaaabbbbbbbbbbbb

# インデックスとslice
word = 'python'
print(word[0]) # p
print(word[1]) # y
print(word[-1]) # n
print(word[2:5]) # tho
print(word[:2]) # py
print(word[2:]) # thon

# ⭐️書き換え
word = 'j' + word[1:] # jython

# ⭐️コピー
print(word[:]) # jython

# ⭐️インデックスの長さ
n = len(word)
print(n) # 6

# ⭐️文字列代入（f-string）
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x} {y} {z}')
print(f'a is {z} {y} {x}')

name = 'Takayuki'
family = 'Tooyama'
print(f'My name is {name} {family}. Watashi ha {family} {name}')

# str型に変換
print(str(1), type(str(1))) # 1<class 'str'>
print(str(3.14), type(str(3.14)))# 3.14<class 'str'>
print(str(True), type(str(True))) # True<class 'str'>
