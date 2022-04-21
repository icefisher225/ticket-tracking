from datastructures import *
from helperfunctions import *

import pickle, math, time, datetime, os, sys

INSIGHTS = list()


def main():
    return 0


def new_insight(number, *args, **kwargs):
    global insight
    insight = Insight()
    INSIGHTS.append(insight)


if __name__ == "__main__":
    main()
