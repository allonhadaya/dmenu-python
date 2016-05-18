from os import path

from setuptools import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='dmenu',
    version='0.1',
    description='A dmenu wrapper.',
    long_description=long_description,
    url='https://github.com/allonhadaya/dmenu',
    author='Allon Hadaya',
    author_email='self@allon.nyc',
    license='MIT',
    packages=['dmenu'],
    package_data={
        'dmenu': ['../README.md'],
    },
    include_package_data=True,
)
