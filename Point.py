class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, another_point):
        return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5

    def calculate_height(self, another_point):
        return abs(self.y - another_point.y)

    def calculate_width(self, another_point):
        return abs(self.x - another_point.x)
