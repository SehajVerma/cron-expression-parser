import argparse
from cron_schedule_parser.cron_expression import CronExpression

def main():
    parser = argparse.ArgumentParser(description="Cron Schedule Parser")
    parser.add_argument("expression", help="Cron expression to parse")
    args = parser.parse_args()

    try:
        cron = CronExpression(args.expression).parse()
        output = cron.to_table()
        print(output)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
