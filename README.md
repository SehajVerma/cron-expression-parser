# Cron Schedule Interpreter

This Python utility parses cron expressions and presents them in an easy-to-read tabular format. It processes cron expressions that contain five timing fields (minute, hour, day of month, month, and day of the week) and a command, displaying the result in a structured table.

## Prerequisites

- Python 3.6 or newer

## How to Use

To get started, follow these steps:

1. Clone this repository to your local system.

2. Open a terminal and navigate to the root directory of the project.

3. Install the package as a binary.
   ```shell
   pip install --editable .
   ```

4. `cron-schedule-parser` binary is now created. You can run the program with the cron expression For example:

   ```shell
   cron-parser "*/15 0 1,15 * 1-5 /usr/bin/find"
   ```

5. Output of the provided cron expression will be displayed as a table, like this:

   ```
   minute        0 15 30 45
   hour          0
   day of month  1 15
   month         1 2 3 4 5 6 7 8 9 10 11 12
   day of week   1 2 3 4 5
   command       /usr/bin/find

6. To run the unit tests, navigate to the root directory and execute:
   ```shell
   python3 -m unittest discover -s tests
   ```

