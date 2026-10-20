from controller.main_controller import MainController

# نقطه شروع برنامه (Entry Point) - منطق به لایه کنترلر منتقل شده است
def main():
    app = MainController()
    app.run()

if __name__ == "__main__":
    main()