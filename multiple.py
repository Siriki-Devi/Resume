# class Person:
#     def __init__(self,name,contact):
#         self.name=name
#         self.contact=contact
# class Driver:
#     def __init__(self,license_no,rating):
#         self.license_no=license_no
#         self.rating=rating
# class  UberDriver(Person,Driver):
#     def __init__(self, name, contact,car,license_no,rating):
#         self.car=car
#         Person.__init__(self, name, contact)    
#         Driver.__init__(self, license_no, rating) 
#     def showDetails(self):
#         print("Name:", self.name)
#         print("Contact:", self.contact)
#         print("License:", self.license_no)
#         print("Rating:", self.rating)
#         print("Car:", self.car)

# d1 = UberDriver("Rahul", "9876543210", "DLX12345", 4.9, "Hyundai i20") 
# d1.showDetails()


class Person:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
class Employee:
    def __init__(self,emp_id, salary):
        self.emp_id=emp_id
        self.salary=salary
class DeliveryPartner(Person,Employee):
    def __init__(self, name, contact,emp_id, salary,vehicle):
        self.vehicle= vehicle
        Person.__init__(self, name, contact)    
        Employee.__init__(self,emp_id, salary) 
    def showDetails(self):
        print("Name:", self.name)
        print("Contact:", self.contact)
        print("emp_id:", self.emp_id)
        print("salary:", self.salary)
        print("vehicle:", self.vehicle)
dp1 = DeliveryPartner("Anil", "9876543210", "BKP101", 12000, "Scooter") 
dp1.showDetails()

