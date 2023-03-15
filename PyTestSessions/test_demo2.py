import pytest

def test_m2():
    a = 10
    b = 10
    c = 15
    assert a + b == c, "Test Failed"

@pytest.mark.execute
def test_m3():
    a="Rutuja"
    b="Rohini"
    assert a==b, "Test Fail"