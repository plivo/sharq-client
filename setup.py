# -*- coding: utf-8 -*-
# Copyright (c) 2014 Plivo Team. See LICENSE.txt for details.
from setuptools import setup

setup(
    name='SharQClient',
    version='0.0.1-alpha',
    url='http://github.com/plivo/sharq-client',
    author='Plivo Team',
    author_email='hello@plivo.com',
    py_modules=['sharq_client'],
    license=open('LICENSE.txt').read(),
    description='SharQ Client',
    long_description=open('README.md').read(),
    install_requires=[
        'requests==2.3.0',
        'ujson==1.33'
    ],
)