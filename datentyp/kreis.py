if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.punkt import Punkt


class Kreis:
    def __init__(self, mp, r):
        self.__mp = mp
        self.__r = r

    def get_mp(self):
        return self.__mp

    def get_r(self):
        return self.__r

    def set_mp(self, mp):
        self.__mp = mp

    def set_r(self, r):
        self.__r = r

    def __str__(self):
        return "Kreis MP: " + str(self.__mp) + " Radius: " + str(self.__r)


if __name__ == "__main__":
    mipu = Punkt(1, 1)
    c = Kreis(mipu, 1)
    print(c)
