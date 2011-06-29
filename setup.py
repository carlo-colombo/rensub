#!/usr/bin/env python
from distutils.core import setup
setup(name='Rensub',
    version='1.0.1',
    packages=['rensub'],
    description='Subtitles utils',
    author='Carlo Colombo',
    author_email='carlo.colombo@gmx.com',
    url='https://github.com/carlo-colombo/rensub',
    scripts=['scripts/rensub','scripts/getshow']
    )