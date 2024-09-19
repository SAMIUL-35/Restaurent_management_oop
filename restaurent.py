from Menu import menu
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


