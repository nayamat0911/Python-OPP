# print("hello world")

class Human:
    # class variale
    class_va = "class variable"
    def __init__(self, name):
        # instance variavle
        self.name = name

    # Instance method
    def show_name(self):
        print(self.name)
        print(self.class_va)

    # instance method
    def info(hey):
        print(hey.name)

    @classmethod
    def class_method(cls):
        print("this is class method")
        print(cls.class_va)


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
human.show_name()
print(human.class_va)
print(Human.class_va)
human.class_method()

