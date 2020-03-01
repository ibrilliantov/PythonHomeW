from dateutil.relativedelta import *
from datetime import *


dt_now = datetime.now()
print(dt_now)

delta = timedelta(days=1)

dt_yestd = dt_now - delta
print(dt_yestd)

dt_tomrr = dt_now + delta
print(dt_tomrr)


today = dt_now
r = relativedelta(months=1)
result = today - r
print(result)



formats = datetime.strptime("01/01/17 12:10:03.234567", "%d/%m/%y %H:%M:%S.%f")
print(formats)
dt = formats + delta
print(dt)