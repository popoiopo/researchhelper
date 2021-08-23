"""Setup the package."""

from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='researchhelper',
    author='Bas Chatel',
    author_email='bastiaan.chatel@gmail.com',
    description='A repository of useful functions supporting research.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='http://github.com/popoiopo/researchhelper',
    version='0.1.7',
)
