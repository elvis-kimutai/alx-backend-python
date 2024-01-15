#!/usr/bin/env python3
"""
  Asynchronous coroutine that waits for a random
  delay between 0 and max_delay seconds.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    functions that return random float numbers
    """

    time_delayed = random.uniform(0, max_delay)
    await asyncio.sleep(time_delayed)
    return time_delayed
