import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/10")==10
    assert convert("10/10")==100
    assert convert("5/10")==50
    assert convert("3/10")==30


def test_gauge():
    assert gauge(1)=="E"
    assert gauge(99)=="F"
    assert gauge(50)=="50%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("3/1")
