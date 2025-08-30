import requests
apiurl = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(apiurl)
print(response.status_code)
if response.status_code==200:
    data=response.json()
    total_posts = len(data) 
    print("Total posts returned:", total_posts)
    for i in data:
        if i["id"]==15 :
            print(i["title"])
    count = 0   
    for i in data:
        if i["userId"] == 3:
            count += 1
            print("UserId:", i["userId"])   
    print("Total posts by userId=3:", count)
    for i in data:
        if i["id"]==50:
            print(i["title"],i["body"]) 
    for i in data:
        if i["userId"]==7:
            print(i["id"]) 
    total_users = len(data) 
    print("Total users returned:", total_users) 




import requests
apiurl = "https://jsonplaceholder.typicode.com/users"
response = requests.get(apiurl)
print(response.status_code)
if response.status_code==200:
 data=response.json()
 total_users = len(data) 
 print("Total users returned:", total_users)
 for i in data:
  if i["id"]==5:
   print(i["name"],i["email"])
 for i in data:
  if i["username"]=="Bret":
    print("User found:", i)
 for i in data:
  if i["address"]["city"]=="South Christy":
    print(i["name"])
 for i in data:
  if "Group" in i["company"]["name"]:
    print(i["id"],i["name"])




import requests
apiurl = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(apiurl)
print(response.status_code)
if response.status_code==200:
 data=response.json()
total_todos = len(data) 
print("Total todos returned:", total_todos)
for i in data:
   if i["id"]==42:
    print(i["title"])
for i in data:
   if i["userId"]==3:
     print("belongs todos to that userid is:",i)
for todo in data:
    if todo["completed"] == False:   
         print(todo["id"])
count=0
for i in data:
    if i["userId"]==5 and i["completed"] == True: 
         count+=1  
print("count true id's",count)


    
  
  
    
