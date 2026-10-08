from script import square
from script import radius

def main():
    test_square()
    test_radius()

def test_square():
    assert square(2) == 4, "Test failed: square(2) should be 4" # Assert é usado para verificar se uma condição é verdadeira. Se a condição for falsa, ele lança uma exceção AssertionError com a mensagem fornecida.
    assert square(-3) == 9, "Test failed: square(-3) should be 9"
    assert square(0) == 0, "Test failed: square(0) should be 0"
    print("All square tests passed!")

def test_radius():
    try:
        assert radius(1) == 3.141592653589793, "Test failed: radius(1) should be 3.141592653589793"
        assert radius(0) == 0, "Test failed: radius(0) should be 0"
        assert radius(2) == 12.566370614359172, "Test failed: radius(2) should be 12.566370614359172"
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")

if __name__ == "__main__":
    main()