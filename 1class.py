class Apple:
    size="Medium"
    def __init__(self,colo,flavour):
    
        self.color=colo
        self.flavour=flavour
    def func(self):
        self.cost=250
        return "Apples are {1}, {0} and size is {2}".format(self.cost,self.flavour,self.size)
    def fun2(self):
        return "second example{} and {}".format(self.color,self.size)
    def __str__(self):
        return "second {} and {}".format(self.color,self.size)
fruit=Apple("red","sweet")
print(fruit.func())
print(fruit.fun2())
print(fruit)




