# Phyllis Torres
# 17.4 Write an add Method for a Point Class Assignment
# Due 11/17/2016

print('17.4 Write an add Method for a Point Class Assignment \n')
print('Phyllis Torres\n\n')

print('This program will use an add method for a Point class object. ')


# create a point class
class Point:
    """Represents a point in a 2 dimensional space
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# initialize the instantiated object with the values of 3 and 4 for x and y
p1 = Point(3, 4)
p2 = Point(2, 2)

# when adding the points together, the add method is invoked
p3 = p1 + p2

# display the point values for p1
print ('\nThe values for the point, p1, are: '),
print p1

# display the point values for p2
print ('\nThe values for the point, p2, are: '),
print p2

# display the point values for p3
print ('\nWhen these points are added together, the result is: '),

# print the point using the str method defined in the class
print p3


