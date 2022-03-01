from abc import ABC,abstractmethod
class Father(ABC): #abstract class
    @abstractmethod #abstract method
    def go_school(self):
        pass
        # print("haa, school e gesi")
    @abstractmethod
    def go_collage(self):
        pass

    #concret method
    def result(self):
        print("Ha result dise")


class Nobita(Father):
    def go_school(self):
        super(Nobita, self).result()
        print("Haa , school e gesi")

    def go_collage(self):
        print(self)
        print("Haaaa collage e gesi")

    def playing(self):
        print("Playing Football")

    def singing(self):
        print("sining")


# father =Father()
# father.go_school()
nobita = Nobita()
nobita.go_collage()
nobita.go_school()
nobita.playing()
nobita.singing()

