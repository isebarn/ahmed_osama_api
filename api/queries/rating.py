from utils.DbConnection import get_collection
import os

def get_rate(data):
  get_collection(os.environ.get('MONGODB_COLLECTION')).insert(data)