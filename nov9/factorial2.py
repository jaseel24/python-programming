def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
f=int(input("enter number to find the factorial"))
f=fact(f)
print("the factorial is: ",f)
