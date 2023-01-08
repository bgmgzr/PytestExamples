import pytest


@pytest.mark.group1
def test_method1():
    a = 5
    b = 6
    assert a == b, "test failed"


@pytest.mark.group2
def test_method2():
    a = 5
    b = 6
    assert b - 1 == a, "test failed"


@pytest.mark.group1
def test_method3():
    x = 1
    y = 100
    assert x * 100 == y
