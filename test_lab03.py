import pytest
import sys
pytestmark=pytest.mark.skipif(sys.platform!="linux",reason="will only run in windows")
def test_01():
    assert type(1.0)==float
