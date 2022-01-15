# if文
# インデントを綺麗に合わせる必要がある！
x = -10

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')


a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')


# Notの使い所
x = 1
y = [1, 2, 4]
z = [2, 4]

# ①inを使う時
if x in y:
    print('in') # in
if x not in z:
    print('Not in') # Not in

# ②isを使う時
is_empty = None
if is_empty is not None:
    print('None!!')

# ⭐️③boolean型を否定する時
is_ok = False
if not is_ok:
    print('False') # False
else:
    print('True')


# ⭐️値が入っていない判定
# リストに値が入っていない時の条件分岐
# False, 0, 0.0, '', [], (), {}, set()
lists = []
if lists:
    print('Yes!')
else:
    print('No!')


# ⭐️Noneの判定
is_empty = None

if is_empty is None:
    print('None!!') # None
if is_empty is not None:
    print('None!!')

# isとは「オブジェクト同士が同じもの」にTrueを返す
print(1 == True) # True
print(1 is True) # False
print(None is None) # True
