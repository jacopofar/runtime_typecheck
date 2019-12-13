.. image:: https://travis-ci.org/jacopofar/runtime_typecheck.svg?branch=master
    :target: https://travis-ci.org/jacopofar/runtime_typecheck
    :alt: Travis CI badge

.. image:: https://badge.fury.io/py/runtime_typecheck.svg
    :target: https://badge.fury.io/py/runtime_typecheck
    :alt: pypy version badge

runtime typecheck
#################

## __NOTE:__ this was fun to implement and I learned a lot about Python type metadata, but if you are looking for a runtime type checker look at `Pydantic<https://pydantic-docs.helpmanual.io/>`_

Checks that a value satisfies a Python 3.6 type at runtime

This code uses Python 3.6 type hints and the `typing` package to provide a simple runtime type check.


The check can be done explicitly calling the `check_type` function or with the `@check_args` function decorator which raises an exception when the argument passed to the function do not match the type hints

Example:

.. code-block:: python

    from runtime_typechecker import check_type, check_args
    from typing import Tuple
    assert check_type((1, 67), Tuple[int, int])
    assert not check_type((1, "new york"), Tuple[int, int])
    
    @check_args
    def dummy_fun(a: int = 0, b: str = '', c: Tuple[int, str] = (0, '')) -> int:
        return a + len(b) + c[0] + len(c[1]) + 7
    # this will throw a TypeException with the list of the issues. The decorated function is not even called in this case
    dummy_fun(a='1', c=(1,42))
    # this will work
    dummy_fun(a=3)


Currently not all of the components of Python 3.6 `typing` module are supported, more coming.
