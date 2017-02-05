#!/usr/bin/env python

import os
from setuptools import setup

# initialize __version__
execfile(os.path.join("psutil_remote", "version.py"))

setup(name='psutil-remote',
      version=__version__,
      description='A WebSockets wrapper around Python psutil',
      author='Jordan Heemskerk',
      author_email='jordanh@shaw.ca',
      url='https://github.com/jordan-heemskerk/psutil-remote',
      packages=['psutil_remote'],
      entry_points={
          'console_scripts': [
              'psutil-remote = psutil_remote.__main__:main'
          ]
      },
     )