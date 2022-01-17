def no_execution():
    return '誤った実行です'

print('test.py: ', __name__)
print('test.py: ', no_execution())

if __name__ == '__main__':
    print('メインで実行してください')
    # 本当はここに書いていく
