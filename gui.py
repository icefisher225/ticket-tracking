from datastructures import *
from helperfunctions import *
from gui_helperfunctions import *
import gui_new_insight as gni

from tkinter import *
from tkinter.ttk import *


def new_insight():
    gni.new_insight()


window = Tk()
window.geometry("1024x600")
window.title("Gui Frontend for Sumo CSE Ticket Tracking")
window.focus()

lbl = Label(window, text=f"{insight_num(50010)}", font=(50))
place_obj(lbl, 0, 0)

btn = Button(window, text="New Insight", command=new_insight)
place_obj(btn, 0, 1)

window.mainloop()
