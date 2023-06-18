import pytest



@pytest.mark.usefixtures("setup")
class Demo:
    def test_run(self):
        print("Hello")

    def test_run1(self):
        print("Am at 1st place, I'll be executed after first")

    def test_run2(setup):
        print("Am at 1st place, I'll be executed after first")

    def test_run3(setup):
        print("Am at 1st place, I'll be executed after first")
