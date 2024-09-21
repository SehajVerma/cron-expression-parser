import unittest
from cron_schedule_parser.utils import get_step_values, get_range_values

class TestUtils(unittest.TestCase):

    def test_get_step_values(self):
        self.assertEqual(get_step_values(15, 0, 59), [0, 15, 30, 45])

    def test_get_range_values(self):
        self.assertEqual(get_range_values("5-10"), [5, 6, 7, 8, 9, 10])

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            get_range_values("10-5")

if __name__ == '__main__':
    unittest.main()
