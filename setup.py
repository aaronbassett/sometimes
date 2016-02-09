#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.1.3"

readme = open('README.rst').read()

setup(
    name='sometimes',
    version=version,
    description="""Stop being so black & white. Mix things up a bit and execute code sometimes.""",
    long_description=readme,
    author='Aaron Bassett',
    author_email='aaron@rawtech.io',
    url='https://github.com/aaronbassett/sometimes',
    packages=[
        'sometimes',
    ],
    include_package_data=True,
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords='sometimes',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
