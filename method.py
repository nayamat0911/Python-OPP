# print("hello world")

class Human:
    def __init__(self, name):
        self.name = name

    # Instance method
    def show_name(self):
        print(self.name)
    # instance method
    def info(hey):
        print(hey.name)

    @classmethod
    def class_method(cls):
        print("this is class method")
    @staticmethod
    def sttic_metod():
        print("this is static maethd")


human = Human("Nobita")
human.show_name()
# human.name()
human.info()
# Human.show_name()

# class method
Human.class_method()

# human.class_method("Doreeemoooon")

Human.sttic_metod()