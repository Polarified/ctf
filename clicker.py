import pyautogui as pag
import time

# Place the cursor on the relevant places to get them saved, one after the other.
# password = input("Place cursor on text field")
# text_x, text_y = pag.position()
input("Place cursor on the button and hit enter to execute the entire cycle.")
button_x, button_y = pag.position()

pag.click(button_x, button_y)
pag.press(['f5'])
time.sleep(0.010)
# pag.click(text_x, text_y)
# pag.typewrite(password)
# pag.typewrite(['enter'])
pag.click(button_x, button_y)
