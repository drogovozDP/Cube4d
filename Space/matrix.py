import numpy as np
from numpy import sin, cos
from Space.constants import KZ, KW


"""
P0 and P1 are projection matrix. Digit in the end means that which dimension we transfer from
For example: 
    x14 = (x, y, z, w, 1),  xi4 @ P1 = xi3 = (x/H, y/H, z/H, 0, 1)
    x13 = (x/H, y/H, z/H, 0, 1),  xi3 @ P0 = xi2 = (x/(HG), y/(HG), 0, 0, 1) 
"""


P0 = np.array([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, KZ],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
])

P1 = np.array([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, KW],
    [0, 0, 0, 0, 1]
])


def rotate(axis, a):
    R = np.eye(4)
    if axis == "xw":
        R = np.array([[1,      0,      0,  0, 0],
                      [0, cos(a), sin(a),  0, 0],
                      [0, -sin(a), cos(a), 0, 0],
                      [0,       0,      0, 1, 0],
                      [0,       0,      0, 0, 1]])
    elif axis == "yw":
        R = np.array([[cos(a), 0,  sin(a), 0, 0],
                      [0,      1,       0, 0, 0],
                      [-sin(a), 0, cos(a), 0, 0],
                      [0,       0,      0, 1, 0],
                      [0,       0,      0, 0, 1]])
    elif axis == "zw":
        R = np.array([[ cos(a), sin(a), 0, 0, 0],
                      [-sin(a), cos(a), 0, 0, 0],
                      [0,    0,      1,    0, 0],
                      [0,    0,      0,    1, 0],
                      [0,    0,      0,    0, 1]])

    elif axis == "xy":
        R = np.array([[1, 0,       0,      0, 0],
                      [0, 1,       0,      0, 0],
                      [0, 0,  cos(a), sin(a), 0],
                      [0, 0, -sin(a), cos(a), 0],
                      [0, 0,       0,      0, 1]])

    elif axis == "xz":
        R = np.array([[1,       0, 0,      0, 0],
                      [0,  cos(a), 0, sin(a), 0],
                      [0,       0, 1,      0, 0],
                      [0, -sin(a), 0, cos(a), 0],
                      [0,       0, 0,      0, 1]])

    elif axis == "yz":
        R = np.array([[cos(a),  0, 0, sin(a), 0],
                      [0,       1, 0,      0, 0],
                      [0,       0, 1,      0, 0],
                      [-sin(a), 0, 0, cos(a), 0],
                      [0,       0, 0,      0, 1]])

    return R


def move(x, y, z, w):
    return np.array([[1, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 0, 1, 0],
                     [x, y, z, w, 1]])
