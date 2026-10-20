import tkinter as tk
from tkinter import messagebox


class MainView:
    def __init__(self):
        self.choice = None

    def show_main_menu(self):
        self.root = tk.Tk()
        self.root.title("Airline Ticket System")
        self.root.geometry("300x350")


        self.root.eval('tk::PlaceWindow . center')

        tk.Label(self.root, text="Main Menu", font=("Arial", 14, "bold")).pack(pady=15)

        tk.Button(self.root, text="1. View Flights", width=20, command=lambda: self.set_choice("1")).pack(pady=5)
        tk.Button(self.root, text="2. Add New Flight", width=20, command=lambda: self.set_choice("2")).pack(pady=5)
        tk.Button(self.root, text="3. Book a Ticket", width=20, command=lambda: self.set_choice("3")).pack(pady=5)
        tk.Button(self.root, text="4. Cancel a Ticket", width=20, command=lambda: self.set_choice("4")).pack(pady=5)
        tk.Button(self.root, text="5. Exit", width=20, command=lambda: self.set_choice("5")).pack(pady=20)

        self.root.mainloop()
        return self.choice

    def set_choice(self, c):
        self.choice = c
        self.root.destroy()


    def show_info(self, message):
        messagebox.showinfo("Success", message)


    def show_error(self, message):
        messagebox.showerror("Error", message)