# 例外処理
l = [1, 2, 3]
i = 5

# 通常（try..except）
try:
    l[i]
except:
    print('except')
# => except


# 特定のエラー対処（IndexError, NameErrorなど）
try:
    l[i]
except IndexError as ex:
    print(ex)
except NameError as ex:
    print(ex)
# => # list index out of range


# ほとんどのエラーの対処（非推奨）
try:
    l + ()
except Exception as ex:
    print(ex)
# => can only concatenate list (not "tuple") to list


# エラーなく抜けた場合に出力（else）
try:
    l
except IndexError as ex:
    print(ex)
else:
    print('done')
# => done


# 最後に必ず出力したい時（finally）
try:
    l
finally:
    print('clean up')
# => clean up


# 独自例外
# 自分で作成した独自の例外をraiseを用いて発生させることができる
# 自分たちで作ったエラーなので見てすぐわかる
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
check()

# 独自例外なりの対応策をtry..exceptで書いておくことによって開発がやりやすくなる
try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')
