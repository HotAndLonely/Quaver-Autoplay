# LIBRARIES
from win32gui import GetWindowText, GetForegroundWindow
from pyautogui import pixel
from time import sleep
from ahk import AHK

# VARIABLES
ahk = AHK()

# CHANGE THIS (EXAMPLE)
bg_color      = (20, 20, 20)            # Color of note slot without notes
coords_x      = [770, 900, 1015, 1140]  # X coords of every note slot horizontal left to right 4k mode
coords_y      = 900                     # Y coord of note slots vertical
game_controls = ['w', 'e', 'i', 'o']    # Game controls left to right 4k mode

# FUNCTIONS

# Detect if Quaver window active
def is_game_active():
    return 'quaver' in GetWindowText(GetForegroundWindow()).lower()

# Hit note function
def hit_note(slot, action):
    if   slot == 0: key = game_controls[0]
    elif slot == 1: key = game_controls[1]
    elif slot == 2: key = game_controls[2]
    elif slot == 3: key = game_controls[3]

    if action == 'down': ahk.key_down(key)
    elif action == 'up': ahk.key_up(key)

# Autoplay
def autoplay():
    while True:
        if is_game_active():
            for n in range(0, 4):
                if pixel(x=coords_x[n], y=coords_y) != bg_color:
                    hit_note(n, 'down')
                else:
                    hit_note(n, 'up')
        else:
            sleep(1)

# Main
def main():
    autoplay()

if '__main__' == __name__:
    main()