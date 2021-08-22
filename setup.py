"""Setup the package."""

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    author='Bas Chatel',
    author_email='bastiaan.chatel@gmail.com',
    description='A repository of useful functions supporting research.',
    long_description=long_description,
    long_description_content_type='text/x-rst',  # This is important!
    name='researchhelper',
    url='http://github.com/popoiopo/researchhelper',
    version='0.1.6',
)
