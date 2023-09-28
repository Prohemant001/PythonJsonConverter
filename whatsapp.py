import pyautogui
import time

time.sleep(20)
for i in range(5000):
    pyautogui.typewrite('Hello Anil !!')
    pyautogui.press("enter")