import os
import sys
import re
from setuptools import setup, find_packages, Extension
import Cython.Build
import numpy

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
    "docopt >= 0.6.2",
    "cython >= 0.29.24"
]

EXTENSIONS = [
        Extension("icikt._kendall_dis", sources=["icikt/_kendall_dis.pyx"], include_dirs=[numpy.get_include()])
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
    cmdclass={'build_ext': Cython.Build.build_ext},
    install_requires=REQUIRES,
    ext_modules=EXTENSIONS,
    entry_points={"console_scripts": ["icikt = icikt.__main__:main"]},
)
