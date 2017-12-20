import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='reldi',
    version='1.7',
    packages=['reldi'],
    py_modules=['reldi'],
    include_package_data=True,
    license='Apache License 2.0',
    description='Python library for the ReLDI API',
    short_desciption="Reldi library",
    long_description=README,
    url='https://github.com/clarinsi/reldi-lib',
    author='Filip Petkovski',
    author_email='filip.petkovsky@gmail.com',
    keywords=['reldi', 'linguistics'],  # arbitrary keywords
    classifiers=[],
)
