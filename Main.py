from Module import FuncAbfragen as FuncA
from Module import Func
import sys

def handle_gui_result(value):
    print("Entered text:", value)
    Func.screenshot_to_pdf(Jpgdatei, value)

Jpgdatei = FuncA.AbfrageJPG()
FuncA.call_entry_gui(handle_gui_result)

