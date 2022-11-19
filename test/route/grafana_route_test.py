import time
import datetime


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=10)

star = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
t = int(time.mktime(time.strptime(str(today), '%Y-%m-%d')))
print(t)
print(star)