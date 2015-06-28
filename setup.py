# -*- coding: utf-8 -*-

import os
del os.link

from setuptools import setup, find_packages

setup(
    name='CuraSlicer',
    version='0.0.2',
    description='',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
    },
    tests_require=[
    ],
    test_suite='nose.collector',
)

