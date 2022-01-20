# tarfile圧縮展開
import tarfile

# 圧縮
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

# 展開
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall(path='test_tar')

# 展開しないで中身だけを見る
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('test_dir/sub_dir/sub.txt') as f:
        print(f.read())
        # sub\n
