try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='runtime_typecheck',
    long_description='Runtime type checking with Python 3.6 typing functions',
    version='0.3',
    description='Runtime type checking with Python 3.6 typing',
    author='Jacopo Farina',
    author_email='jacopo1.farina@gmail.com',
    license='MIT',
    packages=['runtime_typecheck'],
    url='https://github.com/jacopofar/runtime_typecheck',
    download_url='https://github.com/jacopofar/runtime_typecheck/archive/0.2.tar.gz'
)
