from flask import Blueprint, request

from util.json_util import return_json, to_json
from pre_request import pre, Rule
from util.flask_util import param_list, param
import util.date_util as date_util
import core.k_data as k_data

grafana_route = Blueprint('grafana_route', __name__)

fields = {
    "codes": Rule(type=list, required=True, dest="codes"),
    "start": Rule(type=int, required=True, dest="start"),
    "end": Rule(type=int, required=True, dest="end"),
}


@grafana_route.route("/grafana/", methods=["get"])
def grafana_root():
    return '{"status":"success"}'


@grafana_route.route("/grafana/k_data", methods=["post", "get"])
@pre.catch(fields)
@return_json
def query_k_data():
    codes = param_list("codes", request)
    start = date_util.timestamp_to_str(param("start", request))
    end = date_util.timestamp_to_str(param("end", request))
    res = {}
    for code in codes:
        df = k_data.query_history_k_data_plus_d(code, start, end)
        res['date'] = df['date'].tolist() \
            if 'date' not in res or len(res['date']) < len(df['date'].tolist()) \
            else res['date']
        res[code.replace('.', '')] = to_json(df)
    return res
