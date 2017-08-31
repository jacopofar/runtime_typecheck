try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='runtime_typecheck',
    long_description='Check the correspondence between a value and a Python 3.6 type at runtime',
    version='0.1',
    description='Check that a value satisfies a Python 3.6 type',
    author='Jacopo Farina',
    author_email='jacopo1.farina@gmail.com',
    license='MIT',
    packages=['runtime_typecheck'],
    url='https://github.com/jacopofar/runtime_typecheck',
    download_url='https://github.com/jacopofar/runtime_typecheck/archive/0.1.tar.gz'
)
