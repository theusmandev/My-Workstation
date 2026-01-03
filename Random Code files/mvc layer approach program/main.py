import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controller.thumbnail_controller import ThumbnailController


INPUT = r"E:\unb-workstation\Writers All Novels\New folder"
OUTPUT = INPUT + r"\thumbnails_1000x667"
FONT = r"E:\unb-workstation\Writers All Novels\RobotoCondensed-BoldItalic.ttf"

app = ThumbnailController(INPUT, OUTPUT, FONT)
app.process()
