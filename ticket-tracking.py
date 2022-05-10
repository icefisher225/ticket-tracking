import pickle, math, time, datetime, os, sys

from datastructures import *
from helperfunctions import *

INSIGHTS = list()


def main():
    while True:
        user_in = input("Input: ")
        if user_in.lower().strip() == "exit" or user_in.lower().strip() == "quit":
            break
        elif user_in.lower().strip() == "new":
            new_insight()


def new_insight(*args, **kwargs):
    number = input("Number: ")
    tme = input("Time: ")
    dte = input("Date: ")
    host = input("Host: ")
    user = input("User: ")
    entity = input("Entity: ")
    insight = Insight(number, host, user, entity, dte, tme, None, None, None)
    print(insight)


if __name__ == "__main__":
    main()
