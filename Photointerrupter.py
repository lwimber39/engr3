import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import board

photointerrupter = digitalio.DigitalInOut(board.D2)
photointerrupter.direction = digitalio.Direction.INPUT
photointerrupter.pull = digitalio.Pull.UP
photointerrupter_state = None
interrupt_counter = 0

lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows=2, num_cols=16)
lcd.set_cursor_pos(0,0)
lcd.print("The number of interrupts is: ")
now = time.monotonic()

while True:
    if not photointerrupter.value and photointerrupter_state is None:
        photointerrupter_state = "interrupted"
    if photointerrupter.value and photointerrupter_state == "interrupted":
        photointerrupter_state = None
        interrupt_counter = interrupt_counter+1
    if (now + 4) < time.monotonic():
        lcd.set_cursor_pos(1,13)
        lcd.print(str(interrupt_counter))
        now = time.monotonic()
