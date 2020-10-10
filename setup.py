#!/usr/bin/env python

import os
import sys
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()



setup(
    name='precisely',
    version='0.1.9',
    description='Rich matchers, useful for assertions in tests. Inspired by Hamcrest.',
    long_description=read("README.rst"),
    author='Michael Williamson',
    author_email='mike@zwobble.org',
    url='http://github.com/mwilliamson/python-precisely',
    packages=['precisely'],
    keywords="matcher matchers",
    install_requires=[],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    license="BSD-2-Clause",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
