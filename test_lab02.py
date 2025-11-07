import pytest
class Test_c1:
    def test_a4(self):
        assert type(10)==int
    def test_a5(self):
        assert type(1.3)==float


class Test_c2:
    def test_a6(self):
        with pytest.raises(Exception) as E:
            assert (1/0)
        print(E)
