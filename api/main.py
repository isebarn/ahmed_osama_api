from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS

from endpoints import blueprint as api


app = Flask(__name__)
CORS(app)
app.config["PROPAGATE_EXCEPTIONS"] = False
app.url_map.strict_slashes = False
app.register_blueprint(api)

