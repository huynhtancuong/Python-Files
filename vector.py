from math import sqrt
from math import acos
from math import degrees

class Point():
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Point: (%d, %d, %d)" % (self.x, self.y, self.z)

    def __add__(self, *other):
        "This function add two or more point."
        for each in other:
            assert type(each) is Point
        x = self.x
        y = self.y
        z = self.z
        for each in other:
            x += each.x
            y += each.y
            z += each.z
        return Point(x, y, z)

    def __sub__(self, *other):
        "This function subtract two or more point."
        for each in other:
            assert type(each) is Point
        x = self.x
        y = self.y
        z = self.z
        for each in other:
            x -= each.x
            y -= each.y
            z -= each.z
        return Point(x, y, z)

    def __mul__(self, *other):
        "This function multiply vector with number or vector with point."
        x = self.x
        y = self.y
        z = self.z
        for each in other:
            if (type(each) is int or type(each) is float):
                x *= each
                y *= each
                z *= each
        return Point(x, y, z)
    
    def toVector(self):
        return Vector(self.x, self.y, self.z)

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
            if (type(each) is int or type(each) is float):
                x *= each
                y *= each
                z *= each
            if (type(each) is Vector):
                x = self.y*each.z - each.y*self.z
                y = self.z*each.x - self.x*each.z
                z = self.x*each.y - each.x*self.y
        return Vector(x, y, z)

def center(pointa, pointb):
    "Lay trung diem cua 2 diem"
    return Point((pointa.x+pointb.x)/2, (pointa.y+pointb.y)/2, (pointa.z+pointb.z)/2)

def tichvohuong(vector1, vector2):
    assert (type(vector1) is Vector) and (type(vector2) is Vector), 'Invalid input type.'
    return vector1.x*vector2.x + vector1.y*vector2.y + vector1.z*vector2.z

def gocgiua2vector(vector1, vector2):
    assert (type(vector1) is Vector) and (type(vector2) is Vector), 'Invalid input type.'
    return acos(tichvohuong(vector1, vector2)/(vector1.length*vector2.length))

def getVector(pointa, pointb):
    return Vector(pointb.x-pointa.x, pointb.y-pointa.y, pointb.z-pointa.z)
    


if (__name__ == '__main__'):
    A = Point(3, 9, 2)
    B = Point(1, 3, 0)
    print(getVector(A, B))
    print(A.toVector())