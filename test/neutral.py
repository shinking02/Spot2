#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

################################
time.sleep(3)
pwm.set_pwm(0, 0, 350)  #pwm.set_pwm(チャンネル1~12, 0?, 値)
pwm.set_pwm(1, 0, 370)
pwm.set_pwm(2, 0, 450)
pwm.set_pwm(3, 0, 350)
pwm.set_pwm(4, 0, 370)
pwm.set_pwm(5, 0, 340)
pwm.set_pwm(6, 0, 350)
pwm.set_pwm(7, 0, 350)
pwm.set_pwm(8, 0, 120)
pwm.set_pwm(9, 0, 200)
pwm.set_pwm(10, 0, 180)
pwm.set_pwm(11, 0, 590)
################################

