import control
from time import sleep
import neutral
import threading

neutral.n()
sleep(2)

if __name__ == "__main__":
    thread_1 = threading.Thread(target=control.moveServo(0, 100, 200))
    thread_2 = threading.Thread(target=control.moveServos(1, 100, 200))

    thread_1.start()
    thread_2.start()

