from abc import ABC

class User(ABC):
    def __init__(self,name,phone,Email,address) :
        self.name=name
        self.phone=phone
        self.Email =Email
        self.address =address

class Employee(User):
    def __init__(self, name, phone, Email, address,age,designation,salary):
        super().__init__(name, phone, Email, address)
        self.age =age
        self.designation =designation
        self.salary = salary

    
class Admin(User):
    def __init__(self, name, phone, Email, address):
        super().__init__(name, phone, Email, address)
        self.employees = []

    def add_employee(self, name, phone, Email, address,age,designation,salary):
        employee=Employee( name, phone, Email, address,age,designation,salary)
        self.employees.append(employee)
    
    def view_employees(self):
        for emp in self.employees:
            print("Name: ", emp.name)
            print("Phone: ", emp.phone)
            print("Email: ", emp.Email)
            print("Address: ", emp.address)
            print("Age: ", emp.age)
            print("Designation: ", emp.designation)
            print("Salary: ", emp.salary)
            print("--------------------")

ad=Admin('samiul','016861448','sami34@','dhaka')
ad.add_employee('kanok','01558','sjjdjj@','ctg',25,'tech',25000)
ad.show_all_employee()