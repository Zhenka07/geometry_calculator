import unittest
import math
import circle

class CircleTestCase(unittest.TestCase):
    """
    Тесты для модуля circle.py
    """
    
    def test_area_positive(self):
        """Тест площади с положительным радиусом"""
        self.assertAlmostEqual(circle.area(5), math.pi * 25)
        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25)
        self.assertAlmostEqual(circle.area(1), math.pi)
    
    def test_area_zero(self):
        """Тест площади с нулевым радиусом"""
        self.assertEqual(circle.area(0), 0)
    
    def test_area_negative(self):
        """Тест площади с отрицательным радиусом (ожидаем исключение)"""
        with self.assertRaises(ValueError):
            circle.area(-5)
    
    def test_perimeter_positive(self):
        """Тест длины окружности с положительным радиусом"""
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5)
        self.assertAlmostEqual(circle.perimeter(2.5), 2 * math.pi * 2.5)
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)
    
    def test_perimeter_zero(self):
        """Тест длины окружности с нулевым радиусом"""
        self.assertEqual(circle.perimeter(0), 0)
    
    def test_perimeter_negative(self):
        """Тест длины окружности с отрицательным радиусом (ожидаем исключение)"""
        with self.assertRaises(ValueError):
            circle.perimeter(-5)

if __name__ == '__main__':
    unittest.main()