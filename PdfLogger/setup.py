#!/usr/bin/env python
from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pdf-latex',
      version=version,
      description="Log your experiment scripts and result figures to pdf.",
      long_description="""\
Log your experiment scripts and result figures from 
the command line and directly to a nicely formatted pdf.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Python Pdf Log LaTeX',
      author='Johannes Alneberg',
      author_email='johannesalneberg@gmail.com',
      url='www.github.com/alneberg/pdf-logger',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
