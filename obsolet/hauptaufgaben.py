from math import pi, sin, cos, sqrt, atan2


def erstegga(Y1, X1, s, t):
    Y2 = Y1 + (s * sin(t))
    X2 = X1 + (s * cos(t))
    return Y2, X2


def zweitegga(Y1, X1, X2, Y2):
    dY = Y2 - Y1
    dX = X2 - X1
    s = sqrt((dY ** 2 + dX ** 2))
    t = atan2(dY, dX)
    if t < 0:
        t = 2*pi + t
    return s, t
