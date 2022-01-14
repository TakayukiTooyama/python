# 変数宣言とprint出力

num = '1'
name = 'TAKA'
new_num = int(num)

print(num, type(num))
# => 1 <class 'str'>
print(name, type(name))
# => TAKA <class 'str'>
print(new_num, type(new_num))
# => 1 <class 'int'>

print('Hi', 'Mike')
# Hi Mike
print('Hi', 'Mike', sep=',')
# Hi,Mike
print('Hi', 'Mike', sep=',', end='.\n')
# Hi,Mike.
print('Hi', 'Mike', sep=',', end='')
print('Hi', 'Mike', sep=',', end='')
# Hi,MikeHi,Mike
