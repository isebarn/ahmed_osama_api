from utils.DbConnection import get_collection

def get_rate(data):
  get_collection().insert(data)