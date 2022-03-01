print("Nested Class")


class Human:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(self.name)


    class Robot:
        def __init__(self, name):
            self.name = name

        def show_name(self):
            print(self.name)

        class Robo:
            def __init__(self,details):
                self.details = details
            def show_details(self):
                print(self.details)

class Humana(Human):
    def __init__(self, name):
        self.name = name

    def show_home(self):
        print(self.name)


    class Robona():
        def __init__(self, name):
            self.name = name

        def show_cat(self):
            print(self.name)
            print("I am cat")


print('--------human---------')
huamn = Human("I am Huamn")
huamn.show_info()


print('---robot----')
robot=huamn.Robot("I am ROBOT")
robot.show_name()
# huamn.Robot.show_name()

print('-----Robo------')
# robo = huamn.Robot.Robo("I am ROBO class")
# robo.show_details()
robo = robot.Robo('Ami Robo class')
robo.show_details()

huma=Humana(" I am From Humana")
huma.show_info()
himo = Humana.Robot.Robo("Hi Robo")
himo.show_details()
huma.show_home()
# huma.Robona.show_cat()
humaei=Humana.Robona("I am From Robana cat")
humaei.show_cat()

print('nested class')