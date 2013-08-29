#!/usr/bin/env python


from numpy.distutils.core import setup
from numpy.distutils.core import Extension
import os
import glob


setup(name='Bayesian Exploration Statistical Toolbox',
      author='Ilias Bilionis',
      version='0.0',
      ext_modules=[Extension('best.core.orthpol',
                             glob.glob(os.path.join('src', 'orthpol',
                                                    '*.f')))],
      packages=['best', 'best.core', 'best.misc', 'best.domain',
                'best.maps', 'best.linalg', 'best.random', 'best.rvm',
                'best.gp', 'best.design', 'best.uq', 'best.inverse'])
