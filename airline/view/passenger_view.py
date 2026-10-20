import tkinter as tk


class PassengerView:
    def get_passenger_details(self):
        self.win = tk.Toplevel()
        self.win.title("Passenger Details")
        self.win.geometry("300x280")
        self.win.eval('tk::PlaceWindow . center')

        tk.Label(self.win, text="Name:").pack(pady=2)
        self.entry_name = tk.Entry(self.win)
        self.entry_name.pack(pady=2)

        tk.Label(self.win, text="Family:").pack(pady=2)
        self.entry_family = tk.Entry(self.win)
        self.entry_family.pack(pady=2)

        tk.Label(self.win, text="Phone (09...):").pack(pady=2)
        self.entry_phone = tk.Entry(self.win)
        self.entry_phone.pack(pady=2)

        tk.Label(self.win, text="National ID (10 digits):").pack(pady=2)
        self.entry_nid = tk.Entry(self.win)
        self.entry_nid.pack(pady=2)

        self.result = None
        tk.Button(self.win, text="Submit", command=self.submit).pack(pady=10)

        self.win.grab_set()
        self.win.wait_window()
        return self.result if self.result else ("", "", "", "")

    def submit(self):
        self.result = (
            self.entry_name.get(),
            self.entry_family.get(),
            self.entry_phone.get(),
            self.entry_nid.get()
        )
        self.win.destroy()