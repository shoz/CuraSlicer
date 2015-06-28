# -*- coding: utf-8 -*-

import os
del os.link

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    req = f.readlines()


setup(
    name='CuraSlicer',
    version='0.0.2',
    description='',
    packages=find_packages(),
    include_package_data=True,
    install_requires=req,
    tests_require=[],
    test_suite='nose.collector',
)

