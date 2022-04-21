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

    def __str__(self, *args, **kwargs) -> str:
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

    def _pp_day_conversion(self, *args, **kwargs) -> str:
        if self.day >= 10:
            return str(self.day)
        else:
            return "0" + str(self.day)

    def __str__(self, *args, **kwargs) -> str:
        return self._pretty_print(args, kwargs)

    def _pretty_print(self, *args, **kwargs) -> str:
        # returns a date in format "daymonthyear" formatted like "02apr2022".
        return (
            f"{self._pp_day_conversion()}{month_num_to_ltr_conv(self.month)}{self.year}"
        )


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

    def _prettyprint(self, *args, **kwargs) -> str:
        description = ""
        for line in self.details:
            description += f"{line}\n\t"
        return f"{self.name.capitalize()}\nSource: {self.source}\n\y{description}\n"

    def __str__(self, *args, **kwargs) -> str:
        return self._prettyprint(args, kwargs)


@dataclass()
class Entity:
    name: str = ""
    _set: bool = None

    def __post_init__(self, *args, **kwargs) -> None:
        if self.name == "":
            self._set = False

    def set_name(self, name, *args, **kwargs) -> None:
        self.name = str(name)

    def prettyprint(self, *args, **kwargs) -> str:
        return str(self.name)

    def __str__(self, *args, **kwargs) -> str:
        return self.prettyprint()


@dataclass()
class Object:
    name: str

    @property
    def set_name(self, nm, *args, **kwargs) -> None:
        self.name = nm

    def prettyprint(self, *args, **kwargs) -> str:
        return self.name

    def __str__(self, *args, **kwargs) -> str:
        return self.prettyprint()


@dataclass()
class Host(Object):
    pass


@dataclass()
class User(Object):
    pass


@dataclass()
class CloseCode:
    # Close Code class, only option is the code.
    # Sumo Logic uses "False Positive", "resolved", "No Action", "Duplicate".
    code: str

    def _prettyprint(self):
        return f"{self.code}"

    def __str__(self):
        return self._prettyprint()


@dataclass()
class Duplicate(CloseCode):
    dupe: str

    def _prettyprint(self):
        return f"{self.code} of {self.dupe}"


@dataclass()
class Insight:
    number: int = 0
    _host: Host = None
    _user: User = None
    _entity: Entity = None
    _date: Date = None
    _time: Time = None
    _activity_time: Time = None
    _signals: list = None
    _close_code: CloseCode = None

    """
    :number: Insight number
    :host: Relevant host
    :user: Relevant user
    :entity: What entity the insight triggered on. Can be host, IP, user, etc.
    """
    # TODO: Timing. Was kwarg-based, now something else is necessary.

    def __post_init__(self, *args, **kwargs):
        self.signals = list()
        # TODO: what else needs to be initialized?

    @property
    def set_host(self, host: str, *args, **kwargs) -> None:
        self._host = Host(host)

    @property
    def get_host(self, *args, **kwargs):
        return str(self._host)

    @property
    def set_user(self, user: str, *args, **kwargs) -> None:
        self._user = User(user)

    @property
    def get_user(self, *args, **kwargs):
        return str(self._user)

    @property
    def set_entity(self, entity: str, *args, **kwargs) -> None:
        self._entity = Entity(entity)

    @property
    def set_date(self, year=-1, month=-1, day=-1, *args, **kwargs) -> None:
        self._date = Date(year, month, day)

    @property
    def get_date(self, *args, **kwargs) -> str:
        return str(self._date)

    @property
    def set_time(self, hour=-1, minute=-1, second=None, *args, **kwargs) -> None:
        self._time = Time(hour, minute, second)

    @property
    def get_time(self, *args, **kwargs) -> str:
        return str(self._time)

    @property
    def set_act_time(self, hour=-1, minute=-1, second=None, *args, **kwargs) -> None:
        self._activity_time = Time(hour, minute, second)

    @property
    def get_act_time(self, *args, **kwargs) -> str:
        return str(self._activity_time)

    @property
    def add_signal(self, sig: Signal, *args, **kwargs) -> None:
        """
        :sig: Signal object
        :return: None
        """
        self._signals.append(sig)

    @property
    def get_signals(self, *args, **kwargs) -> str:
        # TODO: Fix this, it definitely does not work
        ret = ""
        for sig in self._signals:
            ret += f"{sig}\n"
        return ret
