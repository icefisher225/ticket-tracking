from typing import Any, Union

DEBUG_PRINT = True


def is_intable(*args, **kwargs) -> bool:
    for test in args:
        try:
            int(test)
        except Exception as e:
            dprint(e)
            return False
    return True


def dprint(*args, **kwargs) -> None:
    # Debug print function
    # all non-release print calls should use this function instead of standard print. Supports multiple arguments and auto-stringifying.
    if DEBUG_PRINT:
        for item in args:
            print(f"{item}", end=" ")
        print("")


def is_empty(item: Any, *args, **kwargs) -> bool:
    try:
        if item:
            return False
        else:
            return True
    except IndexError as idxErr:
        dprint(idxErr)
        return False


def prt_conv_hlpr(value, *args, **kwargs) -> str:
    # helper function to clean up prettyprint code
    if value > 9:
        return str(value)
    else:
        return "0" + str(value)


def month_num_to_ltr_conv(month: int, *args, **kwargs) -> str:
    """
    :month: int, month of year you want to convert
    :return: 3-letter-ified monthname based on number passed in
    """
    if type(month) is not int:
        raise TypeError(f"got {type(month)}, need <class 'int'>")
    try:
        conv_dict = {
            1: "jan",
            2: "feb",
            3: "mar",
            4: "apr",
            5: "may",
            6: "jun",
            7: "jul",
            8: "aug",
            9: "sep",
            10: "oct",
            11: "nov",
            12: "dec",
        }
        return conv_dict[month]
    except KeyError as ke:
        dprint(ke)
        raise ValueError("Month must be between 1 and 12.")
