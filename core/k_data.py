import baostock as bs
import pandas as pd
from functools import lru_cache
from core.login import login
from core.cache import cache_manage_day
import util.date_util as date_util


@login
def query_history_k_data_plus(code, cols, start_date, end_date, frequency, adjust):
    """
    查询股票K线历史数据
    :param code: 股票代码
    :param cols: 指标
    :param start_date: 开始日期
    :param end_date: 结束日期
    :param frequency: 数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写；指数没有分钟线数据；周线每周最后一个交易日才可以获取，月线每月最后一个交易日才可以获取
    :param adjust: 复权类型，默认不复权：3；1：后复权；2：前复权。已支持分钟线、日线、周线、月线前后复权。
    :return: DataFrame 类型的股价数据
    """
    rs = bs.query_history_k_data_plus(code, cols, start_date, end_date, frequency, adjust)
    data_list = []
    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())
    return pd.DataFrame(data_list, columns=rs.fields)


def query_history_k_data_plus_cols(code, start_date, end_date, frequency):
    return query_history_k_data_plus(code,
                                     "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                     start_date, end_date, frequency, adjust="2")


def query_history_k_data_plus_d(code, start_date, end_date):
    return query_history_k_data_plus_cols(code, start_date, end_date, frequency="d")


def query_history_k_data_plus_d_today(code, start_date):
    return query_history_k_data_plus_d(code, start_date, end_date=date_util.now_str())


@lru_cache
@cache_manage_day
def query_history_k_data_plus_1000d(code):
    return query_history_k_data_plus_d_today(code, date_util.last_n_days_str(1000))


@lru_cache
@cache_manage_day
def query_history_k_data_plus_10000d(code):
    return query_history_k_data_plus_d_today(code, date_util.last_n_days_str(10000))


def query_history_k_data_plus_1000d_codes(codes):
    return [query_history_k_data_plus_1000d(code) for code in codes]


def query_history_k_data_plus_10000d_codes(codes):
    return [query_history_k_data_plus_10000d(code) for code in codes]
