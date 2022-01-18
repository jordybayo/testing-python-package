import sys
import pytest
import mathematic.math_func as math_func


print(sys.version_info)


@pytest.mark.skipif(sys.version_info < (3, 3), reason="Do not run")
def test_adder():
    assert math_func.add(7, 3) == 10
    assert math_func.add(8, 2) == 10
    print(math_func.add(7, 3), "+++++++++++++++++++++")


@pytest.mark.skip(reason="do not run number add test")
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(8) == 10


@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(2) == 4


@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello', 'world')
    assert type(result) is str
    assert 'Hello' in result


@pytest.mark.parametrize('num1, num2, result', [
    (7, 3, 10),
    ('Hello', ' World', "Hello World"),
    (10.5, 25.5, 36)
])
def test_adding(num1, num2, result):
    assert math_func.add(num1, num2) == result


@pytest.mark.xfail
def test_add_strings_willfail():
    """On sait deja qu'il y'aura un echec"""
    result = math_func.add('Hello', 'world')
    assert type(result) is str
    assert 'Hello' in result


# def test_add_strings_invalid():
#     """Pour tester un echec"""
#     with pytest.raises(ValueError):
#         result = math_func.add('Hello', 'world')
#         assert type(result) is str
#         assert 'Hello' in result
