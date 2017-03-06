#!/usr/bin/env python

from pyvultr.meta import (__version__, __description__, __author__,
                          __author_email__, __url__)
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'pyvultr',
    'pyvultr.cmd',
    'pyvultr.lib'
]

requires = open("requirements/base.txt").read().split()

setup(
    name='pyvultr',
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'pyvultr': 'pyvultr'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ),
)
