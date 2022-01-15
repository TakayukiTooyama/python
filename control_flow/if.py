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
