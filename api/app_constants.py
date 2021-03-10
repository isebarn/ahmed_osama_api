import os

databases = {
  "collection": {
    "database": os.environ.get('MONGODB_DB_NAME'),
    "collection": os.environ.get('MONGODB_COLLECTION')
  }
}

filter_maps = {

}
