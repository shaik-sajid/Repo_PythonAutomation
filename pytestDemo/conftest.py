import pytest


@pytest.fixture(scope="class")
def setup():
    print(''' I"ll be executed first''')
    yield
    print("I'll be executed last")


@pytest.fixture(scope="class")
def data():
    return ["Shaik", "Sajid", "skbsajid365@gmail.com"]


@pytest.fixture(params=[("Chrome1", "Chrome2"), "Firefox", "Edge"])
def crossBrowser(request):
    return request.param
