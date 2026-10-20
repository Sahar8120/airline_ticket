from view.console_window import ConsoleWindow

class MainView:
    def __init__(self):
        self.window = ConsoleWindow(title="MAIN MENU")

    def show_main_menu(self):
        menu_text = (
            "1. View Flights\n"
            "2. Add New Flight (Admin)\n"
            "3. Book a Ticket\n"
            "4. Cancel a Ticket\n"
            "5. Exit"
        )
        self.window.render(menu_text)
        return self.window.get_input("Enter your choice (1-5): ")

    def show_message(self, message, is_error=False):
        self.window.render(message, is_error)

    def pause(self):

        self.window.get_input("Press Enter to continue...")