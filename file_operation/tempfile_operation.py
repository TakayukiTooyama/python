import tempfile

"""
tempfileとは
PythonがIOバッファの上でファイルを作ってくれるため、
使い終わったら消してくれるもの
"""

# ファイル
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())
    # => hello

# ファイルを消さずに残しておく場合
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# ディレクトリ
with tempfile.TemporaryDirectory() as td:
    print(td)
    # => /var/folders/pz/ngy68qb168d7p3tykk9dqkxw0000gn/T/tmpc7m7lvzp
