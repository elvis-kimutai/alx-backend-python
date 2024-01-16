#!/usr/bin/env python3
"""
write a measure_runtime coroutine that will
execute async_comprehension four times in parallel
using asyncio.gather
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ run four times in parallel using asyncio.gather"""
    start = time.perf_counter()
    coroutines = []
    for idx in range(4):
        coroutines.append(async_comprehension())
    await asyncio.gather(*coroutines)
    end = time.perf_counter()
    return end - start
