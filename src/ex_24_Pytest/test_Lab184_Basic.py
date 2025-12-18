import pytest
@pytest.mark.smoke
def test_method1():
    print('Hello world')
    assert 5==5

@pytest.mark.smoke
def test_method2():
    print('Hello world')
    assert 5==6