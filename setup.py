#!/usr/bin/env python

import re
import sys

from setuptools import setup, find_packages


#def version():
    #with open('pypot/_version.py') as f:
        #return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read()).group(1)

#extra = {}
#if sys.version_info >= (3,):
    #extra['use_2to3'] = True

setup(name='explauto',
      version='0.1',
      packages=find_packages(exclude = ["humm"]),

      install_requires=['numpy'],

      #extras_require={
          #'tools': [],  # Extras require: PyQt4 (not a PyPi packet)
          #'doc': ['sphinx', 'sphinx-bootstrap-theme'],
          #'server': ['bottle', 'tornado', 'zmq']
      #},

      #entry_points={
          #'gui_scripts': [
              #'herborist = pypot.tools.herborist.herborist:main [tools]',
              #],
      #},

      #setup_requires=['setuptools_git >= 0.3', ],

      #include_package_data=True,
      #exclude_package_data={'': ['README', '.gitignore']},

      zip_safe=True,

      author='Moulin-Frier Clement, Pierre Rouanet',
      author_email='clement.moulinfrier@gmail.com',
      description='Python Library for Autonomous Exploration',
      url='https://github.com/poppy-project/pypot'
      #license='GNU GENERAL PUBLIC LICENSE Version 3',
      )
