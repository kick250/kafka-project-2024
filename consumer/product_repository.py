import psycopg2


class ProductRepository:
  @classmethod
  def build(cls):
    conn = psycopg2.connect(
      host='localhost',
      database='products_database',
      user='postgres',
      password='admin'
    )
    return ProductRepository(conn)

  def __init__(self, conn):
    self.conn = conn

  def save(self, product):
    cursor = self.conn.cursor()
    cursor.execute(self.__build_insert_sql(product))
    self.conn.commit()

  def __build_insert_sql(self, product):
    return f"INSERT INTO products (name, description, price) VALUES ('{product.name}', '{product.description}', {product.price});"