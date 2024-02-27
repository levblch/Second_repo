# class Rectangle:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width

#     def get_area(self):
#         return self._length * self._width
    
# class Triangle:
#     def __init__(self, base, height):
#         self._base = base
#         self._height = height

#     def get_area(self):
#         return 0.5 * self._base * self._height


# rect1 = Rectangle(4, 5)
# rect2 = Rectangle(8, 10)
# trian1 = Triangle(7, 9)
# trian2 = Triangle(3, 5)

# # print(rect1.get_rectangle_area(), rect2.get_rectangle_area())
# # print(trian1.get_triangle_area(), trian2.get_triangle_area())

# figures = [rect1, rect2, trian1, trian2]
# for fig in figures:
#     print(f'Площадь фигуры: {fig.get_area()}')

# class Rectangle:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width

#     def get_area(self):
#         return self._length * self._width
    
#     def get_perimeter(self):
#         return (self._length + self._width) * 2
    
# class Triangle:
#     def __init__(self, side1, side2, side3):
#         self._side1 = side1
#         self._side2 = side2
#         self._side3 = side3

#     def get_perimeter(self):
#         return self._side1 + self._side2 + self._side3

#     def get_area(self):
#         p = (self._side1 + self._side2 + self._side3) / 2
#         return (p * (p - self._side1) * (p - self._side2) * (p - self._side3)) ** 0.5

# rect = Rectangle(4, 5)
# trian = Triangle(3, 4, 5)
# figures = [rect, trian]
# for fig in figures:
#     print(f'Площадь фигуры: {fig.get_area()}')
#     print(f'Периметр фигуры: {fig.get_perimeter()}')    



    
class Circle(Figure):
    def __init__(self, radius):
        self._radius = radius

circ = Circle(8)
circ_area = circ.get_area()
circ_perimeter = circ.get_perimeter()
print(circ_area)
print(circ_perimeter)

from figure import Figure

class Circle(Figure):
    pass

class Rectangle(Figure):
    pass

class Triangle(Figure):
    pass