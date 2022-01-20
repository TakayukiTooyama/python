# ファイル操作
import os
import pathlib
import glob
import shutil

# ファイルの存在確認（exists）
# print(os.path.exists('test.txt'))

# ファイルであるかの確認（isfile）
# print(os.path.isfile('test.txt'))

# ディレクトリであるかの確認（isdir）
# print(os.path.isdir('file_operation'))


# ファイル・ディレクトリ名前変更（rename）
# os.rename('renamed.txt', 'test.txt')


# リンクファイルの作成（symlink）
# os.symlink('test.txt', 'symlink.txt')


# ディレクトリの作成（mkdir）
# os.mkdir('test_dir')

# ファイル作成（touch）
# pathlib.Path('empty.txt').touch()


# ディレクトリ内のディレクトリを確認（listdir）
# print(os.listdir('test_dir'))

# ディレクトリ内のファイルを確認（glob.glob）
# print(glob.glob('test_dir/*'))


# ディレクトリの削除（rmdir）
# os.rmdir('test_dir')

# ファイル削除（remove）
# os.remove('empty.txt')


# コピー（shutil.copy）
# shutil.copy('test_dir', 'test_dir2')


# 現在のパスの確認（getcwd）
# print(os.getcwd())


# ディレクトリ内（ファイル, ディレクトリ）全てを削除
# shutil.rmtree('test_dir')
