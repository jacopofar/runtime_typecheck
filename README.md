# runtime typecheck
Checks that a value satisfies a Python 3.6 type at runtime

This code uses Python 3.6 type hints and the `typing` package to provide a simple runtime type check.

Example:

```python
    assert check_type((1, 67), Tuple[int, int])
    assert not check_type((1, "new york"), Tuple[int, int])
```

Currently not all of the components of Python 3.6 `typing` module are supported.