import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

photointerrupter = digitalio.DigitalInOut(board.D2)
photointerrupter.direction = digitalio.Direction.INPUT
photointerrupter.pull = digitalio.Pull.UP
photointerrupter_state = None
if not photointerrupter.value and photointerrupter_state is None:
photointerrupter_state = "interrupted"
lcd.set_cursor_pos(0,0)
lcd.print("The number of interrupts is: ")