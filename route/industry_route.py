from flask import Blueprint, request
from util.json_util import return_json
from pre_request import pre, Rule
import core.industry as industry

industry_route = Blueprint('industry_route', __name__)


@industry_route.route("/industry_map", methods=["POST", "GET"])
@pre.catch({})
@return_json
def industry_map():
    return industry.query_stock_industry_map()
