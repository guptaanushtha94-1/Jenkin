import pytest
lst1=["mon","tue","wed"]
lst2=["fri","sat","sun"]
@pytest.fixture()
def setup():
    v1=lst1.copy()
    v1.append("thu")
    yield v1
    print("after yield, teardown")
    v1.pop()
def test_a1(setup):
    setup.extend(lst2)
    assert setup==["mon","tue","wed","thu","fri","sat","sun"]
