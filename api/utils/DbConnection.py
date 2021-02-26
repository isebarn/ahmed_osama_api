import os
import pymongo
from app_constants import databases
from multipledispatch import dispatch

def client():
  mongodb_server   = os.environ.get('MONGODB_SERVER')
  mongodb_port     = int(os.environ.get('MONGODB_PORT'))
  mongodb_username = os.environ.get('MONGODB_USERNAME')
  mongodb_password = os.environ.get('MONGODB_PASSWORD')
  db_connection = pymongo.MongoClient(mongodb_server, mongodb_port)
  if mongodb_username and mongodb_password:
    db_connection.the_database.authenticate(mongodb_username, mongodb_password, source='admin')
  return db_connection

def get_collection(collection_name):
  collection = databases.get(collection_name, None)
  if collection is not None:
    return client()[collection.get('database')][collection.get('collection')]
