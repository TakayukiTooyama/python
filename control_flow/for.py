# for文
some_list = [1, 2, 3, 4, 5]
for i in some_list:
    print(i)
# =>
# 1
# 2
# 3
# 4
# 5

for s in 'abcde':
    print(s)
# =>
# a
# b
# c
# d
# e

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        break
    print(word)
# =>
# My
