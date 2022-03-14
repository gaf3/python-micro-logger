#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name="python-micro-logger",
    version="0.1.1",
    package_dir = {'': 'lib'},
    py_modules = [
        'micro_logger',
        'micro_logger_unittest'
    ],
    install_requires=[
        'python-json-logger==2.0.2'
    ]
)
