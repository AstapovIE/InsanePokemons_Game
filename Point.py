class Point1D:
    def __init__(self, x):
        self.x = x

    def calculate_distance(self, other):
        return other.x - self.x


class Point2D(Point1D):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y


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
