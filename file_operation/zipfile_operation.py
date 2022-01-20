import glob
import zipfile

# zipファイルの圧縮
with zipfile.ZipFile('test.zip', 'w') as z:
    for f in glob.glob('test_dir/**', recursive=True):
        z.write(f)

# zipファイルの展開
with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('test_dir2')

# 展開せずに読み込み
with zipfile.ZipFile('test.zip', 'r') as z:
    with z.open('test_dir/test.txt') as f:
        print(f.read())
