# -*- coding: utf-8 -*-

import os
del os.link

from setuptools import setup, find_packages

setup(
    name='CuraSlicer',
    version='0.0.1',
    description='',
    packages=find_packages(),
    include_package_data=True,
    exclude_package_data={
        '': ['*.c', '*.cpp'],
    },
    entry_points={
    },
    ext_modules=cythonize([]),
    tests_require=[
    ],
    test_suite='nose.collector',
)

