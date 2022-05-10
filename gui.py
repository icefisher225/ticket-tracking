from datastructures import *
from helperfunctions import *

from tkinter import *
from tkinter.ttk import *


def _insight_num(number):
    return f"Insight-{number}"


def _place_obj(object, col, rw):
    object.grid(column=col, row=rw)


def _new_insight():
    new = Tk()
    new.geometry("1024x600")
    new.title("New Insight")

    lbl = Label(new, text="New Insight here???")
    _place_obj(lbl, 0, 0)

    txt = Entry(new, width=8)


def main():
    window = Tk()
    window.geometry("1024x600")
    window.title("Gui Frontend for Sumo CSE Ticket Tracking")

    lbl = Label(window, text=f"{_insight_num(50010)}", font=(50))
    _place_obj(lbl, 0, 0)

    btn = Button(window, text="New Insight", command=_new_insight)
    _place_obj(btn, 0, 1)

    window.mainloop()


if __name__ == "__main__":
    main()
