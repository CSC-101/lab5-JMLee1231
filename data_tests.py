import data
import unittest


class TestCases(unittest.TestCase):
    #### Time tests
    def test_Time_1(self):
        time = data.Time(7, 20, 1)
        self.assertEqual(7, time.hour)
        self.assertEqual(20, time.minute)
        self.assertEqual(1, time.second)


    def test_Time_2(self):
        time = data.Time(4, 19, 45)
        self.assertEqual(4, time.hour)
        self.assertEqual(19, time.minute)
        self.assertEqual(45, time.second)



    #### Add tests for Time.__eq__
    def test__eq__1(self):
        time = data.Time(4,19,45)
        time2 = data.Time(4,19,45)
        self.assertEqual(time,time2)

    #### Add tests for Time.__repr__
    def test__eq__2(self):
        time = data.Time(5,19,45)
        bad = data.Time(6,12,45)
        self.assertNotEqual(bad,time)

    def test_Time_3(self):
        time_Bad = 5
        time = data.Time(4,5,2)
        self.assertNotEqual(time,time_Bad)

    def test_repr1(self):
        expected = "Time is 5 hours, 6 minutes, 3 seconds"
        time = data.Time(5,6,3)
        self.assertAlmostEqual(repr(time),expected)

    def test_repr2(self):
        expected = "Time is 6 hours, 7 minutes, 3 seconds"
        time = data.Time(6,7,3)
        self.assertAlmostEqual(repr(time),expected)

    #### Point tests
    def test_Point_1(self):
        point = data.Point(7, 20)
        self.assertAlmostEqual(7, point.x)
        self.assertAlmostEqual(20, point.y)


    def test_Point_2(self):
        point = data.Point(4, 19)
        self.assertAlmostEqual(4, point.x)
        self.assertAlmostEqual(19, point.y)


    def test_Point_eq_1(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = data.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = data.Point(1, 20)
        point2 = data.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point = data.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point, other)


    def test_Point_repr(self):
        point = data.Point(5, 75)
        self.assertEqual('Point(5, 75)', repr(point))


if __name__ == '__main__':
    unittest.main()

