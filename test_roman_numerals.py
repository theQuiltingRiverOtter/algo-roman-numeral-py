from roman_numerals import to_roman
import pytest


def test_01_a_single_number():
    assert to_roman(1) == "I"


def test_02_multiple_entries():
    assert to_roman(3) == "III"


def test_03_odd_numerals():
    assert to_roman(4) == "IV"


def test_04_all_edge_cases():
    assert to_roman(944) == "CMXLIV"


def test_05_44():
    assert to_roman(44) == "XLIV"


def test_06_19():
    assert to_roman(19) == "XIX"


# add tests to cover different edge cases
