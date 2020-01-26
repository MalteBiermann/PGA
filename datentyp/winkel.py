from math import pi


class Winkel:
    def __init__(self, w, einheit="rad"):
        if einheit == "gon":
            self.__w = self.gon2rad(w)
        elif einheit == "grad":
            self.__w = self.grad2rad(w)
        else:
            self.__w = w

    def get_w(self):
        return self.__w

    def set_w(self, w):
        self.__w = w

    def __str__(self):
        return str(self.get_w()) + " rad"

    def grad2rad(self, grad):
        return grad * pi / 180

    def grad2gon(self, grad):
        return grad * (10/9)

    def rad2grad(self, rad):
        return rad / pi * 180

    def gon2grad(self, gon):
        return gon / (10 / 9)

    def rad2gon(self, rad):
        return rad / pi * 200

    def gon2rad(self, gon):
        return gon * pi / 200


if __name__ == "__main__":
    w0 = Winkel(90, "grad")
    print("W", w0.get_w())
