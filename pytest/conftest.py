import pytest


@pytest.fixture()
def setUp():
    print("Once before every method ")
    yield
    print("Once After every method")

@pytest.fixture(scope="module")
def oneTimeSetUp():
    print("oneTimeSetUp  before every method ")
    yield
    print("oneTimeSetUp  After every method")