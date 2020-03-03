class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def coordinates(self):
        print(f"Координаты: x {self.x} y {self.y}")

    def __repr__(self):
        return f"Point x: {self.x} y: {self.y}"



my_point = Point(1,2)
my_point.coordinates()

print(my_point)
# print(my_point.x)
# my_point.x = 10
# my_point.coordinates()

# print(my_point.x)