from front.front import MyWindow
from tkinter import *

# The runner creates a gui window, by using TK library
print("Type down the number of machine windows to open. When finished, press Enter")
numberOfWindows = int(input())
for i in range(numberOfWindows):
    window = Tk()
    mywin = MyWindow(window)
    window.title("BRAINY")
    window.geometry("600x350")

window.mainloop()
