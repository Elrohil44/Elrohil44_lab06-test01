import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2016, 2, 29)
        self.assertEqual(weekday, 0)
        weekday = calculate(1969, 12, 1)
        self.assertEqual(weekday, 0)
        weekday = calculate(2011, 2, 6)
        self.assertEqual(weekday, 0)
        weekday = calculate(2017, 5, 9)
        self.assertEqual(weekday, 1)

        weekday = calculate(2017, 2, 29)
        self.assertEqual(weekday, -1)
        weekday = calculate(2017, 13, 9)
        self.assertEqual(weekday, -1)
        weekday = calculate(2017, -1, 9)
        self.assertEqual(weekday, -1)

        weekday = calculate(2017, 1, -9)
        self.assertEqual(weekday, -1)
        weekday = calculate(2017, 1, 32)
        self.assertEqual(weekday, -1)
        weekday = calculate(2017, 2, 89)
        self.assertEqual(weekday, -1)
        weekday = calculate(2017, 4, 31)
        self.assertEqual(weekday, -1)

        weekday = calculate(-2017, 1, 9)
        self.assertEqual(weekday, -1)
        weekday = calculate(-1, 1, 9)
        self.assertEqual(weekday, -1)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)
        retcode = main(("--year", "1969", "--month", "12", "--day", "1"))
        self.assertEqual(retcode, 0)
        retcode = main(("--year", "2011", "--month", "2", "--day", "6"))
        self.assertEqual(retcode, 0)
        retcode = main(("--year", "2017", "--month", "5", "--day", "9"))
        self.assertEqual(retcode, 0)
        retcode = main(("--year", "2a017", "--month", "5", "--day", "9"))
        self.assertEqual(retcode, -1)
        retcode = main(("--year", "2017", "--month", "5a", "--day", "9"))
        self.assertEqual(retcode, -1)
        retcode = main(("--year", "2017", "--month", "5", "--day", "x9"))
        self.assertEqual(retcode, -1)
        retcode = main(("--year", "2017", "--month", "5", "--day", "x9"))
        self.assertEqual(retcode, -1)
        retcode = main(("--year", "2017", "--month", "5", "--day", "x9"))
        self.assertEqual(retcode, -1)
        retcode = main(("--year", "2017", "--day", "9"))
        self.assertEqual(retcode, -1)
        retcode = main(("--month", "5", "--day", "9"))
        self.assertEqual(retcode, -1)
        retcode = main(("--day", "9"))
        self.assertEqual(retcode, -1)


if __name__ == '__main__':
    unittest.main()
