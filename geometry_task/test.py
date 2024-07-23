import unittest
from geometry_task.geometry import Circle, Triangle, calculate_area

class TestGeometry(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), 28.274333882308138, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=5)

    def test_right_angled_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

        triangle = Triangle(5, 12, 13)
        self.assertTrue(triangle.is_right())

        triangle = Triangle(1, 1, 1)
        self.assertFalse(triangle.is_right())

    def test_calculate_area(self):
        circle = Circle(3)
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(circle), 28.274333882308138, places=5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0, places=5)

    def test_invalid_shape(self):
        with self.assertRaises(TypeError):
            calculate_area("not_a_shape")

if __name__ == '__main__':
    unittest.main()
