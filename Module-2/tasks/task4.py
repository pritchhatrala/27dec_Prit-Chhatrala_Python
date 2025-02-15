file = open("stdata.txt","a")

count=int(input("how many student's data you want to add? "))

for i in range(count):
    id=input("enter your id:")
    name=input("enter your name: ")
    sub=input("enter your subject:")


    file.write(f"\nid={id}")
    file.write(f"\nname={name}")
    file.write(f"\nsubject={sub}")
    file.write("\n============================")