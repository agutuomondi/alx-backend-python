#!/usr/bin/env python3

from typing import Mapping, Any, TypeVar, Union, Optional

# Define a TypeVar for the default value
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[Union[T, None]] = None
                     ) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
