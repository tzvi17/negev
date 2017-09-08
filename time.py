from datetime import datetime
from pytz import timezone


def show(time_zone='Israel', fmt='%Y-%m-%d %H:%M:%S %Z%z'):
    """
    prints the current time in the Negev
    :param time_zone: the name of the Negev's time zone
    :param fmt: the format of the time representation
    """
    current_time = datetime.now(timezone(time_zone))
    print "The time in the Negev is: {time}".format(time=current_time.strftime(fmt))