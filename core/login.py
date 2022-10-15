from functools import wraps
import baostock as bs


def login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            bs.login()
            return func(*args, **kwargs)
        finally:
            bs.logout()

    return wrapper
