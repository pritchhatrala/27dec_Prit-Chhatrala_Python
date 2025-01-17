math=int(input("Enter the mark of math :"))
science=int(input("Enter the mark of science: "))
physics=int(input("Enter the mark of physics: "))

total=math+science+physics
print ("Total :",total)
    
pr= total/4
print("PR :", pr)

if pr>=70:
    print("grade = A+ ")
elif pr>=60:
    print("grade = A")
elif pr>=50:
    print("grade = B")
elif pr>=40:
    print("grade = C ")
else:
    print("grade = F")