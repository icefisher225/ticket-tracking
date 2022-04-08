from dataclasses import dataclass, field
from typing import Any, Union
from helperfunctions import *

import os, sys, math, datetime, time


@dataclass()
class _Time:
    """
    Class to represent a specific time value.
    Will initialize itself to instantiation time if no values given.
    :hour:   (int) hour value
    :minute: (int) minute value
    :second: (int) optional seconds value
    :return: None.
    """

    _hour: int = -1
    _minute: int = -1
    _second: Union(None, int) = None

    def __post_init__(self, *args, **kwargs) -> None:
        # Sets default values to instantiation time if not passed in
        if self._hour == -1 or self._minute == -1:
            # checks if the minute or hour was not set
            pass
        else:
            # if both were set, return b/c no change required
            return
        # if at least one was not set, set them both to instantiation time
        temp = time.localtime()
        self._hour = temp[3]
        self._minute = temp[4]
        # Never add a seconds value if it was not passed in
        # self._second = temp[5]

    def set_time(self, *args, **kwargs) -> None:
        # TODO: time setter to make user prompting easier
        pass

    def pretty_print(self, *args, **kwargs) -> str:
        hour, min = prt_conv_hlpr(self._hour), prt_conv_hlpr(self._minute)
        if self._second:
            return f"{hour}:{min}:{self._second}"
        else:
            return f"{hour}:{min}"

    def __str__(self, *args, **kwargs):
        return self.pretty_print()
