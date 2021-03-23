from utils.DbConnection import get_collection
from pandas import read_csv
from random import choice

def get_url_list(aggregate, filters):
  data = read_csv("data.csv")

  # mongodb
  checked = [x['look_id']
    for x in get_collection().find({}, {"look_id": 1})]

  look_id = choice([x for x in data.look_id.to_list() if x not in checked])
  result = list(data[data.look_id == look_id].T.to_dict().values())

  # size on site
  list(map(lambda x: x.update({'flex': 6}), result))
  if len(result) % 2 != 0:
    result[0].update({'flex': 12})

  return {
    "style": result,
    "checked": len(checked)
  }
