import unittest
import sys

# Импортируем все тесты
from test_rectangle import RectangleTestCase
from test_triangle import TriangleTestCase
from test_square import SquareTestCase
from test_circle import CircleTestCase


def suite():
    """Создает набор всех тестов"""
    test_suite = unittest.TestSuite()
    
    # Добавляем все тестовые классы
    test_suite.addTest(unittest.makeSuite(RectangleTestCase))
    test_suite.addTest(unittest.makeSuite(TriangleTestCase))
    test_suite.addTest(unittest.makeSuite(SquareTestCase))
    test_suite.addTest(unittest.makeSuite(CircleTestCase))
    
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
