#!/usr/bin/env python

from setuptools import setup

setup(
    name="dribbble",
    version="0.2",
    description="An easy-to-use Python wrapper for the Dribbble API.",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    url="http://github.com/zachwill/dribbble",
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    packages=[
        "dribbble"
    ],
    install_requires=[
        "requests",
        "simplejson"
    ]
)
