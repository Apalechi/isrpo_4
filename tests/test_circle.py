import unittest
import math
import sys
sys.path.insert(0, '..')
import circle


class CircleTestCase(unittest.TestCase):
    """Тесты для модуля circle"""
    
    def test_area_positive_values(self):
        """Тест площади с положительными значениями"""
        self.assertAlmostEqual(circle.area(5), math.pi * 25)
        self.assertAlmostEqual(circle.area(10), math.pi * 100)
        self.assertAlmostEqual(circle.area(3), math.pi * 9)
    
    def test_area_unit_value(self):
        """Тест площади единичного круга"""
        self.assertAlmostEqual(circle.area(1), math.pi)
    
    def test_area_zero(self):
        """Тест площади с нулевым радиусом"""
        self.assertEqual(circle.area(0), 0)
    
    def test_area_decimal_values(self):
        """Тест площади с дробными значениями"""
        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25)
        self.assertAlmostEqual(circle.area(0.5), math.pi * 0.25)
        self.assertAlmostEqual(circle.area(1.5), math.pi * 2.25)
    
    def test_area_specific_values(self):
        """Тест площади с конкретными значениями"""
        # Радиус 7, площадь = π * 49 ≈ 153.938
        self.assertAlmostEqual(circle.area(7), 153.93804002589985, places=5)
        # Радиус 2, площадь = π * 4 ≈ 12.566
        self.assertAlmostEqual(circle.area(2), 12.566370614359172, places=5)
    
    def test_perimeter_positive_values(self):
        """Тест периметра с положительными значениями"""
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5)
        self.assertAlmostEqual(circle.perimeter(10), 2 * math.pi * 10)
        self.assertAlmostEqual(circle.perimeter(3), 2 * math.pi * 3)
    
    def test_perimeter_unit_value(self):
        """Тест периметра единичного круга"""
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевым радиусом"""
        self.assertEqual(circle.perimeter(0), 0)
    
    def test_perimeter_decimal_values(self):
        """Тест периметра с дробными значениями"""
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5)
        self.assertAlmostEqual(circle.perimeter(0.5), 2 * math.pi * 0.5)
        self.assertAlmostEqual(circle.perimeter(1.5), 2 * math.pi * 1.5)
    
    def test_perimeter_specific_values(self):
        """Тест периметра с конкретными значениями"""
        # Радиус 7, периметр = 2π * 7 ≈ 43.982
        self.assertAlmostEqual(circle.perimeter(7), 43.982297150257104, places=5)
        # Радиус 2, периметр = 2π * 2 ≈ 12.566
        self.assertAlmostEqual(circle.perimeter(2), 12.566370614359172, places=5)


if __name__ == '__main__':
    unittest.main()
