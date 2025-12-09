import unittest
import sys
sys.path.insert(0, '..')
import triangle


class TriangleTestCase(unittest.TestCase):
    """Тесты для модуля triangle"""
    
    def test_area_positive_values(self):
        """Тест площади с положительными значениями"""
        self.assertEqual(triangle.area(10, 5), 25)
        self.assertEqual(triangle.area(6, 8), 24)
        self.assertEqual(triangle.area(4, 3), 6)
    
    def test_area_unit_values(self):
        """Тест площади с единичными значениями"""
        self.assertEqual(triangle.area(1, 1), 0.5)
        self.assertEqual(triangle.area(2, 1), 1)
    
    def test_area_zero(self):
        """Тест площади с нулевыми значениями"""
        self.assertEqual(triangle.area(0, 5), 0)
        self.assertEqual(triangle.area(5, 0), 0)
        self.assertEqual(triangle.area(0, 0), 0)
    
    def test_area_decimal_values(self):
        """Тест площади с дробными значениями"""
        self.assertAlmostEqual(triangle.area(5.5, 4.2), 11.55)
        self.assertEqual(triangle.area(3.6, 2.5), 4.5)
    
    def test_perimeter_positive_values(self):
        """Тест периметра с положительными значениями"""
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)
        self.assertEqual(triangle.perimeter(6, 8, 10), 24)
    
    def test_perimeter_unit_values(self):
        """Тест периметра с единичными значениями"""
        self.assertEqual(triangle.perimeter(1, 1, 1), 3)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевыми значениями"""
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)
    
    def test_perimeter_decimal_values(self):
        """Тест периметра с дробными значениями"""
        self.assertEqual(triangle.perimeter(2.5, 3.5, 4.0), 10.0)
        self.assertAlmostEqual(triangle.perimeter(1.1, 2.2, 3.3), 6.6)


if __name__ == '__main__':
    unittest.main()
