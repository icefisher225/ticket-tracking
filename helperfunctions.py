import typing

DEBUG_PRINT = True


def is_intable(*args) -> typing.Union(Exception, bool):
    for test in args:
        try:
            int(test)
        except Exception as e:
            return False
    return True


def dprint(*args) -> None:
    # Debug print function
    # all non-release print calls should use this function instead of standard print. Supports multiple arguments and auto-stringifying.
    if DEBUG_PRINT:
        for item in args:
            print(f"{item}", end=" ")
        print("")


def is_empty(item: typing.Any) -> bool:
    try:
        if item:
            return False
        else:
            return True
    except IndexError as idxErr:
        dprint(idxErr)
        return False


def prt_conv_hlpr(value, *args, **kwargs):
    # helper function to clean up prettyprint code
    if value > 9:
        return value
    else:
        return "0" + str(value)
