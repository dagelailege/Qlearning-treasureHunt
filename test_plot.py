# -*- coding: utf-8 -*-

"""
author = ‘wuzhiheng‘
time   = '2019-04-14 22:46'
"""

import tkinter as tk
from tkinter import *
import time
import random


def update():
    global cv
    time.sleep(3)
    row = 10 + 100*random.randint(0, 4)
    col = 100 + 100*random.randint(0, 4)
    cv.coords("robot", (row, col, 100+row, 100+col))
    cv.update()


root = tk.Tk()
root.geometry("900x700")
cv = tk.Canvas(root, bg='white', height=800, width=600)
cv.pack()
grids = []
for i in range(5):
    for j in range(5):
        row = 10 + i*100
        col = 100 + j*100
        if i == 2 and j == 1:
            r = cv.create_rectangle(row, col, 100+row, 100+col, fill="red", tag="robot")
        else:
            r = cv.create_rectangle(row, col, 100 + row, 100 + col)

        # print(type(w))
        """
        if i == 1 and j == 2:
            w.
        """

for i in range(1):
    update()
"""

while True:
    time.sleep(3)
    update()
"""

# root.mainloop()

