import pytest
from working import convert

def test_convert():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("10:30 PM to 8 AM")=="22:30 to 08:00"

def test_value_error():
    with pytest.raises(ValueError):
        convert("10:30 PM - 8 AM")
    with pytest.raises(ValueError):
        convert("10:30PM to 8AM")
    with pytest.raises(ValueError):
        convert("15:30 AM to 25:00 PM")
    with pytest.raises(ValueError):
        convert("10:65 PM to 8:66 AM")
    with pytest.raises(ValueError):
        convert("10:30 to 8")
