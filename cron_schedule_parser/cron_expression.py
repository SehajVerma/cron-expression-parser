from cron_schedule_parser.constants import FIELD_NAMES
from cron_schedule_parser.cron_field import CronField

class CronExpression:
    def __init__(self, expression: str):
        self.expression = expression
        self.fields = []
        self.command = None

    def parse(self):

        # Split the expression into fields (5 time fields and a command)
        field_strings = self.expression.split(' ', 5)

        # Validate the number of fields
        if len(field_strings) != 6:
            raise ValueError(f"Invalid cron expression: {self.expression}. Must have exactly 5 time fields and a command.")

        self.command = field_strings[-1]
        if not self.command:
            raise ValueError(f"Command part of the cron expression cannot be empty.")
        
        for i, field_str in enumerate(field_strings[:-1]):
            field_name = FIELD_NAMES[i]
            cron_field = CronField(field_str, field_name)
            cron_field.parse()
            self.fields.append(cron_field)
        return self

    def to_table(self):
        table_lines = [self.format_field(field) for field in self.fields]
        table_lines.append(self.format_command(self.command))
        return "\n".join(table_lines)

    def format_field(self, field):
        return f"{field.field_name:<14}{' '.join(map(str, field.values))}"

    def format_command(self, command):
        return f"{'command':<14}{command}"
