import time
from _datetime import datetime,timedelta


print("changes test made for git")

print(time.time())
print(time.localtime())
t = datetime.now()
print (t)
print ('%s/%s/%s'%(t.year,t.day,t.month))
print('%s/%s/%s,%s:%s:%s'%(t.day,t.month,t.year,t.hour,t.minute,t.second))

date = datetime.now()
print(date)
print(date+timedelta(10))
