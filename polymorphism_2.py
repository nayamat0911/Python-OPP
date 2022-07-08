# polymorphic means bohorophi
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

human = Human("I am from Human")
human.show_info()
roobot = Robot("i ama from robot")
roobot.show_name()