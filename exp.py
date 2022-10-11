import calendar
from datetime import datetime
import time

print(calendar.month(2019 , 6))

now = datetime.now()
print(now)

print(now.strftime(' %a %A %y'))

start = datetime.now()


time.sleep(60)

end = datetime.now()
print("*******************************")
print(start)
print("*******************************")
print(end)
print("*******************************")

