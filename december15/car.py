class Car:
    def __init__(self,color,price,kilometer):
        self.color=color
        self.price=price
        self.kilometer=kilometer
    

c1=Car("black",120000,16100)
c2=Car("red",110000,16700)

if(c1.price>c2.price):    
    print("price of car 1 is greater:",c1.price)
print("kilometer of both cars:",c1.kilometer+c2.kilometer)
