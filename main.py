from tkinter import Tk
from src.app.components import build

if __name__ == "__main__":
    root = Tk()
    root.title("Shopee Voucher Automation")
    root.geometry("420x260")
    root.resizable(False, False)
    root.configure()

    root.update_idletasks()
    width = 420
    height = 260
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    build(root)

    root.mainloop()