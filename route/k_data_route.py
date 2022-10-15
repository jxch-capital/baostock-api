from flask import Blueprint, request
import core.k_data as k_data
from util.json_util import return_json
from pre_request import pre, Rule
from util.flask_util import param_list
from util.convert_util import k_data_df_list_to_json

k_data_route = Blueprint('k_data_route', __name__)


@k_data_route.route("/k_data_1000d", methods=["POST", "GET"])
@pre.catch(post={"codes": Rule(type=list, required=True, dest="codes")},
           get={"codes": Rule(type=list, required=True, dest="codes")})
@return_json
def k_data_1000d():
    return k_data_df_list_to_json(k_data.query_history_k_data_plus_1000d_codes(param_list('codes', request)))


@k_data_route.route("/k_data_10000d", methods=["POST", "GET"])
@pre.catch(post={"codes": Rule(type=list, required=True, dest="codes")},
           get={"codes": Rule(type=list, required=True, dest="codes")})
@return_json
def k_data_10000d():
    return k_data_df_list_to_json(k_data.query_history_k_data_plus_10000d_codes(param_list('codes', request)))
