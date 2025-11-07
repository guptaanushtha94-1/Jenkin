import pytest
@pytest.mark.parametrize("a,b,c",[(1,2,3),(2,4,7)])
def test_par(a,b,c):
    assert a+b==c