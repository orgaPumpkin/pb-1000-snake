import pyautogui
from time import sleep

N_SHIFT = {'(': '9',
           ')': '0',
           ':': ';',
           '"': '\'',
           '*': '8',
           '$': '4',
           '+': '='
           }

V_SHIFT = {'<': ';'
           }

V_N_SHIFT = {'>': ';'
             }

PRESS_TIME = 0.1
pyautogui.DARWIN_CATCH_UP_TIME = 0


def main():
    with open("optimized.txt") as f:
        txt = f.read().lower()
        # txt = ">>>"

    print(txt)
    sleep(2)

    for char in txt:
        if char in N_SHIFT.keys():
            normal = N_SHIFT[char]

            pyautogui.keyDown('shift')
            pyautogui.keyDown(normal)
            sleep(PRESS_TIME)
            pyautogui.keyUp(normal)
            pyautogui.keyUp('shift')

        elif char in V_SHIFT.keys():
            normal = V_SHIFT[char]

            pyautogui.mouseDown()
            pyautogui.keyDown(normal)
            sleep(PRESS_TIME)
            pyautogui.keyUp(normal)
            pyautogui.mouseUp()

        elif char in V_N_SHIFT.keys():
            normal = V_N_SHIFT[char]

            pyautogui.mouseDown()
            pyautogui.keyDown('shift', )
            pyautogui.keyDown(normal)
            sleep(PRESS_TIME)
            pyautogui.keyUp(normal)
            pyautogui.keyUp('shift')
            pyautogui.mouseUp()

        else:
            pyautogui.keyDown(char)
            sleep(PRESS_TIME)
            pyautogui.keyUp(char)


if __name__ == '__main__':
    main()
