from os import system
from product_repository import ProductRepository


repository = ProductRepository.build()

while True:
  print("Criador de produto")

  name  = input("Nome: ")
  description = input("Descrição: ")
  price = float(input("Preço: "))

  product_data = { "name": name, "description": description, "price": price }
  repository.create(product_data)
  system("clear")