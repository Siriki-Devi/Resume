# import requests
# apiurl="https://jsonplaceholder.typicode.com/users"
# response=requests.get(apiurl)
# class user:
#     def __init__(self,id,name,email):
#         self.id=id
#         self.name=name
#         self.email=email
#     def  showUser(self):
#         print(f"{self.id}")
#         print(f"{self.name}")
#         print(f"{self.email}")
#     def getEmailDomain(self):
#         return self.email.split("@")[1]
# if response.status_code==200:
#     data=response.json()
# users=[]
# for i in data[:5]:
#     object=user(i['id'], i['name'], i['email'])
#     users.append(object)
#     object.getEmailDomain()
#     object.showUser()


# import requests
# apiurl="https://jsonplaceholder.typicode.com/posts"
# response=requests.get(apiurl)
# class Posts:
#     def __init__(self,userId, id, title, body):
#         self.userid=userId
#         self.id=id
#         self.title=title
#         self.body=body
#     def showSummary(self):
#         print(f"{self.id} → {self.title[:20]}...")
#     def getWordCount(self):
#         count = len(self.body.split())
#         print(f"Word Count: {count}")
# if response.status_code==200:
#     data=response.json()
#     for i in data[:3]:
#         object=Posts(i['userId'],i['id'],i['title'],i['body'])
#         object.getWordCount()
#         object.showSummary()


import requests
apiurl="https://dummyjson.com/products"
response=requests.get(apiurl)
class Product:
    def __init__(self, id, title, price, stock):
        self.accept_id=id
        self.title=title
        self.price=price
        self.stock=stock
    def showDetails(self):
        print(f"{self.accept_id}")
        print(f"{self.title}")
        print(f"{self.price}")
    def  buyProduct(self,qty):
        self.qty=qty
        if  self.stock>qty:
           self.stock-=qty
           print(f"Bought {qty} {self.title}(s). Remaining stock: {self.stock}")
        else:
           print("out of stock")
if response.status_code==200:
    data=response.json()
    products=[]
for i in data['products']:
    object=Product(i['id'],i['title'],i['price'],i['stock'])
    products.append(object)
for p in products:
    p.buyProduct(2)
    p.showDetails()
    print("------")







