class Nobita:
    def __init__(self):
        self.book = "comics"
        self.no = 10
        self._no = 20
        self.__no = 30
        self.___no = 40
    def show_data(self):
        print( self.no ,self._no, self.__no,self.___no)

    def change_data(self):
        self.__no = 50
        print(self.__no)

class Sonio(Nobita):
    def show_nobita(self):
        print(self.no)
        # print("Sonio", self._nobita__no)


class Shijuka(Nobita):
    def show_nobita(self):
        print("SHijuka", self._no)

nobita = Nobita()
sonio = Sonio()
shijuka = Shijuka()
# nobita.no =35
nobita.show_data()
nobita.no =35
nobita.change_data()
sonio.show_nobita()
shijuka.show_nobita()
# print(sonio._nobita__no)


a=5
b=20
print(a+b)
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))

print("==============")
class Number:
    def __init__(self, no):
        self.no = no

    def __add__(self, jeita_seita):
        # return self.no + jeita_seita.no +1
        return "ja iccha ta"

    def show(self):
        print(self.no)

a = Number(3)
b = Number(3)
print(a+b)
print(a.__add__(b))

