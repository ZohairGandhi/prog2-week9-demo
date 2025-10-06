from tkinter import *
from stadium import stadium
from stadium_app import StadiumApp

root = Tk()
root.title("Stadium")
StadiumApp(root, stadium)
root.mainloop()
