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
