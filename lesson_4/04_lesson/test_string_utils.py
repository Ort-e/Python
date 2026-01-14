import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Проверка функции capitalize
@pytest.mark.positive_test
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("123abc", "123abc"),
        ("", ""),
        ("   ", "   "),
    ],
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Проверка функции trim
@pytest.mark.positive_test
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("  hello", "hello"),
        ("    world", "world"),
        ("no_spaces", "no_spaces"),
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("     ", ""),
        ("  hello world  ", "hello world  "),
    ],
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Проверка функции contains
@pytest.mark.positive_test
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("skypro", "k", True),
        ("hello", "h", True),
        ("world", "d", True),
    ],
)
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("skypro", "z", False),
        ("hello", "x", False),
        ("world", "a", False),
    ],
)
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# Проверка функции delete_symbol
@pytest.mark.positive_test
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "S", "kyPro"),
        ("SkyPro", "k", "SyPro"),
        ("hello world", "l", "heo word"),
    ],
)
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "K", "SkyPro"),
        ("hello", "z", "hello"),
    ],
)
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected