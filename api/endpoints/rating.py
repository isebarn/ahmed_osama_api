from flask_restx import Resource
from flask_restx import fields
from flask_restx import Namespace
# Query methods
from queries.rating import get_rate

api = Namespace("rating", description="ratings")

@api.route("/rate")
class Rate(Resource):
  def post(self):
    return get_rate(api.payload)