# ファイル操作
# w = 上書き
# a = 追記
# r = 読み込む
# print
f = open('test.txt', 'w')
f.write('Test')
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()


s = """\
AAA
BBB
CCC
DDD
"""
# withステートメント
# ファイルの書き込み（w, a）
with open('test.txt', 'w') as f:
    f.write(s)


# ファイルの読み込み（r）
with open('test.txt', 'r') as f:
    # 全て読み込む
    print(f.read())

with open('test.txt', 'r') as f:
    # 1行ずつ読み込む
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break

with open('test.txt', 'r') as f:
    # チャンクごとに読み込む
    while True:
        chuck = 2
        line = f.read(chuck)
        print(line)
        if not line:
            break


# 書き込み + 読み込み（w+）
with open('test.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read(), end='')

# 読み込み + 書き込み（r+）
with open('test.txt', 'r+') as f:
    f.write(s)
    f.seek(0)
    print(f.read(), end='')
