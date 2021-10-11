import time
import pyautogui

print("\nFind some stuff here: https://sujalgoel.engineer\n")

for i in range(10):
    print(f"{str(10 - i)} seconds remaining to start the script.")
    time.sleep(1)

time.sleep(1)

for word in open("macbeth.txt"):
    pyautogui.typewrite(word)
    pyautogui.press("enter")
