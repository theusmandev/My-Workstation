# view/console_view.py

class ConsoleView:

    @staticmethod
    def show_generated(name):
        print(f"Generated: {name}")

    @staticmethod
    def done(total, folder):
        print(f"\nDone! Total {total} thumbnails")
        print(f"Folder: {folder}")
