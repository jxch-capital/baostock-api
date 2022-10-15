from flask import Flask
from util.flask_util import register_routes_arr
from route import routes
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
register_routes_arr(app, routes)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
