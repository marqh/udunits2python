from distutils.core import setup, Extension
from Cython.Build import cythonize
from distutils.sysconfig import get_config_var

import numpy as np

setup(
  name = 'udunits2python',
  version = '0.1',
  description = 'Python package for accessing udunits2 from unidata',
  package_dir = {'': 'lib'},
  packages = ['udunits'],
  ext_modules =  Extension('udunits.__init__', ['lib/udunits/__init__.pyx'],
                           include_dirs=[get_config_var('INCLUDEDIR'), np.get_include()],
                  libraries=['libc', 'netcdf'],
                  library_dirs=[get_config_var('LIBDIR')],
                  **extra_extension_args
                  ),
)

