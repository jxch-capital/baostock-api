from datetime import datetime as dt
import datetime
import time

default_fmt = '%Y-%m-%d'


def date_to_str(date):
    return date.strftime(default_fmt)


def now_str():
    return date_to_str(dt.now())


def last_n_days(n):
    return dt.now() - datetime.timedelta(days=n)


def last_n_days_str(n):
    return date_to_str(dt.now() - datetime.timedelta(days=n))


def timestamp_to_str(timestamp):
    return time.strftime(default_fmt, time.localtime(int(timestamp)))
