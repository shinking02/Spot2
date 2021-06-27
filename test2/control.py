# -*- coding: utf-8 -*-
#!usr/bin/python

import RPi.GPIO as GPIO
import Adafruit_PCA9685
from time import sleep

pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#起動時ニュートラル移行必須

now = [295, 305, 380, 280, 320, 260, 300, 285, 100, 170, 130, 500]
adj_list = [295, 305, 380, 280, 320, 260, 300, 285, 100, 170, 130, 500]

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

def neutral():
def forward():
