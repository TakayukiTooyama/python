from calendar import month
import datetime

now = datetime.datetime.now()
print(now) # 2022-01-20 01:14:17.646124
print(now.isoformat()) # 2022-01-20T01:14:17.646124

"""
%d = 日
%m = 月
%y = 年後半の2桁
%Y = 年
%H = 時
%M = 分
%S = 秒
%f = マイクロ秒
"""
print(now.strftime('%Y年%m月%d日%H時%M分')) # 2022年01月20日

today = datetime.date.today()
print(today) # 2022-01-20

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t) # 01:10:05.000100
print(t.isoformat()) # 01:10:05.000100


# 1年前
d = datetime.timedelta(days=365)
print(now - d)
# 1週間前
d = datetime.timedelta(weeks=1)
print(now - d)
# 1日前
d = datetime.timedelta(days=1)
print(now - d)
# 1時間前
d = datetime.timedelta(hours=1)
print(now - d)


import time
# 2秒後に実行したい場合
time.sleep(2)
print('###')
# エポックタイム（1970年1月1日からの秒数）
print(time.time())
