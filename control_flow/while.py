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
