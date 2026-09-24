import sqlite3

db = sqlite3.connect("store.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")

db.commit()


def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    db.commit()
    print("Товар добавлен")


def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    for product in products:
        print(product)


def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    db.commit()
    print("Цена изменена")


def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    db.commit()
    print("Товар удален")


create_product("Телефон", 30000, 5)
create_product("Ноутбук", 60000, 3)
create_product("Наушники", 5000, 10)

print("Все товары:")
read_products()

update_product(1, 25000)

print("После изменения:")
read_products()

delete_product(2)

print("После удаления:")
read_products()

db.close()