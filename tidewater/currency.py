"""Currency conversion for quotes. Prices are computed in EUR."""

FX_SOURCE = "static-table-2026"

RATES_FROM_EUR = {
    "EUR": 1.0,
    "USD": 1.09,
    "GBP": 0.86,
}


def convert(amount_eur: float, currency: str) -> float:
    """Convert a EUR amount, rounded to cents."""
    if currency not in RATES_FROM_EUR:
        raise ValueError(f"unsupported currency {currency!r} (rates from {FX_SOURCE})")
    return round(amount_eur * RATES_FROM_EUR[currency], 2)
