import board

import pwmio

from adafruit_motor import servo

from digitalio import DigitalInOut, Direction, Pull




# create a PWMOut object on the control pin.

pwm = pwmio.PWMOut(board.D5, duty_cycle=0, frequency=50)




btn = DigitalInOut(board.D8)

btn.direction = Direction.INPUT

btn.pull = Pull.DOWN




btn2 = DigitalInOut(board.D9)

btn2.direction = Direction.INPUT

btn2.pull = Pull.DOWN




# To get the full range of the servo you will likely need to adjust the min_pulse and max_pulse to

# match the stall points of the servo.

# This is an example for the Sub-micro servo: https://www.adafruit.com/product/2201

	@@ -40,14 +31,12 @@ servo = servo.Servo(pwm)




# We sleep in the loops to give the servo time to move into position.

while True:

    if btn.value:

        print("Sweep from 0 to 180")

        for i in range(180):

            servo.angle = i

            time.sleep(0.01)

    else:

            if btn2.value:

                print("Sweep from 180 to 0")

                for i in range(180):

                    servo.angle = 180 - i

                    time.sleep(0.01)