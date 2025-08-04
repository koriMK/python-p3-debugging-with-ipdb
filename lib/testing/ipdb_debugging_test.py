import pytest
from ipdb_debugging import adds_two

def test_adds_two():
    assert adds_two(3) == 5
    assert adds_two(-1) == 1
    assert adds_two(0) == 2