import unittest

def area(a, b):
    '''Функция подсчета площади прямоугольника со смежными сторонами, равными a, b
       Входные данные: a, b - смежные стороны прямоугольника
       Выходные данные: площадь прямугольника со смежными сторонами, равными a, b
       Пример вызова:
       area(5, 7)
       Возвращаемое значение = 35'''
    return a * b 


def perimeter(a, b):
    '''Функция подсчета периметра прямоугольника со смежными сторонами, равными a, b
       Входные данные: a, b - смежные стороны прямоугольника
       Выходные данные: периметр прямоугольника со смежными сторонами, равными a, b
       Пример вызова:
       area(5, 7)
       Возвращаемое значение = 24'''
    return a + b + a + b

class TestRectangle(unittest.TestCase):
    
    def test_area(self):
        self.assertEqual(area(5, 7), 35)
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(1.5, 2), 3.0)
        
    def test_perimeter(self):
        self.assertEqual(perimeter(5, 7), 24)
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(0, 5), 10)  # 0+5+0+5 = 10
        self.assertEqual(perimeter(1.5, 2.5), 8.0)
