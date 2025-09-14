# class Restaurant:
#     def __init__(self, restaurant_name, menu):
#         self.restaurant_name = restaurant_name
#         self.menu = menu

#     def showMenu(self):
#         print(f"\n--- {self.restaurant_name} Menu ---")
#         for item, price in self.menu.items():   
#             print(f"{item} - ₹{price}")

#     def orderFood(self, item, qty):
#         if item in self.menu:  
#             total = self.menu[item] * qty
#             print(f"\nYou ordered {qty} {item}(s). Bill: ₹{total}")
#         else:
#             print("\nItem not available")


# dominos_menu = {
#     "Pizza": 200,
#     "Burger": 120
# }
# kfc_menu = {
#     "Chicken": 250,
#     "Fries": 100
# }

# dominos = Restaurant("Dominos", dominos_menu)
# kfc = Restaurant("KFC", kfc_menu)

# dominos.showMenu()
# dominos.orderFood("Pizza", 2)

# kfc.showMenu()
# kfc.orderFood("Fries", 3)



# class Driver:
#     def __init__(self,driver_name, car_model, per_km_rate):
#         self.driver_name=driver_name
#         self.car_model=car_model
#         self.per_km_rate=per_km_rate
#     def  showDriver(self) :
#         print(f"Driver: {self.driver_name}, Car: {self.car_model}, Rate: {self.per_km_rate}/km")
#     def  calculateFare(self,distance):
#         fare=distance*self.per_km_rate
#         print(f"Distance: {distance} km, Fare: {fare}")
# driver1 = Driver("Raj", "Swift", 20)
# driver2 = Driver("Kiran", "Innova", 25)
# driver3 = Driver("Meena", "Dzire", 18)
# driver1.showDriver()
# driver1.calculateFare(10)
# driver2.showDriver()
# driver2.calculateFare(9)
# driver3.showDriver()
# driver3.calculateFare(8)


class product:
    def __init__(self,product_name,price,stock):
        self.product_name=product_name
        self.price=price
        self.stock=stock
        
        
    def showDetails(self):
        print(f"{self.product_name}")
        print(f"{self.price} ")
        print(f"{self.stock}")
        
    def Product(self,qty):
        if self.stock >= qty:
            self.stock -= qty
            total = self.price * qty
            print(f"{qty} {self.product_name}(s) purchased for ₹{total}")
        else:
            print(f"Out of Stock! Only {self.stock} {self.product_name}(s) left.")
laptop=product("hp",50000,10)
shoes=product("nyke",1200,0)
phone=product("iphone",10000,12)
laptop.Product(2)
laptop.showDetails()
shoes.Product(3)
shoes.showDetails()
phone.Product(4)
phone.showDetails()



