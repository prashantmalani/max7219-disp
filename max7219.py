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
# CS  - Pin 15 (GPIO 22)
# Clk - Pin 16 (GPIO 23)
#
import RPi.GPIO as GPIO
import time

# Local defines (GPIO mappings)
DIN = 17
CS = 22
CLK = 23

class Max7219:
    """ Max7219 initial drive.
    """
    def initialize(self):
        """ Set up GPIO pins.
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DIN, GPIO.OUT)
        GPIO.setup(CS, GPIO.OUT)
        GPIO.setup(CLK, GPIO.OUT)

        GPIO.output(CLK, GPIO.LOW)
        GPIO.output(CS, GPIO.LOW)

        self.writeData(0xB,0xF7)
        self.writeData(0xC,0xFF)
        self.writeData(0x9,0x00)
        self.writeData(0xA,0xFF)

    def writeData(self, address, data):
        """ Write data to the defined address. Assumed that both data and
        address are in hex format.
        Address is assumed to be 4 bits wide, and data 8 bits wide.
        """
        address = address | 0x1F0
        data = data | 0x100
        # Convert to array
        addr_list = [int(x) for x in bin(address)[3:]]
        data_list = [int(x) for x in bin(data)[3:]]
        print data_list
        write_data = addr_list + data_list

        # Write the data
        GPIO.output(CS, GPIO.HIGH)
        #time.sleep(0.002)
        for cur_bit in write_data:
            GPIO.output(DIN, cur_bit == 1)
            #time.sleep(0.002)
            GPIO.output(CLK, 1)
            #time.sleep(0.002)
            print "Bit written is " + str(cur_bit)
            #time.sleep(0.002)
            GPIO.output(CLK, 0)
        # The clock edge needs to rise, and only then should the CS
        # signal be raised.
        GPIO.output(CS, GPIO.LOW)
        print "Done all the GPIO stuff..."

    def expData(self, address):
        """ Write all bits to 1 individually.
        """
        val = 1;
        for i in range(0, 8):
            self.writeData(address, val)
            time.sleep(2)
            val = (val << 1) | 1

    def cleanUp(self):
        self.writeData(0xC, 0x0)
        self.writeData(0xA,0xFF)
        GPIO.cleanup()

if __name__ == "__main__":
    max_drv = Max7219()
    max_drv.initialize()
    max_drv.writeData(0x1, 0x1)
    max_drv.writeData(0x2, 0x3)
    max_drv.writeData(0x3, 0x7)
    max_drv.writeData(0x4, 0xF)
    max_drv.writeData(0x5, 0x1F)
    max_drv.writeData(0x6, 0x3F)
    max_drv.writeData(0x7, 0x7F)
    max_drv.writeData(0x8, 0xFF)
    time.sleep(3);
    max_drv.cleanUp()

