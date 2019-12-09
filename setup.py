"""A setuptools based setup module.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open

setup(
   name='movieCriticsOverTime',
   version='1.0',
   description='A module to analyze movie crtitic data and sentiment over time. Made for a class project.',
   author='Melinda Haughey/Jessica Liu/Olivia Li',
   author_email='mhaughey@uw.edu',
   packages=['moviecriticanalysis'],
   install_requires=['pandas', 'warnings', 'altair', 'matplotlib', 'NLTK', 'mpld3', 're'], #external packages as dependencies
)
