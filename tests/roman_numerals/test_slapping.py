import pytest

from roman_numerals.to_roman_numerals import to_roman_numerals


def test_decimal_number_is_negative_raises_value_error():
    with pytest.raises(ValueError):
        to_roman_numerals(-1)


@pytest.mark.parametrize("bad_argument", [
    2.4,
    "abc"
])
def test_decimal_number_is_not_an_int_raises_value_error(bad_argument):
    with pytest.raises(ValueError):
        to_roman_numerals(bad_argument)


@pytest.mark.parametrize("decimal_number, expected", [
    (1, "I"),
    (2, "II"),
    (3, "III")
])
def test_small_decimal_number_returns_is(decimal_number, expected):
    assert to_roman_numerals(decimal_number) == expected


def test_four_returns_iv():
    assert to_roman_numerals(4) == "IV"
