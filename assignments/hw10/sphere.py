from math import pi
class Sphere:
    """represents a geometric solid sphere"""

    def __init__(self,radius):
        """sphere constructor, takes input radius"""
        self.radius = radius
    def get_radius(self):
        """returns the radius of sphere"""
        return self.radius
    def surface_area(self):
        """returns the surface area of sphere"""
        return 4*pi*(self.radius**2)
    def volume(self):
        """returns sphere volume"""
        return 4/3 * pi * (self.radius**3)
