from config import timeZone

import datetime
import dateutil
from dateutil import tz

def currentTime():
    t = datetime.datetime.now(dateutil.tz.gettz(timeZone())
    return t
