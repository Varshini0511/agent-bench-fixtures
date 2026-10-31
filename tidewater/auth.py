"""Checks that a webhook really came from the carrier."""

import hashlib
import hmac


def verify_signature(payload: bytes, signature: str, secret: bytes) -> bool:
    """True if ``signature`` is the hex HMAC-SHA256 of ``payload`` under ``secret``."""
    expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)
