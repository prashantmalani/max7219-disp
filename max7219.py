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
        # NOTE: Data optionally reversed here, depending on orientation.
        write_data = addr_list + data_list

        # Write the data
        GPIO.output(CS, GPIO.HIGH)
        for cur_bit in write_data:
            GPIO.output(DIN, cur_bit == 1)
            GPIO.output(CLK, 1)
            GPIO.output(CLK, 0)
        GPIO.output(CS, GPIO.LOW)

    def writeScreen(self, data):
        """ Write the contents of a screen out to the appropriate addresses.
        The data is expected as a array of 8 8 bit entries, arranged so:
        [row0, row1, row2, row3, .... row7]. We write the extra 9th "No-op"
        register since it's needed to flush out the last row."""
        row_addr = 0x1
        for row_data in data:
            self.writeData(row_addr, row_data)
            row_addr += 1
        self.writeData(row_addr, 0)


    def cleanUp(self):
        self.writeData(0xC, 0x0)
        self.writeData(0xA,0xFF)
        GPIO.cleanup()

if __name__ == "__main__":
    max_drv = Max7219()
    max_drv.initialize()
    test1 = [0x1, 0x3, 0x7, 0xF, 0x1F, 0x3F, 0x7F, 0xFF]
    max_drv.writeScreen(test1)
    time.sleep(3);
    test2 = [0x18, 0x3C, 0x7E, 0xFF, 0xFF, 0x7E, 0x3C, 0x18]
    max_drv.writeScreen(test2)
    time.sleep(3);
    max_drv.cleanUp()

