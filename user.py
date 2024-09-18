from abc import ABC

class User(ABC):
    def __init__(self, name, phone, Email, address):
        self.name = name
        self.phone = phone
        self.Email = Email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, Email, address):
        super().__init__(name, phone, Email, address)
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
            print(f'{item.name} {item.price} {quantity}')
        print("Total:", self.cart.total_price())

class order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def clear_order(self):
        self.items.clear()

class Employee(User):
    def __init__(self, name, phone, Email, address, age, designation, salary):
        super().__init__(name, phone, Email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, Email, address):
        super().__init__(name, phone, Email, address)

    def add_employee(self, Restaurant, employee):
        Restaurant.add_employee(employee)
    
    def view_employees(self, Restaurant):
        Restaurant.view_employees()

    def add_menu(self, Restaurant, item):
        Restaurant.menu.add_menu(item)

    def remove_item(self, Restaurant, item):
        Restaurant.menu.remove_item(item)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = menu()  # Initialize the menu here

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employees(self):
        for emp in self.employees:
            print(f"Name: {emp.name}")
            print(f"Phone: {emp.phone}")
            print(f"Email: {emp.Email}")
            print(f"Address: {emp.address}")
            print(f"Age: {emp.age}")
            print(f"Designation: {emp.designation}")
            print(f"Salary: {emp.salary}")
            print("--------------------")

class menu:
    def __init__(self):
        self.items = []

    def add_menu(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print('Item deleted successfully')
        else:
            print('Item not found')

    def show_menu_item(self):
        for item in self.items:
            print(f'Item name: {item.name}')
            print(f'Item price: {item.price}')
            print(f'Item quantity: {item.quantity}')
            print('--------------------')

class fooditem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Example usage
mn = menu()
res = Restaurant("Mama's Restaurant")
ad = Admin('Samiul', '016861448', 'sami34@', 'Dhaka')
cus1 = Customer('Samiul', "555555", "sami34@", "Dhaka")
item1 = fooditem('Burger', 50, 10)
item2 = fooditem('Fries', 20, 15)

ad.add_menu(res, item1)
ad.add_menu(res, item2)

cus1.view_menu(res)
cus1.add_cart(res, 'Burger', 2)
cus1.view_cart()
