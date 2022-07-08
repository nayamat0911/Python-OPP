# class Robot:
#     def __init__(self, name):
#         self.name = name
#
#     def show_name(self):
#         print(self.name)
#         print("Robot class")

class Human:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(self.name)
        print("Human class")

    class Robot:
        def __init__(self, name):
            self.name = name

        def show_name(self):
            print(self.name)
            print("Robot class")

        class Sajo:
            def __init__(self, name):
                self.name = name

            def show_Sajo(self):
                print(self.name)
                print("Sajo class")

    class Robo(Robot):
        def __init__(self, name):
            self.name = name

        def show_robo(self):
            print(self.name)
            print("Robo class")

# robot = Robot("Sophiya")
# robot.show_name()


human = Human("Nobita")
human.show_info()
robot = human.Robot("Rokaiya from robot class")
robot.show_name()

robo = human.Robo("I am from Robo")
robo.show_robo()
robo.show_name()

sajo = robot.Sajo(" i am Sajo from subclass of Robot")
sajo.show_Sajo()
dajo = human.Robot.Sajo("Sajoooooooooooooo")
dajo.show_Sajo()