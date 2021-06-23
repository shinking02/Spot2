# -*- coding: utf-8 -*-
#!usr/bin/python

import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time

pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

def moveServo(id, degree, speed):
    adj_list = [295, 305, 380, 280, 320, 260, 300, 285, 100, 170, 130, 500]
    
