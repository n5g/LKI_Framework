"""
file name should start with test
test method name should start with test

py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module

-s to print statements
-v verbose
"""

import pytest

@pytest.fixture()
def setUp():
    print("Once before every method - 150")
    yield
    print("Once After every method - 150")

def test_150_method_A(setUp):
    print("Run 150 method A")

def test_150_method_B(setUp):
    print("Run 150 method B")