from dataclasses import dataclass
from tkinter import *
from tkinter.ttk import *


def insight_num(number):
    return f"Insight-{number}"


def place_obj(object, col, rw):
    object.grid(column=col, row=rw)


class MyButton(Button):
    def __init__(self, *args, **kwargs):
        pass


def main():
    return 0


if __name__ == "__main__":
    main()
