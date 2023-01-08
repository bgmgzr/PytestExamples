import pytest


@pytest.mark.square
@pytest.mark.parametrize("xEdge, yEdge", [(30, 10), (20, 20)])
def test_squareArea(xEdge, yEdge):
    x = xEdge
    y = yEdge
    area = x * y
    assert area == x * x, "Failed: Not Square"
