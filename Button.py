import time
import board
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.D8)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

btn2 = DigitalInOut(board.D9)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

while True:
    if btn.value:
        print("BTN is down")
    else:
        print("BTN is up")
        pass

    time.sleep(0.1) # sleep for debounce
    if btn2.value:
        print("BTN2 is down")
    else:
        print("BTN2 is up")
    pass

    time.sleep(0.1) # sleep for debounce