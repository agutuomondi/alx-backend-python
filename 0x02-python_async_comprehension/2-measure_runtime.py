#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Async Coroutine function that will execute async_comprehension
    four times in parallel using asyncio.gather.
    Coroutine will measure the total runtime and return it.
    '''

    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
