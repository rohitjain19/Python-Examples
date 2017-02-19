class Circle(object):

    #class object attribute
    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        #radius**2 * pi
        return (self.radius**2)*Circle.pi

    def set_radius(self,new_radius):
        self.radius = new_radius

c = Circle(radius = 10)

print ("Current Radius is :",c.radius)

c.set_radius(60)

print ("Current Radius is :",c.radius)

