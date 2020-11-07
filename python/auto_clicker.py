# This script uses pyautogui to repeatedly click on a x & y coordinate on your screen.
# pip install PyAutoGUI

import pyautogui
i = 1
x = input("X coordinate: ")
y = input("Y coordinate: ")
while i != 0:
    # x and y coordinates for pointer location
    pyautogui.click(x, y)
