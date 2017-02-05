#!/usr/bin/env python

import os
from distutils.core import setup

# initialize __version__
execfile(os.path.join("psutil_remote", "version.py"))

setup(name='psutil-remote',
      version=__version__,
      description='A WebSockets wrapper around Python psutil',
      author='Jordan Heemskerk',
      author_email='jordanh@shaw.ca',
      url='https://github.com/jordan-heemskerk/psutil-remote',
      packages=['psutil_remote'],
     )