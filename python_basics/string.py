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
