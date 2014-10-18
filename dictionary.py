#
# Dictionary register mappings for max7219 driver
#
# Author : Prashant Malani <p.malani@gmail.com>
# Date   : 10/17/2014
#
# NOTE: The leading zeroes will be a problem while writing up these
# mappings. They will create a problem in case scrolling text is
# presented and we need to composite screen contents before drawing.
# To counter this, we add a leading zero at bit-8 for all the
# definitions. That way leading zero's will be preserved.

char_map = {
    "A": [0x08, 0x14, 0x14, 0x22, 0x3E, 0x22, 0x42, 0x42],
    "B": [0x7C, 0x42, 0x44, 0x78, 0x44, 0x42, 0x42, 0x7C],
    "C": [0x3C, 0x42, 0x40, 0x40, 0x40, 0x40, 0x42, 0x3C],
}

