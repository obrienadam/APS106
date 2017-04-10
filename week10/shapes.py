from math import sqrt

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def is_inside(self, point):
        return self.center.dist(point) <= self.radius

    def __str__(self):
        return '{}, r = {}'.format(self.center, self.radius)

class Triangle:
    def __init__(self, v1, v2, v3):
        self.vertices = v1, v2, v3

    def collides_with(self, shape):
        for v in self.vertices:
            if shape.is_inside(v):
                return True

        return False

    def __str__(self):
        return '{{{},{},{}}}'.format(*self.vertices)

if __name__ == '__main__':
    pt = Point2D(1.34, 0.54)
    circle = Circle(Point2D(0.44, 0.54), 1.3)

    print('Point {} is {} circle {}.'.format(pt, 'inside' if circle.is_inside(pt) else 'not inside', circle))

    tri = Triangle(Point2D(0, 0), Point2D(1, 0), Point2D(0.5, 0.5))
    print('Triangle:', tri)

    if tri.collides_with(circle):
        print('The circle and the triangle collide!')
    else:
        print('Phew, there was no collision.')

    # Move the circle
    circle.center = Point2D(20., 20.)

    if tri.collides_with(circle):
        print('The circle and the triangle collide!')
    else:
        print('Phew, there was no collision.')






