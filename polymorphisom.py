print("----polymorphisom---")
"""
class Rebot:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)
        print("robot class")

class Human():
    def __init__(self, name):
        self.name = name
    def show_name(self):
        print(self.age)

print("Robot---------")
robot= Rebot("I am Robot method")
# robot.show_name()

print('Human----------')
human=Human("I am Huamn Class")
# human.show_age()


for i in (robot,human):
    i.show_name()
"""
print("method overloading")

class Profile:
    def name(self, first=None,middle=None,last=None):
        if first != None and middle != None and last != None:
            print(first+" "+middle+" "+last)
        elif first != None and middle !=None:
            print(first+" "+middle)
        else:
            print(first)
p=Profile()
p.name("ahmed")
p.name("md","Marjuk","ahmed")
p.name("mohammed","siddik")