import pytest
@pytest.fixture()
def city():
    print("in fixtures")
    cityy=["agra","bhopal","bang"]
    return cityy

def test_fix(city):
    print(city[1])
    assert city[0]=="agra"
    
@pytest.mark.xfail(reason="can't use fixtures return in this kind")
@pytest.mark.usefixtures
def test_fix2():
    assert 1==1
    assert city[0]=="agra"