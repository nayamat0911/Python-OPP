# from first_modiule import Robot
# from first_modiule import Robot as R
# from first_modiule import Human as H
import first_modiule as f

from second_module import Animal

# robot = Robot("Sophiya","7 years ")
# robot = R("Sophiya","7 years ")
# huamn = H("Shinshun","8 yeras","mango")
robot = f.Robot("Sophiya","7 years ")
huamn = f.Human("Shinshun","8 yeras","mango")
animal = Animal("cat","8 yeras","milk","pt")

robot.show_name()
robot.show_age()

print("-"*5,"Human","-"*5)
huamn.show_name()
huamn.show_age()
huamn.show_food()

animal.show_name()
animal.show_age()
animal.show_food()
animal.show_pet