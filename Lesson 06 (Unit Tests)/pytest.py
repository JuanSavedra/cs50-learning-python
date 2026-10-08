import pytest # Biblioteca para realizar testes unitários em Python
from script import square, radius # Importa as funções square e radius do módulo script

def test_square():
    assert square(2) == 4, "Test failed: square(2) should be 4"
    assert square(-3) == 9, "Test failed: square(-3) should be 9"
    assert square(0) == 0, "Test failed: square(0) should be 0"

def test_radius():
    assert radius(1) == 3.141592653589793, "Test failed: radius(1) should be 3.141592653589793"
    assert radius(0) == 0, "Test failed: radius(0) should be 0"
    assert radius(2) == 12.566370614359172, "Test failed: radius(2) should be 12.566370614359172"

def test_exception():
    with pytest.raises(ValueError):
        radius(-1)  # Testa se a função radius lança uma exceção ValueError para um raio negativo