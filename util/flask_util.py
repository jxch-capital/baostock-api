def register_routes_arr(app, *routes_arr):
    for routes in routes_arr:
        register_routes(app, routes)


def register_routes(app, routes):
    for route in routes:
        app.register_blueprint(route)


def param(field, request):
    if request.method == "GET":
        return request.args.get(field)
    elif request.method == "POST":
        return request.json.get(field)
    raise Exception("不支持这种请求方法")


def param_list(field, request):
    if request.method == "GET":
        return request.args.getlist(field)
    elif request.method == "POST":
        return request.json.get(field)
    raise Exception("不支持这种请求方法")
