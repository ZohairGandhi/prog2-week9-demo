from tkinter import *
from tkinter import ttk


class GroupPage:
    def __init__(self, parent, group) -> None:
        self.group = group
        self.mainframe = ttk.Frame(parent)
        self.mainframe.grid(column=0, row=0)

        ttk.Label(self.mainframe, text="Seat Group:").grid(column=0, row=0)
        ttk.Label(self.mainframe, text=self.group.self.group_type).grid(column=1, row=0)

        ttk.Label(self.mainframe, text="Capacity:").grid(column=0, row=1)
        ttk.Label(self.mainframe, text=self.group.capacity).grid(column=1, row=1)

        ttk.Label(self.mainframe, text="Price ($):").grid(column=0, row=2)
        ttk.Label(self.mainframe, text=self.group.price).grid(column=1, row=2)

        self.tickets_sold = IntVar(
            value=(self.group.capacity - self.group.remaining_capacity)
        )
        ttk.Label(self.mainframe, text="Sold").grid(column=0, row=3)
        ttk.Label(self.mainframe, textvariable=self.tickets_sold).grid(column=1, row=3)

        self.tickets_remaining = IntVar(value=self.group.remaining_capacity)
        ttk.Label(self.mainframe, text="Left").grid(column=0, row=4)
        ttk.Label(self.mainframe, textvariable=self.tickets_remaining).grid(
            column=1, row=4
        )

        self.income = DoubleVar(value=(self.tickets_sold.get() * self.group.price))
        ttk.Label(self.mainframe, text="Income ($):").grid(column=0, row=5)
        ttk.Label(self.mainframe, textvariable=self.income).grid(column=1, row=5)

        self.entry_tf = IntVar(value=0)
        ttk.Label(self.mainframe, text="Sell").grid(column=0, row=6)
        ttk.Entry(self.mainframe, textvariable=self.entry_tf).grid(column=1, row=6)

        ttk.Button(self.mainframe, text="Sell", command=self.sell_btn_handler).grid(
            column=1, row=7
        )

    def sell_btn_handler(self):
        try:
            tickets = self.entry_tf.get()
            if self.group.has_capacity(tickets):
                self.group.sell(tickets)
                self.tickets_sold.set(self.tickets_sold.get() + tickets)
                self.tickets_remaining.set(self.group.remaining_capacity)
                self.income.set(self.income.get() + (self.group.price * tickets))
        except Exception:
            pass
