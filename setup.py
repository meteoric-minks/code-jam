#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='application',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    url='https://github.com/meteoric-minks/code-jam',
    license='MIT License',
    author='Meteoric Minks',
    description='Application for the code jam',
    entry_points={
        'console_scripts': ['boxapp = application.main:main']
    }
)