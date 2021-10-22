import pytest

@pytest.fixture()
def setUp():
    print("Once before every method")

def test_method_A(setUp):
    print("Run method A")

def test_method_B(setUp):
    print("Run method B")