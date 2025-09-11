# class order:
#     def __init__(self,order_id,items,amount):
#       self.order_id=order_id
#       self.items=items
#       self.amount=amount
#     def show_order(self) :
#        tax=50
#        total=self.amount+tax
#        print(f"{self.order_id}")
#        print(f"{self.items}")
#        print(f"{self.amount}rupees")
#        print(f"your total amount is:{total}")
# class delivery(order):
#    def __init__(self, order_id, items, amount):
#       super().__init__(order_id, items, amount)
#    def show_delivery(self):
#       super().show_order()
#       print(f"Order {self.order_id} is out for delivery")
# menu = {
#     "chicken biryani": 250,
#     "chicken manchuria": 100,
#     "veg biryani": 200
# }
# order1 = delivery(order_id=101, items=["chicken biryani", "chicken manchuria"], amount=menu["chicken biryani"] + menu["chicken manchuria"])
# order1.show_delivery()

# class product:
#    def __init__(self,name,price,category):
#       self.name=name
#       self.price=price
#       self.category=category
#    def show_product(self):
#       platform="Amazon"
#       print(f"{self.name}")
#       print(f"{self.price}")
#       print(f"{self.category}")
# class DiscountedProduct(product):
#    def __init__(self,name,price,category):
#       super().__init__(name,price,category)
#    def show_product(self,discount_percentage):
#       super().show_product()
#       final_price = self.price - (self.price * discount_percentage / 100)
#       print(final_price)
# product_details=DiscountedProduct("hp",45000,"laptop")
# product_details.show_product(10)



class Ride:
   def __init__(self,ride_id, pickup, drop):
      self.ride_id=ride_id
      self.pickup=pickup
      self.drop=drop
   def show_ride(self):
      distance=12
      print(f"Ride ID:{self.ride_id}")
      print(f"Pickup: {self.pickup}")
      print(f"Drop: {self.drop}")
      print(f"Distance: {distance} km")

class Driver(Ride):
   def show_driver(self):
      super().show_ride()
      print("Driver is assigned for your ride.")
driver_status = Driver(101, "Kukatpally", "Madhapur")
driver_status.show_driver()







    