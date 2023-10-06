a=int(input("enter limit oflist \n"))
i=0
lst=[]
while i<a:
    z=int(input("enter number"))
    if z>100:
        lst.append("Over listed")
    else:
        lst.append(z)
    i+=1
print(lst)
