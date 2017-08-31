from typing import Union, Tuple, Any, TypeVar, Type, List

from runtime_typecheck.runtime_typecheck import check_type


def test_any():
    assert check_type(3, Any)
    assert check_type([5, "hi"], Any)


def test_numbers():
    assert check_type(3, int)
    assert not check_type(3, float)


def test_unions():
    assert check_type(3, Union[int, str])
    assert check_type("hello", Union[int, str])
    assert not check_type(4.78, Union[int, str])


def test_tuples():
    assert check_type((1, 67), Tuple[int, int])
    assert not check_type((1, "new york"), Tuple[int, int])
    # NOTE not a tuple, but the whole object is immutable
    # being a JSON received from HTTP
    assert check_type([1, "new york"], Tuple[int, str])
    assert check_type((1, 67, "Amsterdam"), Tuple[int, int, str])
    assert not check_type(("Amsterdam", 1, 67), Tuple[int, int, str])


def test_lists():
    assert check_type([1, 27, 33, 1956], List[int])
    assert not check_type([1.11, 27, 33, 1956], List[int])
    assert not check_type([1, 27, 33, 1956, "h", 42], List[int])


def test_nested_types():
    assert check_type([1, 27, 33, 1956], List[Union[str, int]])
    assert check_type([(12, "Texas"), (-5, "Particle")], List[Tuple[int, str]])
    assert not check_type([(1.9, "Texas"), (-5, "Particle")],
                          List[Tuple[int, str]])
    assert not check_type([1.11, 27, 33, 1956], List[Tuple[int, str]])
