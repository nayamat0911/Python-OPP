"""a =20
b= "bangladesh"
print(type(a))
print(type(b))
print(a+2)
class Carton():
    "this is name Carton class syntext"
    series = "Tv series"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)


ob1=Carton("akash",39)
ob2 = Carton("jamal",34)
ob3 = Carton("hanof",95)

ob1.address= 'shaitshala'

print(ob1.name)
print(ob1.age)
print(ob1.address)
print(ob1.series)
print("-------ob1--------")
ob1.show()
print("-------ob2--------")
ob2.show()
print("-------ob3--------")
ob3.show()
print(3%5)
print(4+3%5)
print(Carton.__doc__)
print(ob1.__dict__)
print("Method=============")

class Human:
    def __init__(self,name):
        self.name = name

    #instance method
    def show_name(self):
        print(self.name)
    @classmethod
    def info(cls):
        print(cls.name)

    @staticmethod
    def info_details():
        print("this s static")


human=Human("nobita")
# humam.show_name()
# humam.info()
#instance method
Human.show_name("Nobita")
# class methed
# Human.info("Nobita")
Human.info_details()
"""
class Shunchan:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

class Minuka(Shunchan):
    def __init__(self, name, age, food):
        super().__init__(name,age)
        self.food = food

    def show_nam(self):
        print(self.name)

    def show_ag(self):
        print(self.age)

    def show_fod(self):
        print(self.food)


class Jishuka(Minuka):
    def __init__(self ,name, age, food, pet):
        super().__init__(name,age,food)
        self.pet = pet

    def show_pet(self):
        print(self.pet)


shunchan =Shunchan('dog', 30,)
print("---shunchan--")
shunchan.show_name()
shunchan.show_age()

minok = Minuka('cat', 30, 'backboon')
print("----minok----")
minok.show_nam()
minok.show_age()
minok.show_fod()

print('----------jishuka---------')
jishuk = Jishuka('manki',60, 'junk', 'pen')
jishuk.show_name()
jishuk.show_age()
jishuk.show_fod()
jishuk.show_pet()