from tkinter import *
from tkinter import ttk
from group_page import GroupPage


class StadiumApp:
    def __init__(self, root, stadium) -> None:
        mainframe = ttk.Frame(root).grid(column=0, row=0)
        self.root = root
        self.stadium = stadium

        ttk.Label(mainframe, text="Stadium").grid(column=0, row=0)

        groups_list = [str(val) for val in stadium.groups]
        groups_var = StringVar(value=groups_list)
        self.groups_lbox = Listbox(mainframe, listvariable=groups_var)
        self.groups_lbox.grid(column=0, row=1)

        ttk.Button(mainframe, text="Open", command=self.open_btn_handler).grid(
            column=0, row=2
        )

    def open_btn_handler(self):
        selection_idx = self.groups_lbox.curselection()[0]
        new_window = Toplevel(self.root)
        GroupPage(new_window, self.stadium.groups[selection_idx])
