class MainView:
    def show_main_menu(self):
        print("\n" + "="*30)
        print("   AIRLINE TICKET SYSTEM")
        print("="*30)
        print("1. View Flights")
        print("2. Book a Ticket")
        print("3. Cancel a Ticket")
        print("4. Exit")
        return input("Enter your choice (1-4): ")

    def show_message(self, message):
        print(f"\n>>> {message} <<<")