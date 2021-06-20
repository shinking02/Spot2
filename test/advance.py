#!usr/bin/python

import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GOUI.IN, pull_up_down=GPIO.PUD_DOWN)

pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq()