class Dorimoon:
    def doreamon_self(self):
        print("I am doreamon  class")

    def gadget(self):
        print("new gadget")

class Nobita():
    def nobtita_self(self):
        print('i am nobia own class')

    def nobita_gadget(self):
        print("nobita gadget")

class Shijuka(Nobita):
    def shijuka_self(self):
        print("i am shijuka class")


class Shown(Dorimoon, Nobita):
    def show_shown(self):
        print("I am shwon class")

doremon = Dorimoon()
nobita = Nobita()
# nobita.doreamon_self()
shijuka = Shijuka()
# shijuka.doreamon_self()
shijuka.shijuka_self()
shijuka.nobtita_self()
# shijuka.gadget()
shijuka.nobita_gadget()

shown = Shown()
shown.doreamon_self()
shown.nobita_gadget()
shown.gadget()

