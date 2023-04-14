import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import *

#  ======== settings ========
resume_key = KeyCode(char='1')
pause_key = KeyCode(char='2')
exit_key = KeyCode(char='3')
#  ==========================

pause = True
running = True
click_speed = None

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")

def get_click_speed():
    global click_speed
    while click_speed is None:
        try:
            click_speed = float(input("Enter click speed (in seconds): "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_controls():
    print("// AutoClicker")
    print("// - Controls:")
    print("\t 1 = Resume")
    print("\t 2 = Pause")
    print("\t 3 = Exit")
    print("-----------------------------------------------------")
    print('Press 1 to start ...')

def main():
    global click_speed
    mouse = MouseController()
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    get_click_speed()

    while running:
        if not pause:
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(click_speed)
    lis.stop()

if __name__ == "__main__":
    main()
