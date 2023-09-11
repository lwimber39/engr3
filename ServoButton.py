
import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

pwm = pwmio.PWMOut(board.D5, duty_cycle=0, frequency=50)

btn = DigitalInOut(board.D8)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

btn2 = DigitalInOut(board.D9)
btn2.direction = Direction.INPUT 
btn2.pull = Pull.DOWN

servo = servo.Servo(pwm)
angle = 90

while True:
    if btn.value:
        angle = angle + 2
        if angle > 180:
            angle = 180
        print(angle)
        servo.angle = angle
        time.sleep(0.01)
        
    if btn2.value:
        angle = angle - 2
        if angle < 0:
            angle = 0
        print(angle)
        servo.angle = angle
        time.sleep(0.01)