lst=["raju","aju","revi","chandhu"]
count=0
print(lst)
a=input("enter the letter to find the occurence \n")
for n in lst:
    for f in n:
        if f==a:
            count+=1
print("Number of",a,"is",count)
