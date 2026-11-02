import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):

    def test_area_docstring_example(self):
        self.assertAlmostEqual(circle.area(3), 28.274333882308138)

    def test_area_unit_radius(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(circle.area(0.5), math.pi / 4)

    def test_perimeter_docstring_example(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.84955592153876)

    def test_perimeter_unit_radius(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle.perimeter(0.5), math.pi)


class CircleInvalidInputTestCase(unittest.TestCase):

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            circle.area("3")


class RectangleTestCase(unittest.TestCase):

    def test_area_docstring_example(self):
        self.assertEqual(rectangle.area(3, 4), 12)

    def test_area_zero_side(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_square_case(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_commutative(self):
        self.assertEqual(rectangle.area(3, 7), rectangle.area(7, 3))

    def test_area_float(self):
        self.assertAlmostEqual(rectangle.area(1.5, 2.5), 3.75)

    def test_perimeter_docstring_example(self):
        self.assertEqual(rectangle.perimeter(3, 4), 14)

    def test_perimeter_zero_side(self):
        self.assertEqual(rectangle.perimeter(5, 0), 10)

    def test_perimeter_commutative(self):
        self.assertEqual(rectangle.perimeter(3, 7), rectangle.perimeter(7, 3))

    def test_perimeter_float(self):
        self.assertAlmostEqual(rectangle.perimeter(1.5, 2.5), 8.0)


class RectangleInvalidInputTestCase(unittest.TestCase):

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, 4)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, 4)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("a", 2)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("a", "b")


class SquareTestCase(unittest.TestCase):

    def test_area_docstring_example(self):
        self.assertEqual(square.area(5), 25)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_one(self):
        self.assertEqual(square.area(1), 1)

    def test_area_float(self):
        self.assertAlmostEqual(square.area(1.5), 2.25)

    def test_area_large_value(self):
        self.assertEqual(square.area(10 ** 6), 10 ** 12)

    def test_perimeter_docstring_example(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(1.5), 6.0)


class SquareInvalidInputTestCase(unittest.TestCase):

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            square.area(-5)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            square.perimeter(-5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            square.area("a")

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("ab")


class TriangleTestCase(unittest.TestCase):

    def test_area_docstring_example(self):
        self.assertEqual(triangle.area(3, 4), 6.0)

    def test_area_zero_height(self):
        self.assertEqual(triangle.area(5, 0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(triangle.area(2.5, 4), 5.0)

    def test_area_odd_product(self):
        self.assertEqual(triangle.area(3, 3), 4.5)

    def test_perimeter_docstring_example(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        self.assertEqual(triangle.perimeter(2, 2, 2), 6)

    def test_perimeter_float(self):
        self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3.0), 7.0)

    def test_perimeter_order_independent(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), triangle.perimeter(5, 3, 4))


class TriangleInvalidInputTestCase(unittest.TestCase):
    
    def test_area_negative_base(self):
        with self.assertRaises(ValueError):
            triangle.area(-3, 4)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)

    def test_perimeter_triangle_inequality(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, 10)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            triangle.area("a", 4)