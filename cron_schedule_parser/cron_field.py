from cron_schedule_parser.constants import FIELD_NAMES, ANY_VALUE, VALUE_LIST_SEPARATOR, RANGE_OF_VALUES, STEP_VALUES
from cron_schedule_parser.strategies import AnyValueStrategy, ListValueStrategy, RangeValueStrategy, StepValueStrategy, SingleValueStrategy

MIN_VALUES = {
    "minute": 0,
    "hour": 0,
    "day of month": 1,
    "month": 1,
    "day of week": 0
}

MAX_VALUES = {
    "minute": 59,
    "hour": 23,
    "day of month": 31,
    "month": 12,
    "day of week": 6
}


class CronField:

    def __init__(self, value_str, field_name):
        self.value_str = value_str
        self.field_name = field_name
        self.values = []

    def validate_characters(self):
        valid_chars = set("0123456789,*/-")
        if not set(self.value_str).issubset(valid_chars):
            raise ValueError(
                f"Invalid characters in {self.field_name}: {self.value_str}")

    def validate_bounds(self):
        for value in self.values:
            if value < self.get_min() or value > self.get_max():
                raise ValueError(
                    f"Invalid value {value} for {self.field_name}. Valid range is {self.get_min()}-{self.get_max()}")

    def select_strategy(self):
        if self.value_str == ANY_VALUE:
            return AnyValueStrategy()
        elif VALUE_LIST_SEPARATOR in self.value_str:
            return ListValueStrategy()
        elif RANGE_OF_VALUES in self.value_str:
            return RangeValueStrategy()
        elif STEP_VALUES in self.value_str:
            return StepValueStrategy()
        else:
            return SingleValueStrategy()

    def parse(self):
        self.validate_characters()
        strategy = self.select_strategy()
        self.values = strategy.parse(self.value_str, self.field_name, self)
        self.validate_bounds()

    def get_min(self):
        return MIN_VALUES[self.field_name]

    def get_max(self):
        return MAX_VALUES[self.field_name]
