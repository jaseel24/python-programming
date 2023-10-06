a=input("enter sentence \n")
b=input("Enter the word to search \n")
lst=a.split()
count=0

for n in lst:
    if n==b:
        count+=1
print("number of",n,"is",count)
