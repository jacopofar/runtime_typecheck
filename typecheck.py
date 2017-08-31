#!/usr/bin/env python3
from typing import (Union,
                    Tuple,
                    Any,
                    TypeVar,
                    Type,
                    List)


def check_type(obj, candidate_type, reltype='invariant') -> bool:

    if reltype not in ['invariant', 'covariant', 'contravariant']:
        raise ValueError(f' Variadic type {reltype} is unknown')

    # builtin type like str, or a class
    if type(candidate_type) == type and reltype in ['invariant']:
        return isinstance(obj, candidate_type)

    if type(candidate_type) == type and reltype in ['covariant']:
        return issubclass(obj.__class__, candidate_type)

    if type(candidate_type) == type and reltype in ['contravariant']:
        return issubclass(candidate_type, obj.__class__)

    # Any accepts everything
    if type(candidate_type) == type(Any):
        return True

    # Union, at least one match in __args__
    if type(candidate_type) == type(Union):
        return any(check_type(obj, t, reltype) for t in candidate_type.__args__)

    # Tuple, each element matches the corresponding type in __args__
    if type(candidate_type) == type(Tuple):
        if not hasattr(obj, '__len__'):
            return False
        if len(candidate_type.__args__) != len(obj):
            return False
        return all(check_type(o, t, reltype) for (o, t) in zip(obj, candidate_type.__args__))

    # List, each element matches the type in __args__
    if type(candidate_type) == type(List):
        if not hasattr(obj, '__len__'):
            return False
        return all(check_type(o, candidate_type.__args__[0], reltype) for o in obj)

    # TypeVar, this is tricky
    if type(candidate_type) == type(TypeVar):
        # TODO consider contravariant, variant and bound
        # invariant with a list of constraints, acts like a Tuple
        if not (candidate_type.__covariant__ or candidate_type.__contracovariant__) and len(candidate_type.__constraints__) > 0:
            return any(check_type(obj, t) for t in candidate_type.__constraints__)

    if type(candidate_type) == type(Type):
        return check_type(obj, candidate_type.__args__[0], reltype='covariant')

    raise ValueError(f'Cannot check against {reltype} type {candidate_type}')


assert check_type(3, Any)
assert check_type([5, "hi"], Any)


assert check_type(3, int)
assert not check_type(3, float)

assert check_type(3, Union[int, str])
assert check_type("hello", Union[int, str])
assert not check_type(4.78, Union[int, str])

assert check_type((1, 67), Tuple[int, int])
assert not check_type((1, "new york"), Tuple[int, int])
# NOTE not a tuple, but the whole object is immutable being a JSON received from HTTP
assert check_type([1, "new york"], Tuple[int, str])

assert check_type((1, 67, "Amsterdam"), Tuple[int, int, str])
assert not check_type(("Amsterdam", 1, 67), Tuple[int, int, str])


assert check_type([1, 27, 33, 1956], List[int])
assert not check_type([1.11, 27, 33, 1956], List[int])
assert not check_type([1, 27, 33, 1956, "h", 42], List[int])


assert check_type([1, 27, 33, 1956], List[Union[str, int]])
assert check_type([(12, "Texas"), (-5, "Particle")], List[Tuple[int, str]])
assert not check_type([(1.9, "Texas"), (-5, "Particle")], List[Tuple[int, str]])

assert not check_type([1.11, 27, 33, 1956], List[Tuple[int, str]])
