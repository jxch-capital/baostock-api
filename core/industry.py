import baostock as bs
import pandas as pd
from functools import lru_cache
from core.login import login
from core.cache import cache_manage_day


@login
def query_stock_industry():
    rs = bs.query_stock_industry()
    industry_list = []
    while (rs.error_code == '0') & rs.next():
        industry_list.append(rs.get_row_data())
    return pd.DataFrame(industry_list, columns=rs.fields)


@lru_cache
@cache_manage_day
def query_stock_industry_dict_list():
    return query_stock_industry().to_dict('records')


@lru_cache
@cache_manage_day
def query_stock_industry_map():
    industry_map = {}
    for industry in query_stock_industry_dict_list():
        key = industry['industry'] if industry['industry'] != '' else '无分类'
        if key in industry_map:
            industry_map[key]['info'].append(industry)
            industry_map[key]['codes'].append(industry['code'])
        else:
            industry_map[key] = {}
            industry_map[key]['info'] = [industry]
            industry_map[key]['codes'] = [industry['code']]
    return industry_map
