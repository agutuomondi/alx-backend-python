#!/usr/bin/env python3

"""Module that augment correct duck-typed annotations.
"""

from typing import List, Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function returns either an element from input_list or 'None'.
    """

    if lst:
        return lst[0]
    else:
        return None
