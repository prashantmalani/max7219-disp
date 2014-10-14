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

class Max7219:
    """ Max7219 initial drive.
    """
    def initialize(self):
        """ Set up GPIO pins.
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DIN, GPIO.OUT)
        GPIO.setup(CS_BAR, GPIO.OUT)
        GPIO.setup(CLK, GPIO.OUT)

    def writeData(self, address, data):
        """ Write data to the defined address. Assumed that both data and
        address are in hex format.
        Address is assumed to be 4 bits wide, and data 8 bits wide.
        """
        address = address | 0xF0
        # Convert to array
        addr_list = [int(x) for x in bin(address)[2:]]
        data_list = [int(x) for x in bin(data)[2:]]
        write_data = addr_list + data_list

        # Write the data
        GPIO.output(CS_BAR, GPIO.LOW)
        for cur_bit in write_data:
            GPIO.output(CLK, 0)
            GPIO.output(DIN, cur_bit)
            GPIO.output(CLK, 1)
        GPIO.output(CS_BAR, GPIO.HIGH)
        print "Done all the GPIO stuff..."

if __name__ == "__main__":
    max_drv = Max7219()
    max_drv.initialize()
    max_drv.writeData(0xF, 0xFF)
    GPIO.cleanup()

