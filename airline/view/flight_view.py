import tkinter as tk
from tkinter import messagebox


class FlightView:
    def show_flights(self, flights):
        if not flights:
            messagebox.showinfo("Flights", "No flights available.")
            return

        msg = "Available Flights:\n\n"
        for i, f in enumerate(flights):
            msg += f"{i + 1}. {f.get_details()}\n"

        messagebox.showinfo("Available Flights", msg)

    def get_new_flight_details(self):
        self.win = tk.Toplevel()
        self.win.title("Add New Flight")
        self.win.geometry("300x300")
        self.win.eval('tk::PlaceWindow . center')

        tk.Label(self.win, text="Flight Number (e.g. IR-123):").pack(pady=2)
        self.entry_num = tk.Entry(self.win)
        self.entry_num.pack(pady=2)

        tk.Label(self.win, text="Airline:").pack(pady=2)
        self.entry_airline = tk.Entry(self.win)
        self.entry_airline.pack(pady=2)

        tk.Label(self.win, text="Origin:").pack(pady=2)
        self.entry_origin = tk.Entry(self.win)
        self.entry_origin.pack(pady=2)

        tk.Label(self.win, text="Destination:").pack(pady=2)
        self.entry_dest = tk.Entry(self.win)
        self.entry_dest.pack(pady=2)

        tk.Label(self.win, text="Price:").pack(pady=2)
        self.entry_price = tk.Entry(self.win)
        self.entry_price.pack(pady=2)

        self.result = None
        tk.Button(self.win, text="Save Flight", command=self.submit_flight).pack(pady=10)

        self.win.grab_set()
        self.win.wait_window()
        return self.result if self.result else ("", "", "", "", 0.0)

    def submit_flight(self):
        try:
            price = float(self.entry_price.get())
        except ValueError:
            price = 0.0
        self.result = (
            self.entry_num.get(),
            self.entry_airline.get(),
            self.entry_origin.get(),
            self.entry_dest.get(),
            price
        )
        self.win.destroy()

    def get_flight_choice(self, flights):
        if not flights:
            return None

        self.win = tk.Toplevel()
        self.win.title("Select Flight")
        self.win.geometry("400x300")
        self.win.eval('tk::PlaceWindow . center')

        tk.Label(self.win, text="Select a flight from the list:").pack(pady=10)

        self.listbox = tk.Listbox(self.win, width=50, height=10)
        for f in flights:
            self.listbox.insert(tk.END, f.get_details())
        self.listbox.pack(pady=10)

        self.result = None
        tk.Button(self.win, text="Select", command=lambda: self.submit_flight_choice(flights)).pack(pady=10)

        self.win.grab_set()
        self.win.wait_window()
        return self.result

    def submit_flight_choice(self, flights):
        try:
            idx = self.listbox.curselection()[0]
            self.result = flights[idx]
        except IndexError:
            messagebox.showerror("Error", "Please select a flight first.")
            return
        self.win.destroy()

    def get_seat_choice(self, available_seats):
        if not available_seats:
            messagebox.showerror("Error", "No seats available on this flight.")
            return None

        self.win = tk.Toplevel()
        self.win.title("Select Seat")
        self.win.geometry("300x150")
        self.win.eval('tk::PlaceWindow . center')

        tk.Label(self.win, text=f"Available: {', '.join(available_seats)}").pack(pady=10)
        self.entry_seat = tk.Entry(self.win)
        self.entry_seat.pack(pady=5)

        self.result = None
        tk.Button(self.win, text="Select", command=lambda: self.submit_seat(available_seats)).pack(pady=10)

        self.win.grab_set()
        self.win.wait_window()
        return self.result

    def submit_seat(self, available_seats):
        seat = self.entry_seat.get().upper()
        if seat in available_seats:
            self.result = seat
            self.win.destroy()
        else:
            messagebox.showerror("Error", "Invalid or taken seat.")
