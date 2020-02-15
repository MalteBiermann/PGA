from math import pi


class Winkel:
    def __init__(self, w=0, einheit="rad"):
        if einheit == "gon":
            self.__w = self.gon2rad(w)
        elif einheit == "grad":
            self.__w = self.grad2rad(w)
        else:
            self.__w = w

    def get_w(self, einheit="rad"):
        if einheit == "gon":
            wresult = self.rad2gon(self.__w)
        elif einheit == "grad":
            wresult = self.rad2grad(self.__w)
        else:
            wresult = self.__w
        return wresult

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

    def neg2pos(self):
        if self.__w < 0:
            self.__w += 2*pi

    def get_json(self):
        return self.__dict__

    def set_json(self, p_dic):
        for k, v in p_dic.items():
            if(hasattr(self,k)):
                setattr(self, k, v) 


if __name__ == "__main__":
    w0 = Winkel(90, "grad")
    print("W", w0.get_w())
    print(w0.get_w("gon"))
