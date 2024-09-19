from abc import ABC
from Order import order


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = order()

    def view_menu(self, Restaurant):
        Restaurant.menu.show_menu_item()

    def add_cart(self, Restaurant, item_name, quantity):
        item = Restaurant.menu.find_item(item_name)
        if item is not None:
            item.quantity = quantity
            self.cart.add_item(item)
            print("Added item")
        else:
            print("Item not found")

    def view_cart(self):
        print("***** View Cart *****")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t {item.price}\t {quantity}')
        print("Total:", self.cart.total_price())

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, Restaurant, employee):
        Restaurant.add_employee(employee)
    
    def view_employees(self, Restaurant):
        Restaurant.view_employees()

    def add_menu(self, Restaurant, item):
        Restaurant.menu.add_menu(item)

    def remove_item(self, Restaurant, item):
        Restaurant.menu.remove_item(item)




