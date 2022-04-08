from dataclasses import dataclass, field
from typing import Any, Union
from helperfunctions import *

import os, sys, math, datetime, time


@dataclass()
class Time:
    """
    Class to represent a specific time value.
    Will initialize itself to instantiation time if no values given.
    :hour:   (int) hour value
    :minute: (int) minute value
    :second: (int) optional seconds value
    :return: None.
    """

    hour: int = -1
    minute: int = -1
    second: int = None

    def __post_init__(self, *args, **kwargs) -> None:
        # Sets default values to instantiation time if not passed in
        if self.hour == -1 or self.minute == -1:
            # checks if the minute or hour was not set
            pass
        else:
            # if both were set, return b/c no change required
            return
        # if at least one was not set, set them both to instantiation time
        temp = time.localtime()
        self.hour = temp[3]
        self.minute = temp[4]
        # Never add a seconds value if it was not passed in
        # self._second = temp[5]

    def set_time(self, *args, **kwargs) -> None:
        # TODO: time setter to make user prompting easier
        pass

    def pretty_print(self, *args, **kwargs) -> str:
        hour, min = prt_conv_hlpr(self.hour), prt_conv_hlpr(self.minute)
        if self.second:
            return f"{hour}:{min}:{self.second}"
        else:
            return f"{hour}:{min}"

    def __str__(self, *args, **kwargs):
        return self.pretty_print()


@dataclass()
class Date:
    year: int = -1
    month: int = -1
    day: int = -1

    def __post_init__(self, *args, **kwargs) -> None:
        temp = time.localtime()
        # TODO: Finish this. Need to move more stuff before spending more time here.
        if self.year == -1 or self.month == -1 or self.day == -1:
            # check if values passed in. If not, set to instantiation date.
            pass
        else:
            if self.year == temp[0] and self.month == temp[0] and self.day == temp[0]:
                # Catches if date agrees with current date
                # If so, returns as date is likely correct.
                return
            elif (self.year + 1 == temp[0] or self.year - 1 == temp[0]) and (
                self.month == 1 or self.month == 12
            ):
                # Checks to see if the year is off by 1 around New Year's
                # Goal: prevent issues around 01jan.
                pass
            else:
                # Check for wildly incorrect year
                # if caught, replaces with current year.
                self.year = temp[0]
        # TODO: Checks on month and day.
        self.year = temp[0]
        self.month = temp[1]
        self.day = temp[2]

    def _pp_month_conversion(self, *args, **kwargs) -> dict:
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
        return conv_dict[self.month]

    def _pp_day_conversion(self, *args, **kwargs) -> str:
        if self.day >= 10:
            return str(self.day)
        else:
            return "0" + str(self.day)

    def __str__(self, *args, **kwargs) -> str:
        return self.pretty_print(args, kwargs)

    def pretty_print(self, *args, **kwargs) -> str:
        # returns a date in format "daymonthyear" formatted like "02apr2022".
        return f"{self._pp_day_conversion()}{self._pp_month_conversion()}{self.year}"


@dataclass()
class Source:
    source: str = "sysmon"

    def __post_init__(self, *args, **kwargs) -> None:
        self._source = self.source.strip().lower()

    def __str__(self, *args, **kwargs) -> str:
        return self._prettyprint(args, kwargs)

    def _prettyprint(self, *args, **kwargs) -> str:
        return f"{self.source}"


@dataclass()
class Signal:
    name: str = ""
    source: Source = None
    details: list = None

    def __post_init__(self, *args, **kwargs):
        self.details = list()

    def add_details(self, *args, **kwargs) -> None:
        # pass in the additional details via *args
        # TODO: Make this better??? It seems too simple
        for item in args:
            self.details.append(str(item))

    def _prettyprint(self, *args, **kwargs):
        description = ""
        for line in self.details:
            description += f"{line}\n\t"
        return f"{self.name.capitalize()}\nSource: {self.source}\n\y{description}\n"

    def __str__(self, *args, **kwargs):
        return self._prettyprint(args, kwargs)
