import tkinter as tk


class TicketView:
    def get_payment_method(self):
        self.win = tk.Toplevel()
        self.win.title("Payment Method")
        self.win.geometry("300x150")
        self.win.eval('tk::PlaceWindow . center')

        tk.Label(self.win, text="Enter Method (Cash, Card, Online):").pack(pady=10)
        self.entry_method = tk.Entry(self.win)
        self.entry_method.pack(pady=5)

        self.result = None
        tk.Button(self.win, text="Submit", command=self.submit).pack(pady=10)

        self.win.grab_set()
        self.win.wait_window()
        return self.result if self.result else ""

    def submit(self):
        self.result = self.entry_method.get()
        self.win.destroy()

    def get_ticket_number_to_cancel(self):
        self.win = tk.Toplevel()
        self.win.title("Cancel Ticket")
        self.win.geometry("300x150")
        self.win.eval('tk::PlaceWindow . center')

        tk.Label(self.win, text="Enter Ticket Number (e.g., TK-1001):").pack(pady=10)
        self.entry_ticket = tk.Entry(self.win)
        self.entry_ticket.pack(pady=5)

        self.result = None
        tk.Button(self.win, text="Cancel Ticket", command=self.submit_cancel).pack(pady=10)

        self.win.grab_set()
        self.win.wait_window()
        return self.result if self.result else ""

    def submit_cancel(self):
        self.result = self.entry_ticket.get()
        self.win.destroy()