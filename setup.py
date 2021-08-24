import os
import sys
import re
from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist')
    os.system('twine upload dist/*')
    sys.exit()


def readme():
    with open('README.rst') as readme_file:
        return readme_file.read()


def find_version():
    with open('icikt/__init__.py', 'r') as fd:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


REQUIRES = [
    "numpy >= 1.18.2",
    "scipy >= 1.4.1",
    "docopt >= 0.6.2"
]


setup(
    name='icikt',
    version=find_version(),
    author='Praneeth S. Bhatt, Robert M. Flight, Hunter N.B. Moseley',
    author_email='praneethsbhatt@gmail.com',
    description='Python tool to calculate the KendallTau correlation coefficients.',
    keywords='icikendalltau missing values',
    license='Modified Clear BSD License',
    url='https://gitlab.cesb.uky.edu/rmflight/pythonICIKendallTau',
    packages=find_packages(),
    platforms='any',
    long_description=readme(),
    install_requires=REQUIRES,
    entry_points={"console_scripts": ["icikt = icikt.__main__:main"]},
)
