# -*- coding: utf-8 -*-
#!usr/bin/python

import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time

pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

def moveServo(id, degree, speed):
    pwm.set_pwm(0, 0, 295)