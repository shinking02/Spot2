from control import moveServo
from time import sleep
import neutral
import threading

neutral.n()
sleep(2)

if __name__ == "__main__":
    thread_1 = threading.Thread(target=moveServo(0, 100, 200))
    thread_2 = threading.Thread(target=moveServo(0, 100, 200))

    thread_1.start()
    thread_2.start()

