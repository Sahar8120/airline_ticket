class SampleView:
    def get_input(self):
        print("\n--- Sample View ---")
        a = input("Enter A: ")
        b = input("Enter B: ")
        return a, b

    def show_result(self, message):
        print(f"Result: {message}")