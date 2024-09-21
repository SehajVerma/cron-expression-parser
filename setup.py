from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    project_description = readme_file.read()

setup(
    name="cron-schedule-parser",
    version="1.0.0",
    author="Sehaj Verma",
    author_email="sehaj.verma@github.com",
    description="A cron expression parser that converts cron schedules into a human-readable format.",
    long_description=project_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SehajVerma/cron-schedule-parser",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cron-schedule-parser = cron_schedule_parser.cli:main"
        ]
    },
    python_requires='>=3.6',
)