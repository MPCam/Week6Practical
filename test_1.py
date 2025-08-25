import pytest
from Example1 import safe_divide


@pytest.mark.parametrize(
    "a,b,expected", [
        (6, 2, 3.0),
        (5, 0, float('inf')),
        (-10, -2, 5.0)
    ]
)
def test_safe_divide(a, b, expected):
    assert safe_divide(a, b) == expected

