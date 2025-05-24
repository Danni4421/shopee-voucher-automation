from tkinter import ttk
from datetime import datetime, timedelta

class GlobalClock(ttk.Label):
    def __init__(self, parent, *args, **kwargs):
        """
        Initializes the GlobalClock widget to display the current time in WIB (Western Indonesian Time).
        Args:
            parent: The parent widget to attach this clock to.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        super().__init__(parent, *args, **kwargs)
        self.configure()
        self.update_clock()

    def update_clock(self):
        """
        Updates the clock label with the current time in WIB (Western Indonesian Time).
        This method calculates the current time in UTC, converts it to WIB by adding 7 hours,
        and formats it as a string to display in the label.
        """

        now_utc = datetime.utcnow()
        now_wib = now_utc + timedelta(hours=7)
        self.config(text=f"Waktu WIB: {now_wib.strftime('%H:%M:%S')}")
        self.after(500, self.update_clock)

def build(parent):
    clock = GlobalClock(parent, anchor="center", justify="center")
    clock.grid(row=0, column=0, columnspan=99, sticky="ew", pady=(5, 10))
    parent.grid_columnconfigure(0, weight=1)
    return clock