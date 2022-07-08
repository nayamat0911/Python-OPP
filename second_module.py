from first_modiule import Human

class Animal(Human):
    def __init__(self,name, age,food,pet):
        super(Animal, self).__init__(name,age, food)
        self.pet = pet

    def show_pet(self):
        print(self.pet)