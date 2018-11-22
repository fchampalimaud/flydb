import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='Fly DB',
    version=2.0,
    description='Application to manage flies stocks',
    long_description=README,
    author=[
        'Ricardo Ribeiro',
        'Hugo Cachitas'
    ],
    author_email=[
        'ricardo.ribeiro@research.fchampalimaud.org',
        'hugo.cachitas@research.fchampalimaud.org',
    ],
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
)
