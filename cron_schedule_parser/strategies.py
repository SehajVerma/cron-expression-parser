from cron_schedule_parser.constants import ANY_VALUE, VALUE_LIST_SEPARATOR, RANGE_OF_VALUES, STEP_VALUES
from cron_schedule_parser.utils import get_range_values, get_step_values

class ParsingStrategy:
    def parse(self, value_str, field_name):
        raise NotImplementedError("Subclasses must implement 'parse' method")

class AnyValueStrategy(ParsingStrategy):
    def parse(self, value_str, field_name, cron_field):
        return list(range(cron_field.get_min(), cron_field.get_max() + 1))

class ListValueStrategy(ParsingStrategy):
    def parse(self, value_str, field_name, cron_field):
        values = []
        parts = value_str.split(VALUE_LIST_SEPARATOR)
        for part in parts:
            if part == ANY_VALUE:
                continue
            if STEP_VALUES in part:
                step_parts = part.split(STEP_VALUES)
                if len(step_parts) == 2:
                    if int(step_parts[1]) > cron_field.get_max():
                        raise ValueError(f"Invalid cron field value for {self.field_name}: {self.value_str}")
                    range_values = get_step_values(step_parts[1], cron_field.get_min(), cron_field.get_max())
                    values.extend(range_values)
                else:
                    raise ValueError(f"Invalid cron field value for {self.field_name}: {self.value_str}")
            elif RANGE_OF_VALUES in part:
                range_values = get_range_values(part)
                values.extend(range_values)
            else:
                values.append(int(part))
        return values

class RangeValueStrategy(ParsingStrategy):
    def parse(self, value_str, field_name, cron_field):
        return get_range_values(value_str)

class StepValueStrategy(ParsingStrategy):
    def parse(self, value_str, field_name, cron_field):
        step_parts = value_str.split(STEP_VALUES)
        if int(step_parts[1]) > cron_field.get_max():
            raise ValueError(f"Invalid cron field value for {field_name}: {value_str}")
        return get_step_values(step_parts[1], cron_field.get_min(), cron_field.get_max())

class SingleValueStrategy(ParsingStrategy):
    def parse(self, value_str, field_name, cron_field):
        return [int(value_str)]
