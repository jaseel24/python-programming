print("\n list of integers \n")
list1=[-1,-2,-3,-4,5,6,7,4]
listp=[]
for n in list1:
    print(n,end=" ")
print("\n +ve integers are \n")
for n in list1:
    if n>0:
        listp.append(n)
for n in listp:
    print(n,end=" ")
