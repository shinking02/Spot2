# -*- coding: utf-8 -*-
#!usr/bin/python

import RPi.GPIO as GPIO
import Adafruit_PCA9685
from time import sleep

pwm=Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#起動時ニュートラル移行必須

now = [295, 305, 380, 258, 200, 380, 200, 395, 200, 380, 230, 400]
adj_list = [295, 305, 380, 258, 200, 380, 200, 395, 200, 380, 230, 400]
sleep_list = [295, 305, 380, 258, 212, 368, 230, 365, 80, 500, 110, 520]

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

def quick_sleep():
    for i in range(12):
        pwm.set_pwm(i, 0, sleep_list[i])
        now[i] = sleep_list[i]

def set_nt():
    while(now[4] != adj_list[4]):
        pwm.set_pwm(4, 0, now[4] - 1)
        pwm.set_pwm(5, 0, now[5] + 1)
        now[4] -= 1
        now[5] += 1
        sleep(0.1)
    while(now[6] != adj_list[6]):
        pwm.set_pwm(6, 0, now[6] - 1)
        pwm.set_pwm(7, 0, now[7] + 1)
        now[6] -= 1
        now[7] += 1
        sleep(0.05)
    while(now[10] != adj_list[10]):
        pwm.set_pwm(10, 0, now[10] + 1)
        pwm.set_pwm(11, 0, now[11] - 1)
        now[10] += 1
        now[11] -= 1
        sleep(0.01)
    while(now[8] != adj_list[8]):
        pwm.set_pwm(8, 0, now[8] + 1)
        pwm.set_pwm(9, 0, now[9] - 1)
        now[8] += 1
        now[9] -= 1
        sleep(0.005)

def set_sleep():
    while(now[4] != sleep_list[4]):
        pwm.set_pwm(4, 0, now[4] + 1)
        pwm.set_pwm(5, 0, now[5] - 1)
        now[4] += 1
        now[5] -= 1
        sleep(0.1)
    while(now[6] != sleep_list[6]):
        pwm.set_pwm(6, 0, now[6] + 1)
        pwm.set_pwm(7, 0, now[7] - 1)
        now[6] += 1
        now[7] -= 1
        sleep(0.05)
    while(now[10] != sleep_list[10]):
        pwm.set_pwm(8, 0, now[8] - 1)
        pwm.set_pwm(9, 0, now[9] + 1)
        pwm.set_pwm(10, 0, now[10] - 1)
        pwm.set_pwm(11, 0, now[11] + 1)
        now[8] -= 1
        now[9] += 1
        now[10] -= 1
        now[11] += 1
        sleep(0.06)

def forward():
    moveServo(4, -50, 0)