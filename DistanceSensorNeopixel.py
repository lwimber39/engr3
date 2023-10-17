# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance))
        dist = sonar.distance
        if dist < 5: 
            pass
            #light up LED somehow
        elif dist > 35:
            pass
            #light up LED somehow
    except RuntimeError:
        print("Retrying!")
        time.sleep(0.1)    