import unittest
from cron_schedule_parser.cron_expression import CronExpression

class TestCronExpression(unittest.TestCase):

    def test_parse_expression(self):
        expression = "*/15 0 1,15 * 1-5 /usr/bin/find"
        cron_exp = CronExpression(expression)
        cron_exp.parse()

        self.assertEqual(cron_exp.fields[0].values, [0, 15, 30, 45])  # minute field
        self.assertEqual(cron_exp.fields[1].values, [0])               # hour field
        self.assertEqual(cron_exp.fields[2].values, [1, 15])           # day of month field
        self.assertEqual(cron_exp.fields[3].values, list(range(1, 13)))# month field
        self.assertEqual(cron_exp.fields[4].values, [1, 2, 3, 4, 5])   # day of week field
        self.assertEqual(cron_exp.command, '/usr/bin/find')

    def test_invalid_expression(self):
        expression = "*/15 0 1,15 * 5-1 /usr/bin/find"
        cron_exp = CronExpression(expression)
        with self.assertRaises(ValueError):
            cron_exp.parse()

if __name__ == '__main__':
    unittest.main()
