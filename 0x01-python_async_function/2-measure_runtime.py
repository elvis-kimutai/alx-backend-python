#!/usr/bin/env python3
"""
 Measures the total execution time for
 wait_n(n, max_delay) and returns total_time / n.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns:
         float: Average time per iteration.
    """
    start_time = time.time()

    # Using asyncio.run to run the asynchronous function
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate average time per iteration
    average_time = total_time / n

    return average_time
