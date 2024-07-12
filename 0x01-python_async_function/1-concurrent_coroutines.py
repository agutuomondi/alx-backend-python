#!/usr/bin/env python3

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    delayed_tasks = []  # init empty list to store delayed tasks
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = asyncio.as_completed(tasks)
    for task in completed:
        result = await task
        delayed_tasks.append(result)
    return delayed_tasks
