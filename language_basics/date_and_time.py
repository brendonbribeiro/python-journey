from datetime import datetime
from datetime import timedelta

today = datetime.today()
#born_date = datetime(1996, 8, 10)
born_date = datetime(month = 8, day = 10, year = 1996)

#http://strftime.org/
print(born_date.strftime("%Y-%m-%d"))

diff = today - born_date
print(diff)

after = today + timedelta(days = 2)
print(after)
