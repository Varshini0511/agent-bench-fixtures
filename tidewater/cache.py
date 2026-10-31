"""A small in-memory cache for quotes."""

import time

TTL_SECONDS = 90


class TTLCache:
    def __init__(self, ttl: float = TTL_SECONDS):
        self.ttl = ttl
        self._items: dict[str, tuple[float, object]] = {}

    def get(self, key: str):
        hit = self._items.get(key)
        if hit is None:
            return None
        stored_at, value = hit
        if time.monotonic() - stored_at > self.ttl:
            del self._items[key]
            return None
        return value

    def put(self, key: str, value) -> None:
        self._items[key] = (time.monotonic(), value)
