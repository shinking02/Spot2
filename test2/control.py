# -*- coding: utf-8 -*-
#!usr/bin/python

import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time

pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

def moveServo(id, degree, speed):
    pwm.set_pwm(0, 0, 295)

    adj_list = [295, 305, 380, 280, 320, 260, 300, 285, 100, 170, 130, 500]
    if speed == 0:
        pwm.set_pwm(id, 0, adj_list[id] + degree)
    elif speed != 0:
        #
    else:
        print('speedの引数が範囲外です')
        
