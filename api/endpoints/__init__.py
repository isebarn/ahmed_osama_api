from flask import Blueprint
from flask_restx import Api, fields
# Subpaths
from .rating import api as rating_api
from .urls import api as urls_api

blueprint = Blueprint('', __name__)
api = Api(blueprint, doc='/doc/')

# Add imported subpaths to api
api.add_namespace(rating_api)
api.add_namespace(urls_api)
