# supper mthod

class Robot:
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

class Human():
    def __init__(self,name,age,food):
        # super(Human, self).__init__(name,age)
        self.name = name
        self.age = age
        self.food = food

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    def show_food(self):
        print(self.food)

class Animal(Human,Robot):
    def __init__(self, name,age,food,pet):
        super(Animal, self).__init__(name,age,food)
        # self.name = name
        # self.age = age
        # self.food = food
        self.pet = pet

    # def show_name(self):
    #     print(self.name)
    #
    # def show_age(self):
    #     print(self.age)

    # def show_food(self):
    #     print(self.food)

    def show_pet(self):
        print(self.pet)



robot = Robot("Sophiya",'6 years')
human = Human("Shinchan","5 years ","mango")
animal = Animal("Cat","2 years","milk","Flay")


print("-"*7,"Robot","-"*7)
robot.show_name()
robot.show_age()


print("-"*5,"Human","-"*5)
human.show_name()
human.show_age()
human.show_food()


print("-"*5,"Animal","-"*5)
animal.show_name()
animal.show_age()
animal.show_food()
animal.show_pet()