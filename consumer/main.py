from product import Product
from product_repository import ProductRepository
from kafka import KafkaConsumer


repository = ProductRepository.build()

for message in KafkaConsumer('products.create'):
  product = Product.build_from_json(message.value)
  print(f"Salvando \"{product.name}\"")
  repository.save(product)