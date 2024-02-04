from json import loads


class Product:
  @classmethod
  def build_from_json(cls, json_data):
    data = loads(json_data)
    id = None
    name = data["name"]
    description = data["description"]
    price = data["price"]

    try:
      id = data["id"]
    except KeyError:
      pass

    return Product(name, description, price, id=id)

  def __init__(self, name, description, price, id=None):
    self.__id = id
    self.__name = name
    self.__description = description
    self.__price = price

  @property
  def id(self):
    return self.__id

  @property
  def name(self):
    return self.__name

  @property
  def description(self):
    return self.__description

  @property
  def price(self):
    return self.__price