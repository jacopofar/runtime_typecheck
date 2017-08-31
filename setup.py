try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='typecheck',
    version='0.1',
    description='Check that a value satisfies a Python 3.6 type',
    author='Jacopo Farina',
    license='MIT',
    packages=['typecheck']
)
