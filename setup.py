#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from setuptools import setup, find_packages
from glob import glob
from os.path import splitext, basename, abspath, dirname, join

here = abspath(dirname(__file__))
try:
    README = open(join(here, 'README.md')).read()
except:
    README = 'An add-on provider for the Python Faker module to generate random and/or fake data for music-related categories. See https://github.com/jeffwright13/faker_music.'

CLASSIFIERS = [
    # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: MIT',
    'Operating System :: Unix',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Utilities',
]

setup(
    name='faker_music',
    version='0.4',
    license='MIT',
    description='Provider of music-related data for Faker module',
    long_description=README,
    author='Jeff Wright',
    author_email='jeff.washcloth@gmail.com',
    url='https://github.com/jeffwright13/faker_music',
    packages=find_packages('faker_music'),
    package_dir={'': 'faker_music'},
    py_modules=[splitext(basename(path))[0] for path in glob('faker_music/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=CLASSIFIERS,
    project_urls={
        'Changelog': 'CHANGELOG.rst',
        'Issue Tracker': 'https://github.com/jeffwright13/faker_music/issues',
    },
    python_requires='>=3.6',
    install_requires=['Faker>=8.2.1'],
    test_requires=['pytest>=6.2', 'pytest-cov>=2.12.0'],
)
