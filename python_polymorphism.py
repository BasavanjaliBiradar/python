#function overridding in python

from math import pi

class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass # pass is a keyword 
    def fact(self):
        pass
    def whichshape(self):
        print(self.name)
class square(shape):
    def __init__(self,name,length):
        super().__init__(name)
        self.length=length
    def area(self):
        print("area of square=",self.length**2)
    def fact(self):
        print("square has each angle equal to 90 degrees")
class circle(shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius=radius
        
    def area(self):
        print("area of circle is =",pi*(self.radius**2))
sq=square("s1",4)
cr=circle("c1",5)
sq.area()#area of square= 16
cr.area()#area of circle is = 78.53981633974483
sq.fact()#square has each angle equal to 90 degrees
cr.fact()# no output bez no fact method def in the circle 
cr.whichshape()#c1
sq.whichshape()#s1
