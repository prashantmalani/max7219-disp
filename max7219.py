#
#
# MAX7219 Driver for displaying text
#
# Author : Prashant Malani <p.malani@gmail.com>
# Date   : 10/13/2014
#
# Max7219 Pin connections :
# Vcc - Pin 2 (5V)
# Gnd - Pin 9 (GND)
# Din - Pin 11 (GPIO 17)
# CS_BAR  - Pin 15 (GPIO 22)
# Clk - Pin 16 (GPIO 23)
#
import RPi.GPIO as GPIO
import time

# Local defines (GPIO mappings)
DIN = 17
CS_BAR = 22
CLK = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(CS_BAR, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)


GPIO.output(CS_BAR, GPIO.LOW)
time.sleep(0.002)
GPIO.output(DIN, GPIO.HIGH)
time.sleep(0.002)

# First 4 bits don't care
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)

# 0xF address
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)

#D7-D1 don't care, D0=1
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)
GPIO.output(CLK,GPIO.LOW)
time.sleep(0.002)
GPIO.output(CLK,GPIO.HIGH)
time.sleep(0.002)

GPIO.output(CS_BAR, GPIO.HIGH)

print "Done all the GPIO stuff..."

time.sleep(5)


GPIO.cleanup()

