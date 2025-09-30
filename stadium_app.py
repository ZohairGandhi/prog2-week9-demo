from tkinter import *
from tkinter import ttk
from tkinter import Tk
from stadium import stadium


class StadiumApp:
    def __init__(self, root) -> None:
        self.mainframe = ttk.Frame(root).grid(column=0, row=0)

        ttk.Label(self.mainframe, text="Seat Group:").grid(column=0, row=0)
        ttk.Label(self.mainframe, text=stadium.group.group_type).grid(column=1, row=0)

        ttk.Label(self.mainframe, text="Capacity:").grid(column=0, row=1)
        ttk.Label(self.mainframe, text=stadium.group.capacity).grid(column=1, row=1)

        ttk.Label(self.mainframe, text="Price ($):").grid(column=0, row=2)
        ttk.Label(self.mainframe, text=stadium.group.price).grid(column=1, row=2)

        self.tickets_sold = IntVar(value=0)
        ttk.Label(self.mainframe, text="Sold").grid(column=0, row=3)
        ttk.Label(self.mainframe, textvariable=self.tickets_sold).grid(column=1, row=3)

        self.tickets_remaining = IntVar(value=stadium.group.remaining_capacity)
        ttk.Label(self.mainframe, text="Left").grid(column=0, row=4)
        ttk.Label(self.mainframe, textvariable=self.tickets_remaining).grid(
            column=1, row=4
        )

        self.income = DoubleVar(value=0.0)
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
            if stadium.group.has_capacity(self.entry_tf.get()):
                stadium.group.sell(self.entry_tf.get())
                self.tickets_sold.set(self.tickets_sold.get() + self.entry_tf.get())
                self.tickets_remaining.set(stadium.group.remaining_capacity)
                self.income.set(
                    self.income.get() + (stadium.group.price * self.entry_tf.get())
                )
        except Exception:
            pass


root = Tk()
root.title("Stadium")
StadiumApp(root)
root.mainloop()
