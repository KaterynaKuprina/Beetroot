class Product:
    def __init__(self, type_, name, price):
        self.type_ = type_
        self.name = name
        self.price = price

    def __str__(self):
        pass

class ProductStore:
    def __init__(self):
        self.warehouse = {}
        self.income = 0

    def add(self, product: object, amount: int):
        product.price = product.price * 1.3
        self.warehouse[product.name] = {
        "type_": product.type_,
        "price": product.price,
        "amount": amount
        }


    def set_discount(self, identifier, percent, identifier_type="name"):
        for key, value in self.warehouse.items():
            if identifier == value["type_"] or identifier_type == key:
                value["price"] *= 1 - percent / 100

    def sell_product(self, product_name, amount):
        if product_name in self.warehouse:
            if self.warehouse[product_name]["amount"] >= amount:
                self.warehouse[product_name]["amount"] -= amount
                self.income += self.warehouse[product_name]["price"] * amount
            else:
                raise ValueError("Not enought product in warehouse")
        else:
            raise IndexError("Wrong store")


    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.warehouse

    def get_product_info(self, product_name):
        if product_name in self.warehouse:
            return product_name, self.warehouse[product_name]["amount"]
        else:
            raise ValueError("Go home")


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product("Food", 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)