from flask_restx import Resource
from flask_restx import fields
from flask_restx import Namespace
# Query methods
from queries.urls import get_url_list

api = Namespace("urls", description="urllists")

@api.route("/url_list")
class UrlList(Resource):
  def get(self):
    return get_url_list({}, api.payload)