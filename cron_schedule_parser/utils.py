def get_range_values(range_str):
    try:
        start, end = map(int, range_str.split('-'))
        if start > end:
            raise ValueError(f"Invalid range: {start}-{end}")
        return list(range(start, end + 1))
    except ValueError as e:
        raise ValueError(f"Invalid range format: {range_str}") from e


def get_step_values(step_str, min_value, max_value):
    step = int(step_str)
    if step < 1 or step > (max_value - min_value + 1):
        raise ValueError(f"Invalid step value {step} for range {min_value}-{max_value}")
    return [value for value in range(min_value, max_value + 1) if (value - min_value) % step == 0]
