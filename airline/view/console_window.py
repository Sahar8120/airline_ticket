import os

class ConsoleWindow:
    def __init__(self, title="Airline System"):
        self.title = title

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self, text, is_error=False):

        self.clear()
        print("*" * 60)
        print(f"{self.title:^60}")
        print("*" * 60)
        if is_error:
            print(f"\n[!] ERROR: {text}")
        else:
            print(f"\n{text}")

    def get_input(self, prompt):
        """گرفتن ورودی از کاربر"""
        return input(f"\n>> {prompt} ")