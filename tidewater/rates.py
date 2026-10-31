"""Parcel pricing."""

from tidewater.zones import zone_multiplier

BASE_RATE_PER_KG = 1.5  # EUR
HEAVY_PARCEL_KG = 20
HEAVY_SURCHARGE = 6.0  # EUR, for parcels of HEAVY_PARCEL_KG and above


def compute_rate(weight_kg: float, zone: str) -> float:
    """Price in EUR for a parcel of ``weight_kg`` shipped to ``zone``."""
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    price = weight_kg * BASE_RATE_PER_KG * zone_multiplier(zone)
    if weight_kg >= HEAVY_PARCEL_KG:
        price += HEAVY_SURCHARGE
    return round(price, 2)
