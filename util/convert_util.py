import json
import stockstats
import pandas as pd
from util.date_util import default_fmt
from pandas import DataFrame


def k_data_df_list_to_json(df_list):
    return [{'code': df.iloc[0]['code'],
             'k': json.dumps(df.to_dict('records'), ensure_ascii=False, default=default_fmt)
             } if not df.empty else None
            for df in df_list]


def to_support_k_data(df):
    df["open"] = pd.to_numeric(df["open"])
    df["high"] = pd.to_numeric(df["high"])
    df["low"] = pd.to_numeric(df["low"])
    df["close"] = pd.to_numeric(df["close"])
    df["preclose"] = pd.to_numeric(df["preclose"])
    df["volume"] = pd.to_numeric(df["volume"])
    df["amount"] = pd.to_numeric(df["amount"])
    df["adjustflag"] = pd.to_numeric(df["adjustflag"])
    df["turn"] = pd.to_numeric(df["turn"])
    df["tradestatus"] = pd.to_numeric(df["tradestatus"])
    df["pctChg"] = pd.to_numeric(df["pctChg"])
    df["isST"] = pd.to_numeric(df["isST"])
    return df


def to_index_k_data(old_df):
    old_df = to_support_k_data(old_df)
    the_code = old_df['code']
    old_df.drop(columns=['code'])
    ss = stockstats.StockDataFrame.retype(old_df)
    df = ss[['open', 'close', 'high', 'low', 'volume',
             'tr', 'atr', 'close_-1_d', 'close_5_sma', 'close_20_sma', 'close_60_sma', 'close_120_sma', 'close_200_sma',
             'close_20_sma_-1_d', 'close_60_sma_-1_d', 'close_120_sma_-1_d', 'close_5_ema',
             'close_20_ema', 'close_60_ema', 'close_120_ema', 'close_20_ema_-1_d', 'close_200_ema',
             'macd', 'macds', 'macdh', 'kdjk', 'kdjd', 'kdjj']]
    df['rate_sma20'] = df['close_20_sma'] / (df['close_20_sma'] - df['close_20_sma_-1_d'])
    df['rate_ema20'] = df['close_20_ema'] / (df['close_20_ema'] - df['close_20_ema_-1_d'])
    df['rate_sma60'] = df['close_60_sma'] / (df['close_60_sma'] - df['close_60_sma_-1_d'])
    df['rate_ema60'] = df['close_60_ema'] / (df['close_60_ema'] - df['close_60_ema_-1_d'])
    df['rate_sma120'] = df['close_120_sma'] / (df['close_120_sma'] - df['close_120_sma_-1_d'])
    df['rate_ema120'] = df['close_120_ema'] / (df['close_120_ema'] - df['close_120_ema_-1_d'])
    df['rate_sma200'] = df['close_200_sma'] / (df['close_200_sma'] - df['close_200_sma_-1_d'])
    df['rate_ema200'] = df['close_200_ema'] / (df['close_200_ema'] - df['close_200_ema_-1_d'])
    ss = stockstats.StockDataFrame.retype(df)
    df['rate_ema20_5_ema'] = ss[['rate_ema20', 'rate_ema20_5_ema']]['rate_ema20_5_ema']
    df['rate_ema60_5_ema'] = ss[['rate_ema60', 'rate_ema60_5_ema']]['rate_ema60_5_ema']
    df['rate_ema120_5_ema'] = ss[['rate_ema120', 'rate_ema120_5_ema']]['rate_ema120_5_ema']
    df['rate_ema200_5_ema'] = ss[['rate_ema200', 'rate_ema200_5_ema']]['rate_ema200_5_ema']
    df.reset_index(inplace=True)
    df['code'] = the_code
    return DataFrame(df)
