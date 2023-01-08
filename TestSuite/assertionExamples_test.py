import pytest


def test_assertion_method1():
    a = 5
    b = 6
    assert a == b, "Test failed: a=" + str(a) + " not equal to" + " b=" + str(b)


def test_assertion_method2():
    assert True


def test_assertion_method3():
    assert False, "Always Fails"


def test_assertion_method4():
    assert "apple" == "orange"
