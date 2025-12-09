import unittest
import sys
sys.path.insert(0, '..')
import square


class SquareTestCase(unittest.TestCase):
    """Тесты для модуля square"""
    
    def test_area_positive_values(self):
        """Тест площади с положительными значениями"""
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(10), 100)
        self.assertEqual(square.area(7), 49)
    
    def test_area_unit_value(self):
        """Тест площади единичного квадрата"""
        self.assertEqual(square.area(1), 1)
    
    def test_area_zero(self):
        """Тест площади с нулевым значением"""
        self.assertEqual(square.area(0), 0)
    
    def test_area_decimal_values(self):
        """Тест площади с дробными значениями"""
        self.assertEqual(square.area(2.5), 6.25)
        self.assertAlmostEqual(square.area(3.3), 10.89)
        self.assertEqual(square.area(0.5), 0.25)
    
    def test_perimeter_positive_values(self):
        """Тест периметра с положительными значениями"""
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(10), 40)
        self.assertEqual(square.perimeter(7), 28)
    
    def test_perimeter_unit_value(self):
        """Тест периметра единичного квадрата"""
        self.assertEqual(square.perimeter(1), 4)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевым значением"""
        self.assertEqual(square.perimeter(0), 0)
    
    def test_perimeter_decimal_values(self):
        """Тест периметра с дробными значениями"""
        self.assertEqual(square.perimeter(2.5), 10.0)
        self.assertAlmostEqual(square.perimeter(3.3), 13.2)
        self.assertEqual(square.perimeter(0.5), 2.0)


if __name__ == '__main__':
    unittest.main()
