import os, sys, math, datetime, time

from typing import Any, Union

from helperfunctions import *


class _Time:
    # Class to represent time. Called by _Time(Hour, Minute, Second)
    def __init__(self, hour=0, minute=0, second=0) -> Union(None, Exception):
        if is_intable(hour, minute, second):
            pass
        else:
            return TypeError(
                f"Require int, int, int. Got {type(hour)}, {type(minute)}, {type(second)}"
            )
        self._hour = int(hour) % 24
        self._minute = int(minute) % 60
        self._second = int(second) % 60

    def pretty_print(self, *args, **kwargs) -> str:
        hour, min = prt_conv_hlpr(self._hour), prt_conv_hlpr(self._minute)
        if self.second:
            return f"{hour}:{min}:{prt_conv_hlpr(self.second)}"
        else:
            return f"{hour}:{min}"


class _Date:
    def __init__(
        self, year=0, month=0, day=0, *args, **kwargs
    ) -> Union(None, Exception):
        # Function returns if types are wrong, else returns nothing. Initializes an instance of a private "_Time" class.
        # This class should not be used out of this specific context.
        if (type(month) is int) and (type(day) is int) and (type(year) is int):
            pass
        else:
            return TypeError("month, day, year must be type int.")
        self._day = day
        self._month = month
        self._year = year

    def _pp_year_conversion(self, *args, **kwargs) -> str:
        # returns stringified year and converts to 20xx if just xx entered.
        if self._year > 99:
            return str(self._year)
        else:
            # catch if the year was entered as "22" instead of "2022" and fix
            return str(self._year + 2000)

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
        return conv_dict[self._month]

    def _pp_day_conversion(self, *args, **kwargs) -> str:
        if self._day >= 10:
            return str(self._day)
        else:
            return "0" + str(self._day)

    def __str__(self, *args, **kwargs) -> str:
        return self.pretty_print(args, kwargs)

    def pretty_print(self, *args, **kwargs) -> str:
        # returns a date in format "daymonthyear" formatted like "02apr2022".
        return f"{self._pp_day_conversion()}{self._pp_month_conversion()}{self._pp_year_conversion()}"


class _Source:
    def __init__(self, *args, **kwargs):
        """
        Takes in the source of the signal as the first argument.
        """
        if is_empty(args) and is_empty(kwargs):
            self._source = "sysmon"
        else:
            self._source = str(args[0]).strip()

    def __str__(self, *args, **kwargs):
        return self.prettyprint(args, kwargs)

    def prettyprint(self, *args, **kwargs):
        return f"{self._source}"


class Signal:
    def __init__(self, name, *args, **kwargs):
        """
        name: Name of the relevant signal (Eventually, autosuggestion?)
        *args: pass in a string that corresponds to the alert/log source IFF the signal is not directly from Sumo CSE. Sample strings include "atp", "aws" or "fortigate".
        """
        self._name = name
        self._details = list()
        self._source = _Source(args[0])

    def add_details(self, info, *args, **kwargs):
        # this function adds details about the signal, one line at a time.
        # TODO: considering a second handler to wrap this one.
        self._details.append(str(info))

    def prettyprint(self, *args, **kwargs):
        # Includes blank line after body
        description = ""
        for line in self._details:
            description += f"{line}\n\t"
        return f"{str(self._name).capitalize()}\n\tSource: {str(self._source)}\n\t{description}\n"

    def __str__(self, *args, **kwargs):
        return self.prettyprint()


class Insight:
    def __init__(
        self,
        number=0,
        host="Unknown",
        user="Unknown",
        entity=False,
        *args,
        **kwargs,
    ):
        """
        :number: Insight number
        :host: Relevant host
        :user: Relevant user
        :entity: What entity the insight triggered on. Can be host, IP, user, etc.
        kwargs:
            :creation_hour: Hour the insight was created at
            :creation_minute: Minute the insight was created at
            :creation_second: Second the insight was created at
            :creation_day: Day the insight was created on. Defaults to today.
            :creation_month: Month the insight was created in. Defaults to current month.
            :creation_year: Year the insight was created in. Defaults to current year.
            :activity_hour: Hour the activity took place
            :activity_minute: Minute the activity took place
            :activity_second: Second the activity took place
        """
        self._number = number
        self._host = host
        self._user = user
        self._date = None  # _Date class
        self._time = None  # _Time class
        self._activity_time = None  # _Time class
        self._datetime_dict = {
            "creation_hour": 0,
            "creation_minute": 0,
            "creation_second": 0,
            "creation_day": 0,
            "creation_month": 0,
            "creation_year": 0,
            "activity_hour": 0,
            "activity_minute": 0,
            "activity_second": 0,
        }
        if entity is False:
            self._entity = host
        else:
            self._entity = entity
        self._signals = (
            list()
        )  # create empty list of signals - specific to Sumo Logic/Exabeam(ish). Other SIEMs: one signal per alert.

    def _set_creation_datetime(self, *args, **kwargs) -> None:
        if not kwargs:
            temp = time.localtime()()
            self._date = _Date(temp[0], temp[1], temp[2])
            self._time = _Time(temp[3], temp[4], temp[5])
        # TODO: check if this even works
        else:
            for key in kwargs.keys:
                dprint(f"{key}:{kwargs[key]}")
                if key in self._datetime_dict.keys:
                    self._datetime_dict[key] = str(kwargs[key])

    def _header_out(self) -> str:
        return f"Insight {self._number}\n{self._time} {self._date}\nHost: {self._host}\nUser: {self._user}\nEntity: {self._entity}"

    def _prettyprint(self) -> str:
        return f"Insight-{self._number}\n{self._time} {self._date}"
        pass

    def __str__(self, *args, **kwargs) -> str:
        return self._prettyprint()
