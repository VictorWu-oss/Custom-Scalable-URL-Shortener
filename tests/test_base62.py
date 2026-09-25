import pytest

from url_shortener.base62 import encode


def test_base62_encodes_zero_and_positive_numbers() -> None:
    assert encode(0) == "0"
    assert encode(61) == "Z"
    assert encode(62) == "10"


def test_base62_rejects_negative_numbers() -> None:
    with pytest.raises(ValueError):
        encode(-1)

