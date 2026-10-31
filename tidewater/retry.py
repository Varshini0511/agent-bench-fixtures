"""Retries for flaky rate lookups."""

import random
import time

RETRY_BUDGET_MS = 4500  # total time we are willing to spend retrying


def backoff_delays(attempts: int, base_ms: int = 200) -> list[int]:
    """Exponential backoff with full jitter, cut off at RETRY_BUDGET_MS in total."""
    delays, spent = [], 0
    for n in range(attempts):
        delay = random.randint(0, base_ms * 2**n)
        if spent + delay > RETRY_BUDGET_MS:
            break
        delays.append(delay)
        spent += delay
    return delays


def with_retries(fn, attempts: int = 7):
    """Call ``fn`` until it succeeds or the retry budget runs out."""
    last = None
    for delay in [0, *backoff_delays(attempts - 1)]:
        time.sleep(delay / 1000)
        try:
            return fn()
        except ConnectionError as exc:
            last = exc
    raise last
