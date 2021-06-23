# -*- coding: utf-8 -*-
#!usr/bin/python

import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time

pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

def moveServo(id, degree, speed):
    adj_list = [295, 305, 380, 280, 320, 260, 300, 285, 100, 170, 130, 500]
    if speed == 0:
        pwm.set_pwm(id, 0, adj_list[id] + degree)
    elif degree >= 0 and speed != 0:
        for i in range(degree = 1):
            pwm.set_pwm(id, 0, adj_list[id] + i)
            time.sleep(0.001 * speed)
    elif degree < 0 and speed != 0:
        for i in range(abs(degree)):
            pwm.set_pwm(id, 0, adj_list[id] -i)
            time.sleep(0.001 * speed)