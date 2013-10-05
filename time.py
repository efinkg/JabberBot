import datetime
import dateutil
from dateutil import tz
time = datetime.datetime.now(dateutil.tz.gettz('America/Chicago'))
print str(time)
