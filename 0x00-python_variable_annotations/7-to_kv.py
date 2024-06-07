#!/usr/bin/env python3
"The python enviroment"


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    "Complex types - string and int/float to tuple"
    state = k, float(v ** 2)
    return (state)
