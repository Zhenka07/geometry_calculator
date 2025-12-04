import unittest
import square

class SquareTestCase(unittest.TestCase):
    """
    Тесты для модуля square.py
    """
    
    def test_area_positive(self):
        """Тест площади с положительными числами"""
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(2.5), 6.25)
        self.assertEqual(square.area(10), 100)
    
    def test_area_zero(self):
        """Тест площади с нулевой стороной"""
        self.assertEqual(square.area(0), 0)
    
    def test_area_negative(self):
        """Тест площади с отрицательной стороной (ожидаем исключение)"""
        with self.assertRaises(ValueError):
            square.area(-5)
    
    def test_perimeter_positive(self):
        """Тест периметра с положительными числами"""
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(2.5), 10.0)
        self.assertEqual(square.perimeter(10), 40)
    
    def test_perimeter_zero(self):
        """Тест периметра с нулевой стороной"""
        self.assertEqual(square.perimeter(0), 0)
    
    def test_perimeter_negative(self):
        """Тест периметра с отрицательной стороной (ожидаем исключение)"""
        with self.assertRaises(ValueError):
            square.perimeter(-5)

if __name__ == '__main__':
    unittest.main()

