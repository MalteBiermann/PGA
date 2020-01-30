from math import pi, sin, cos, sqrt, atan2


def grad2rad(grad):
    return (grad * pi / 180)


def grad2gon(grad):
    return (grad * (10/9))


def rad2grad(rad):
    return (rad / pi * 180)


def gon2grad(gon):
    return (gon / (10 / 9))


def rad2gon(rad):
    return (rad / pi * 200)


def gon2rad(gon):
    return (gon * pi / 200)
