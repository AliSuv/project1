class Animal():
    
    def __init__(self, height, weight, cardivor = False):
        self.height = height
        self.weight = weight
        self.cardivor= cardivor
    
    def eat(self):
        if self.cardivor == True:
            print("I eat meat")
        else:
            print("I don't eat meat")

    def speak(self):
        pass

    def reverse_wh(self):
        self.weight, self.height = self.height, self.weight
    
class Cat(Animal):
    
    def __init__(self, height, weight, cardivor):
        super().__init__(height, weight, cardivor)
        self.cardivor = cardivor
 
    def speak(self):
        print("meow")

class Eagle(Animal):
    def __init__(self, height, weight, cardivor):
        super().__init__(height, weight, cardivor)
        self.cardivor = cardivor

    def speak(self):
        print("eeeeeeeeeee")

parent = Animal(12, 10)
child1 = Cat(19, 17, True)
child2 = Eagle(31, 24, True)

parent.eat()
child1.eat()

print(child1.height)
child1.height = 100
print(child1.height)

print(child2.height, child2.weight)
child2.reverse_wh()
print(child2.height, child2.weight)

# trida TVAR a budou dedit CTVEREC, TROJUHELNIK, KRUH kazdy tvar bude mit sve vlastnosti(kazde jine)
# kazdy tvar bude pocitat svuj obsah a obvod a ten vypsat 



