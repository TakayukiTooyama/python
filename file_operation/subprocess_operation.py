import subprocess
import os

# subprocessとは
# ターミナルで行っているコマンドをPython上で行えるようにするもの

# 旧
# os.system('ls')

# 新（推奨）
subprocess.run(['ls', '-al'])

# 非推奨（rm -rfなどを簡単に付け加えられてしまうため）
# subprocess.run('ls -al', shell=True)

# パイプなどを使いたい場合
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
