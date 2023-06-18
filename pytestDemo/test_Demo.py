import pytest


@pytest.mark.smoke
def test_fun():
    print("Hello")


@pytest.mark.smoke
def test_disp():
    print("World")


@pytest.mark.skip
def test_assert():
    msg = "Hello"
    assert msg == "Hi"

@pytest.mark.xfail
def test_add():
    print("I am inside addition")
    assert True == False