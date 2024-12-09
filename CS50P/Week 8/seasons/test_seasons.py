from seasons import calc_time


def test_calc_time():
    assert calc_time(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert calc_time(10477)=="Fifteen million, eighty-six thousand, eight hundred eighty minutes"

