def getdata(Id, name):
    print("Id: ",Id)
    print("name: ",name)



n=int(input("how many data you want to enter?")) 

for i in range(n):
    id = input("Enter your ID: ")
    name = input("Enter your name: ")
    getdata(id,name)
