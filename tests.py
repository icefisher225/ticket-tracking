from helperfunctions import *


def test_month_conv(month):
    tmp = ""
    for i in range(1, 13):
        print(i)
        tmp += f"{month_num_to_ltr_conv(i)} "
    assert tmp == "jan feb mar apr may jun jul aug sep oct nov dec "
