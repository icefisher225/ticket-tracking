from datastructures import *
from helperfunctions import *
from gui_helperfunctions import *

from tkinter import *
from tkinter.ttk import *


def update_name(txt):
    print(txt.get())


def new_insight():
    new = Tk()
    new.geometry("1024x600")
    new.title("New Insight")
    new.focus()

    lbl = Label(new, text="New Insight here???")
    place_obj(lbl, 0, 0)

    txt = Entry(new, width=8)
    place_obj(txt, 0, 1)

    btn = Button(new, text="Generate", command=lambda: update_name(txt))
    place_obj(btn, 0, 2)


def main():
    return 0


if __name__ == "__main__":
    main()
