
from distutils.core import setup
from Cython.Build import cythonize

setup(
            ext_modules = cythonize("htest.pyx")
            #ext_modules = cythonize("convolve.pyx")
            )


