file = open("myfile.txt", "r") 

print("Initial cursor position:", file.tell())  
data = file.read(10) 
print("After reading 10 characters:", file.tell())  

file.close()  
