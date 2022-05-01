class Point1D:
    def __init__(self, x):
        self.x = x

    def calculate_distance(self, other):
        return other.x - self.x


class Point2D(Point1D):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    '''
    def __init__(self, *args):
        
        if isinstance(args[0], int) and isinstance(args[1], int):
            super().__init__(args[0])
            self.y = args[1]
        else:
            self.x = args[0][0]
            self.y = args[0][1]'''

    def calculate_distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5


class Vector(Point2D):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __iadd__(self, other):
        if isinstance(other, Vector) or isinstance(other, Point2D):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other.rect.x
            self.y += other.rect.y

        return self

    def __isub__(self, other):
        if isinstance(other, Vector) or isinstance(other, Point2D):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other.rect.x
            self.y -= other.rect.y

        return self


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def calculate_distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2) ** 0.5

    def get_white(self):
        return (255, 255, 255)

    def get_black(self):
        return (0, 0, 0)

    def get_red(self):
        return (255, 0, 0)

    def get_green(self):
        return (0, 255, 0)

    def get_blue(self):
        return (0, 0, 255)


# class Color(Point3D):
#     def __init__(self, x, y, z):
#         super().__init__(x, y, z)
#
#     def ???


# a = Point3D(0, 0, 0)
# WHITE = a.get_white()
# print(WHITE)
