#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

################################
time.sleep(3)
pwm.set_pwm(0, 0, 295)  #pwm.set_pwm(チャンネル1~12, 0?, 値)
pwm.set_pwm(1, 0, 305)
pwm.set_pwm(2, 0, 380)
pwm.set_pwm(3, 0, 280)
pwm.set_pwm(4, 0, 320)
pwm.set_pwm(5, 0, 260)
pwm.set_pwm(6, 0, 300)
pwm.set_pwm(7, 0, 285)
pwm.set_pwm(8, 0, 100)
pwm.set_pwm(9, 0, 170)
pwm.set_pwm(10, 0, 130)
pwm.set_pwm(11, 0, 500)
################################

