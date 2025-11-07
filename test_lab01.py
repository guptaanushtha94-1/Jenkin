import pytest
def test_a1():
    assert 1+1==2
def test_a2():
    print("this is first")
    assert 10/10==1
@pytest.mark.skip(reason="skipping intentionally")
def test_a3():
    assert 9//5==1

