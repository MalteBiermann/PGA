from math import sin,cos,atan2,pi
from datentyp.punkt import Punkt
from datentyp.strecke import Strecke
from datentyp.winkel import Winkel


def erste(p1, p12_s, p12_t):
    __y2 = p1.get_y() + (p12_s.länge() * sin(p12_t.get_w()))
    __x2 = p1.get_x() + (p12_s.länge() * cos(p12_t.get_w()))
    return Punkt(__y2, __x2)

def zweite(p0,p1):
    dy = p1.get_y() - p0.get_y()
    dx = p1.get_x() - p0.get_x()
    t = atan2(dy, dx)
    if t < 0:
        t = 2*pi + t
    s = Strecke.init_koor(p0.get_y(),p0.get_x(),p1.get_y(),p1.get_x()).länge()
    return s, Winkel(t, "rad")