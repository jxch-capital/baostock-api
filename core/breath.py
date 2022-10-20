import core.k_data as k_data
import core.industry as industry
from functools import lru_cache
from core.cache import cache_manage_day
import logging
from util.file_util import breath_new_cache_file


@lru_cache
@cache_manage_day
def build_breath_1000d():
    industry_map = industry.query_stock_industry_map()
    breath_map = {}

    keys = industry_map.keys()
    for idx, key in enumerate(keys):
        logging.info(f"[{key} {idx}/{len(keys)}]")
        breath_map[key] = {}
        dfs = k_data.query_history_k_data_plus_1000d_codes(industry_map[key]['codes'])
        for df in dfs:
            for index, row in df.iterrows():
                if 'date' not in breath_map:
                    breath_map[row['date']] = {}
                    breath_map[row['date']]['total'] = 0
                    breath_map[row['date']]['score'] = 0
                if row['close_20_sma'] is not None and row['close_20_sma'] > row['close']:
                    breath_map[row['date']]['total'] = breath_map[row['date']]['total'] + 1

    print('build breath success')
    breath_new_cache_file(breath_map)
    return breath_map
