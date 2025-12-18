import unittest
def area(a, h):
    '''Функция подсчета площади треугольника со стороной а и проведенной к ней высотой h
       Входные данные: a, h - длина стороны треугольника, длина высоты проведенной к стороне длины а 
       Выходные данные: площадь треугольника со сторонй а и проведенной к ней высотой h 
       Пример вызова:
       area(5, 7)
       Возвращаемое значение = 17.5'''
    return a * h / 2 


def perimeter(a, b, c):
    '''Функция подсчета периметра треугольника со сторонами a, b, c
       Входные данные: a, b, c - длины сторон треугольника 
       Выходные данные: периметр треугольника со сторонами a, b, c 
       Пример вызова:
       perimeter(5, 7, 5)
       Возвращаемое значение = 17'''
    return a + b + c 

class TestTriangle(unittest.TestCase):
    
    def test_area(self):
        self.assertEqual(area(5, 7), 17.5)
        self.assertEqual(area(2, 3), 3.0)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(4, 0), 0)
        self.assertEqual(area(1.5, 2), 1.5)
        
    def test_perimeter(self):
        self.assertEqual(perimeter(5, 7, 5), 17)
        self.assertEqual(perimeter(2, 3, 4), 9)
        self.assertEqual(perimeter(0, 5, 5), 10)
        self.assertEqual(perimeter(1.5, 2.5, 3), 7.0)
