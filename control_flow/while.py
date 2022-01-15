# while文
count = 0
while count < 5:
    print(count)
    count += 1
# =>
# 0
# 1
# 2
# 3
# 4


# break文
count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1
# =>
# 0
# 1
# 2
# 3
# 4


# continue文
count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1
# =>
# 0
# 1
# 3
# 4


# while else文
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')
# =>
# 0
# 1
# 2
# 3
# 4
# done


# while else break文
count = 0
while count < 5:
    if count == 1:
        break

    print(count)
    count += 1
else:
    print('done')
# =>
# 0


# ⭐️input関数
# 文字列の入力待ちになる
while True:
    word = input('Enter: ')
    if word == 'ok':
        break
    print('next')

# 数値の入力を待ちたい場合
while True:
    word = input('Enter: ')
    num = int(word)
    if num == 100:
        break
    print('next')
