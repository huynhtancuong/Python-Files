from math import sqrt
from math import acos
from math import degrees

class Vector():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.length = sqrt(x**2 + y**2 + z**2)

    def __str__(self):
        return "Vector: (%d, %d, %d)" % (self.x, self.y, self.z)

    def __add__(self, *other):
        "This function add two or more vector."
        for each in other:
            assert type(each) is Vector
        x = self.x
        y = self.y
        z = self.z
        for each in other:
            x += each.x
            y += each.y
            z += each.z
        return Vector(x, y, z)

    def __sub__(self, *other):
        "This function subtract two or more vector."
        for each in other:
            assert type(each) is Vector
        x = self.x
        y = self.y
        z = self.z
        for each in other:
            x -= each.x
            y -= each.y
            z -= each.z
        return Vector(x, y, z)

    def __mul__(self, *other):
        "This function multiply vector with number or vector with vector."
        x = self.x
        y = self.y
        z = self.z
        for each in other:
            if (type(each) is int):
                x *= each
                y *= each
                z *= each
            if (type(each) is Vector):
                x = self.y*each.z - each.y*self.z
                y = self.z*each.x - self.x*each.z
                z = self.x*each.y - each.x*self.y
        return Vector(x, y, z)

def center(vector1, vector2):
    return Vector((vector1.x+vector2.x)/2, (vector1.y+vector2.y)/2, (vector1.z+vector2.z)/2)

def tichvohuong(vector1, vector2):
    assert (type(vector1) is Vector) and (type(vector2) is Vector), 'Invalid input type.'
    return vector1.x*vector2.x + vector1.y*vector2.y + vector1.z*vector2.z

def gocgiua2vector(vector1, vector2):
    assert (type(vector1) is Vector) and (type(vector2) is Vector), 'Invalid input type.'
    return acos(tichvohuong(vector1, vector2)/(vector1.length*vector2.length))
    


if (__name__ == '__main__'):
    a = Vector(3, 5, 9)
    b = Vector(4, 2, 3)
    print(tichvohuong(a, b))
    print(degrees(gocgiua2vector(a, b)))
    print(center(a, b))