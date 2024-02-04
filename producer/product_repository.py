from json import dumps
from kafka import KafkaProducer


def _value_serializer(value):
    return dumps(value).encode('utf-8')

class ProductRepository:
  __CREATE_TOPIC = "products.create"

  @classmethod
  def build(cls):
    return ProductRepository()

  def create(self, product_data):
    producer = KafkaProducer(value_serializer=_value_serializer)

    producer.send(topic=self.__CREATE_TOPIC, value=product_data)