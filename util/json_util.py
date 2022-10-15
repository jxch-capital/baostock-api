import json
from datetime import datetime, date

from pandas import DataFrame
from util.date_util import default_fmt
import functools
import logging


def json_dumps_default_date(obj, fmt=default_fmt):
    if isinstance(obj, datetime):
        return obj.strftime(fmt)
    elif isinstance(obj, date):
        return obj.strftime(fmt)
    else:
        return obj


def return_json(func, json_date_fmt_func=json_dumps_default_date):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        res = func(*args, **kw)
        if type(res) is str:
            return res
        if type(res) is dict or type(res) is list:
            return json.dumps(res, ensure_ascii=False, default=json_date_fmt_func)
        if type(res) is DataFrame:
            return json.dumps(res.to_dict('records'), ensure_ascii=False, default=json_date_fmt_func)
        logging.info("不支持的转JSON类型")
        return res

    return wrapper
