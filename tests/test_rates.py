import pytest

from tidewater.rates import compute_rate


def test_basic_rate():
    assert compute_rate(10, "harbor") == 15.0


def test_zone_multiplier():
    assert compute_rate(10, "island") == 27.0


def test_heavy_parcel_surcharge():
    # 20 kg is a heavy parcel: 20 * 1.5 + 6.0 surcharge
    assert compute_rate(20, "harbor") == 36.0


def test_rejects_non_positive_weight():
    with pytest.raises(ValueError):
        compute_rate(0, "harbor")
