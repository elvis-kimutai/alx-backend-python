#!/usr/bin/env python3
"""
  Asynchronous routine that spawns wait_random n
  times with the specified max_delay.
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Returns:
        list: List of delays (float values) in ascending order
    """
    list_of_delays = []
    for w in range(n):
        delays = await wait_random(max_delay)
        list_of_delays.append(delays)
    return sorted(list_of_delays)
