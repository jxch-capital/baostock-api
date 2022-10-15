from functools import wraps
import schedule

cache_funcs = []
cache_funcs_day = []


def cache_manage_day(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_funcs.append(func)
        cache_funcs_day.append(func)
        return func(*args, **kwargs)

    return wrapper


def cache_manage(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_funcs.append(func)
        return func(*args, **kwargs)

    return wrapper


def clear_funcs_cache(funcs):
    for func in funcs:
        func.cache_clear()


def clear_all_cache():
    clear_funcs_cache(cache_funcs)


def clear_day_cache():
    clear_funcs_cache(cache_funcs_day)


schedule.every().day.at("00:00").do(clear_day_cache)
