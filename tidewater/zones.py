"""Delivery zones and their price multipliers."""

ZONE_MULTIPLIERS = {
    "harbor": 1.0,
    "inland": 1.25,
    "island": 1.8,
    "remote": 2.4,
}


def zone_multiplier(zone: str) -> float:
    """Price multiplier for ``zone``; unknown zones are an error, not a default."""
    try:
        return ZONE_MULTIPLIERS[zone]
    except KeyError:
        known = ", ".join(sorted(ZONE_MULTIPLIERS))
        raise ValueError(f"unknown zone {zone!r}; expected one of: {known}") from None
