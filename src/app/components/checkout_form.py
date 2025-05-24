from tkinter import ttk, messagebox
from threading import Thread
from datetime import datetime, timedelta

class AppiumCheckoutForm(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        """
        Initializes the AppiumCheckoutForm with input fields for voucher name and time,
        and a button to start the automation process.

        Args:
            parent: The parent widget to attach this form to.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        This form allows users to input a voucher name and a time in WIB (Western Indonesian Time)
        format (HH:MM), and starts an automation process that runs at the specified time.
        """
        super().__init__(parent, *args, **kwargs)
        self.configure(padding=20)

        ttk.Label(self, text="Nama Voucher:").grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.voucher_entry = ttk.Entry(self, width=35, font=('Segoe UI', 11))
        self.voucher_entry.grid(row=1, column=0, pady=(0, 10), sticky="ew")
        self.voucher_entry.insert(0, "Diskon 2% s/d Rp500RB")

        ttk.Label(self, text="Jalankan pada (WIB, HH:MM):").grid(row=2, column=0, sticky="w", pady=(0, 5))
        self.time_entry = ttk.Entry(self, width=20, font=('Segoe UI', 11))
        self.time_entry.grid(row=3, column=0, pady=(0, 10), sticky="ew")
        self.time_entry.insert(0, "20:15")

        self.start_btn = ttk.Button(self, text="Start Automation", command=self.start_automation)
        self.start_btn.grid(row=4, column=0, pady=20, sticky="ew")
        self.grid_columnconfigure(0, weight=1)
        self._countdown_active = False

    def start_automation(self):
        """
        Starts the automation process by retrieving the voucher name and time,
        disabling the start button, and launching a countdown timer.
        """

        self.start_btn.config(state="disabled")
        self._countdown_active = True
        allowed_time = self.time_entry.get()
        Thread(target=self.run_automation, args=(allowed_time,), daemon=True).start()
        self.update_countdown(allowed_time)

    def update_countdown(self, allowed_time):
        """
        Updates the countdown timer based on the allowed time input.
        Args:
            allowed_time (str): The time in HH:MM or HH:MM:SS format when the automation should run.
        """
        
        try:
            time_parts = list(map(int, allowed_time.strip().split(":")))
            if len(time_parts) == 2:
                hour, minute = time_parts
                second = 0
            elif len(time_parts) == 3:
                hour, minute, second = time_parts
            else:
                raise ValueError
        except Exception:
            self.start_btn.config(text="Start Automation")
            return
        
        now_utc = datetime.utcnow()
        now_wib = now_utc + timedelta(hours=7)
        target = now_wib.replace(hour=hour, minute=minute, second=second, microsecond=0)

        if now_wib > target:
            target += timedelta(days=1)
            
        delta = int((target - now_wib).total_seconds())

        if self._countdown_active and delta > 0:
            self.start_btn.config(text=f"Menunggu {delta} detik")
            self.after(200, lambda: self.update_countdown(allowed_time))
        else:
            self.start_btn.config(text="Running...")

    def run_automation(self, allowed_time):
        """
        Runs the Appium automation process after the specified time.
        Args:
            allowed_time (str): The time in HH:MM or HH:MM:SS format when the automation should run.
        """

        try:
            from src.lib.appium import Appium
            from src.auto import run

            app = Appium()
            app.start(run, allowed_time)

            messagebox.showinfo("Checkout Automation Succeed", "Your voucher should be choosen right now!")
        finally:
            self._countdown_active = False
            self.start_btn.config(state="normal", text="Start Automation")


def build(parent):
    form = AppiumCheckoutForm(parent)
    form.grid(row=1, column=0, sticky="nsew")
    return form