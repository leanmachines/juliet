#!/usr/bin/python3

from setuptools import setup

setup(name='juliet',
      version='0.1-alpha2',
      description='The lightweight static website generator',
      url='http://github.com/hlef/juliet',
      author='Hugo Lefeuvre',
      author_email='hle@owl.eu.com',
      license='MIT',
      packages=['juliet'],
      entry_points={
          'console_scripts': [
              'juliet = juliet:main'
          ]
      },
      zip_safe=False,
      install_requires = ['jinja2>=2.7', 'pygments', 'pyyaml>=3.11', 'markdown',
      'python-slugify'],
      test_suite='nose.collector',
      tests_require=['nose'])
