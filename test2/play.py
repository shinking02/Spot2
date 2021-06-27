import control
import neutral
from time import sleep

neutral.n()
sleep(2)
control.moveServo(0, 50, 0)
