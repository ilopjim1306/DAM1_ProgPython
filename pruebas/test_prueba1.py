import pytest
from prueba1 import mayor

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (6, 3, 6),
    (3, 6, 6),
    ]
)
def test_suma_params(input_n1, input_n2, expected):
    assert mayor(input_n1, input_n2) == expected