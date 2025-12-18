import math
import unittest


def area(r):
    '''Функция подсчета площади круга с радиусом r
       Входные данные: r - радиус круга
       Выходные данные: площадь круга с радиусом r
       Пример вызова:
       area(5)
       Возвращаемое значение = 78.53981633974483'''
    return math.pi * r * r


def perimeter(r):
    '''Функция подсчета длинны окружности с радиусом r
       Входные данные: r - радиус окружности
       Выходные данные: длинна окружности с радиусом r
       Пример вызова:
       perimeter(5)
       Возвращаемое значение = 31.41592653589793'''
    return 2 * math.pi * r

class TestCircle(unittest.TestCase):
    
    def test_area(self):
        self.assertAlmostEqual(area(5), math.pi * 25)
        self.assertAlmostEqual(area(2), math.pi * 4)
        self.assertEqual(area(0), 0)
        self.assertAlmostEqual(area(1.5), math.pi * 2.25)
        
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)
        self.assertAlmostEqual(perimeter(2), 2 * math.pi * 2)
        self.assertEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(1.5), 2 * math.pi * 1.5)
        
