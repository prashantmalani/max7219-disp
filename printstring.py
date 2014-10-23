#
#
# Sample code to print a given string on the 8x8 matrix
#
# Author: Prashant Malani <p.malani@gmail.com>
# Date  : 10/19/2014
#

import max7219
import dictionary as ltrs
import time


if __name__ == "__main__":
    sample_str = "lBEllED"
    max_drv = max7219.Max7219()
    max_drv.initialize()
    max_drv.writeString(sample_str)
    max_drv.cleanUp()


