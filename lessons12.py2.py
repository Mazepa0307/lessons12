class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}, description: {self.description}, size: {self.dimensions}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}, phone: {self.numberphone}"

class Purchase:
    def __init__(self, user):
        self.products = {}  # item -> кількість
        self.user = user

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt  # Якщо товар вже є, додаємо кількість
        else:
            self.products[item] = cnt  # Якщо товару ще немає, додаємо новий запис

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        product_str = "\n".join([f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()])
        return f"User: {self.user}\nItems:\n{product_str}\nTotal: {self.get_total()}"

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)  # lemon, price: 5
print(apple)  # apple, price: 2

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)

cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""
assert cart.get_total() == 40, 'Повинно залишатися 40!'
