# -*- coding: utf-8 -*-
#!usr/bin/python

import RPi.GPIO as GPIO
import Adafruit_PCA9685
from time import sleep

pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#起動時ニュートラル移行必須

now = [295, 305, 380, 258, 200, 380, 200, 395, 200, 70, 230, 400]
adj_list = [295, 305, 380, 258, 200, 380, 200, 395, 200, 70, 230, 400]

def moveServo(id, degree, speed):
    if speed == 0:
        pwm.set_pwm(id, 0, adj_list[id] + degree)
        now[id] += degree
    while(now[id] != adj_list[id] + degree):
        if now[id] < adj_list[id] + degree:
            pwm.set_pwm(id, 0, now[id] + 1)
            now[id] += 1
            sleep(0.0001 * speed)
        else:
            pwm.set_pwm(id, 0, now[id] - 1)
            now[id] -= 1
            sleep(0.0001 * speed)

def moveServos(id, degree, speed):
    if speed == 0:
        pwm.set_pwm(id, 0, adj_list[id] + degree)
        now[id] += degree
    while(now[id] != adj_list[id] + degree):
        if now[id] < adj_list[id] + degree:
            pwm.set_pwm(id, 0, now[id] + 1)
            now[id] += 1
            sleep(0.0001 * speed)
        else:
            pwm.set_pwm(id, 0, now[id] - 1)
            now[id] -= 1
            sleep(0.0001 * speed)

def quick_sleep():
    moveServo(0, 0, 0)
    moveServo(1, 0, 0)
    moveServo(2, 0, 0)
    moveServo(3, 0, 0)
    moveServo(4, 12, 0)
    moveServo(5, -12, 0)
    moveServo(6, 30, 0)
    moveServo(7, -30, 0)
    moveServo(8, -120, 0)
    moveServo(9, 120, 0)
    moveServo(10, -120, 0)
    moveServo(11, 120, 0)


#def set_nt():