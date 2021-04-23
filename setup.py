from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='yara',
    version='1',
    packages=['core', 'jdate', 'google_calendar'],
    url='https://github.com/M-b850/Yara-To-Google',
    license='MIT',
    author='Mehrshad Baqerzadegan',
    author_email='mehrshadbaqerzadegan@gmail.com',
    description='Add Practices to google calendar account.',
    include_package_data=True,
)
