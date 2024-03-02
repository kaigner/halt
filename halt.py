#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import socket

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung

p.ChangeDutyCycle(7.5)
# p.ChangeDutyCycle(0)

def ping_server(host, port=80, timeout=5):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        sock.close()
        print("up")
        return True
    except socket.error as e:
        print("down")
        return False

if not ping_server("mail.shemhazai.de"):
    print("shut")
    p.ChangeDutyCycle(4)




p.ChangeDutyCycle(0)
# p.stop()
# GPIO.cleanup()



