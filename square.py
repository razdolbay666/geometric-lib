import unittest

def area(a):
    '''Функция подсчета площади квадрата со стороной равной а
       Входные данные: a - сторона квадрата
       Выходные данные: площадь квадрата со стороной, равной а
       Пример вызова:
       area(5)
       Возвращаемое значение = 25'''
    return a * a


def perimeter(a):
    '''Функция подсчета периметра квадрата со стороной равной а
       Входные данные: a - сторона квадрата
       Выходные данные: периметр квадрата со стороной, равной а
       Пример вызова:
       perimeter(5)
       Возвращаемое значение = 20'''
    return 4 * a

class TestSquare(unittest.TestCase):
    
    def test_area(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1.5), 2.25)
        
    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1.5), 6.0)
