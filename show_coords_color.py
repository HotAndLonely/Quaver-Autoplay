from pyautogui import position, pixel
from time import sleep

# Function to obtain mouse position and color
def show_mouse_position():
    try:
        while True:
            sleep(2)
            x, y = position()
            color = pixel(x, y)
            print(f"Current mouse position: X = {x}, Y = {y} / Color = {color}")
    except KeyboardInterrupt:
        print("\n¡Keyboard Interrupt!")

show_mouse_position()
