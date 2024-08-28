from setuptools import Extension, setup
import numpy
from Cython.Build import cythonize


ext_modules = [
    Extension(
        "icikt.c_kendall_dis",
        sources=["src/icikt/c_kendall_dis.pyx"],
        include_dirs=[numpy.get_include()]
    )
]

setup(
      ext_modules = cythonize(ext_modules)
      )

