# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()
    
with open('requirements.txt') as f: 
    require = [i.replace('\n', '') for i in f.readlines()]
    
setup (
    name='nlp_utils',
    version='0.1.0',
    description='A collection of utility function for NLP projects',
    long_description=readme,
    author='thuan.nguyen',
    author_email='thuan.hieu301@gmail.com',
    url='https://github.com/thuanthan258/nlp_utils',
    packages=find_packages(exclude=('test', 'doc'))
)