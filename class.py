# # class name :
# # statement or block
# class Cartorn:
#     pass  #use for empty class
#
# # create a object
# ob1 = Cartorn()
# ob2 = Cartorn()
#
# ob1.name = "doremon"
# ob1.age = 10
# ob2.name = "shinchang"
# ob2.age = 12
#
# print(ob1.name)
# print(ob1.age)
#
# print('shinshun class---')
# print(ob2.name)
# print(ob2.age)
#
# # class variable
# class Cartorn1:
#     serise  = "tv serise"
#
# obj3 = Cartorn1
# print(obj3.serise)

# init function or constractur
# it use for recive any statement from class
class Cartorn:
    """this is the Tv sereise
    this is best cartorn"""
    serise  = "tv serise"

    def __init__(hp, name1, age1):
        hp.name1 = name1
        hp.age1 = age1

    def show(pk):
        print(pk.name1)
        print(pk.age1)
        print(pk.serise)

print(Cartorn.__doc__) # its use for developer note or its use for help understande the class method code note


obj4 = Cartorn("shinshun", 20)
obj5 = Cartorn("rajuk", 22)
obj6 = Cartorn("nobita", 25)

# dectionary method
#its use for understande whice is use in side the object"
print(obj6.__dict__)

#change/update method
obj4.age1 = 90
# delete object property
del obj6.age1

# delete object
del obj5

#  building method


obj4.show()
obj5.show()
obj6.show()

# print(obj4.name1)
# print(obj4.age1)
# print(obj4.serise)
# print("-------")
# print(obj5.name1)
# print(obj5.age1)
# print(obj5.serise)
# self perameter
# its work for object receive
# self pera meter na hoye onno je kono kico diley hobe
# its not mandatory that to use only self perameter , we can use any word alternate word as a self
# but its main works to receice object

