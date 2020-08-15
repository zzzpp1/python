import unittest

from rect import Rect


class RectTest(unittest.TestCase):
    def test_intersect_for_crossing_rects(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1, 1, 0.5, 0.5)))

    def test_intersect_for_crossing_rects_1(self):
        self.assertFalse(Rect(1,1,1,1).intersect(Rect(2, 2, 0.5, 0.5)))

    def test_intersect_for_crossing_rects_2(self):
        self.assertFalse(Rect(1, 1, 1, 1).intersect(Rect(1, 0, 0.5, 0.5)))

    def test_intersect_for_crossing_rects_3(self):
        self.assertTrue(Rect(1, 1, 1, 1).intersect(Rect(1.5, 1.5, 1, 1)))


if __name__ == '__main__':
    unittest.main()
