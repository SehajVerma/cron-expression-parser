import unittest
from cron_schedule_parser.cron_field import CronField

class TestCronField(unittest.TestCase):

    def test_any_value(self):
        cron_field = CronField('*', 'minute')
        cron_field.parse()
        self.assertEqual(cron_field.values, list(range(0, 60)))

    def test_value_list(self):
        cron_field = CronField('1,15', 'minute')
        cron_field.parse()
        self.assertEqual(cron_field.values, [1, 15])

    def test_range_values(self):
        cron_field = CronField('5-10', 'minute')
        cron_field.parse()
        self.assertEqual(cron_field.values, list(range(5, 11)))

    def test_step_values(self):
        cron_field = CronField('*/15', 'minute')
        cron_field.parse()
        self.assertEqual(cron_field.values, [0, 15, 30, 45])

    def test_invalid_range(self):
        cron_field = CronField('5-1', 'minute')
        with self.assertRaises(ValueError):
            cron_field.parse()

if __name__ == '__main__':
    unittest.main()
