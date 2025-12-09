import unittest
import sys
sys.path.insert(0, '..')
import rectangle


class RectangleTestCase(unittest.TestCase):
    """Тесты для модуля rectangle"""
    
    def test_area_positive_values(self):
        """Тест площади с положительными значениями"""
        self.assertEqual(rectangle.area(5, 10), 50)
        self.assertEqual(rectangle.area(3, 7), 21)
        self.assertEqual(rectangle.area(2.5, 4), 10.0)
    
    def test_area_unit_square(self):
        """Тест площади единичного прямоугольника"""
        self.assertEqual(rectangle.area(1, 1), 1)
    
    def test_area_zero(self):
        """Тест площади с нулевыми значениями"""
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area(5, 0), 0)
        self.assertEqual(rectangle.area(0, 0), 0)
    
    def test_perimeter_positive_values(self):
        """Тест периметра с положительными значениями"""
        self.assertEqual(rectangle.perimeter(5, 10), 30)
        self.assertEqual(rectangle.perimeter(3, 7), 20)
        self.assertEqual(rectangle.perimeter(2.5, 4), 13.0)
    
    def test_perimeter_unit_square(self):
        """Тест периметра единичного прямоугольника"""
        self.assertEqual(rectangle.perimeter(1, 1), 4)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевыми значениями"""
        self.assertEqual(rectangle.perimeter(0, 5), 10)
        self.assertEqual(rectangle.perimeter(5, 0), 10)
        self.assertEqual(rectangle.perimeter(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
