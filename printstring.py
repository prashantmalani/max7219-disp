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
    sample_str = "BAD"
    max_drv = max7219.Max7219()
    max_drv.initialize()
    # Do awesome stuff here
    # Load the screen data with the values to be initially displayed
    screen_data = ltrs.char_map[sample_str[0]][:]
    max_drv.writeScreen(screen_data)
    time.sleep(2)
    for cur_char in sample_str[1:]:
        cur_data = ltrs.char_map[cur_char][:]
        # Run the inner loop 8 times to get through all 8 columns
        for i in range(0, 8):
            # Left shift each row, and then update it
            for i in range(0, 8):
                new_bit = (cur_data[i] >> 7) & 1
                screen_data[i] = ((screen_data[i] << 1) | new_bit) & 0xFF
                cur_data[i] = (cur_data[i] << 1) & 0xFF
            max_drv.writeScreen(screen_data)
            time.sleep(0.3)
    time.sleep(1)
    max_drv.cleanUp()


