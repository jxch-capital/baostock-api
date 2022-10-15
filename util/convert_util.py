import json
from util.date_util import default_fmt


def k_data_df_list_to_json(df_list):
    return [{'code': df.iloc[0]['code'],
             'k': json.dumps(df.to_dict('records'), ensure_ascii=False, default=default_fmt)
             } if not df.empty else None
            for df in df_list]
