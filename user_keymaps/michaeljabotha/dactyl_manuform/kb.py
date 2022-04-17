import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from side import LEFT

col_pins = (board.GP15,board.GP14,board.GP13,board.GP12,board.GP11,board.GP10)
left_row_pins = (board.GP9,board.GP8,board.GP7,board.GP6,board.GP5,board.GP4)
right_row_pins = (board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9)


class KMKKeyboard(_KMKKeyboard):
    col_pins = col_pins
    row_pins = left_row_pins if LEFT else right_row_pins
    diode_orientation = DiodeOrientation.COL2ROW
    
    # NOQA
    # flake8: noqa
    coord_mapping = [
     0,  1,  2,  3,  4,  5,                 41, 40, 39, 38, 37, 36,
     6,  7,  8,  9, 10, 11,                 47, 46, 45, 44, 43, 42,
    12, 13, 14, 15, 16, 17,                 53, 52, 51, 50, 49, 48,
    18, 19, 20, 21, 22, 23,                 59, 58, 57, 56, 55, 54,
            26, 27, 28, 35, 33,         69, 71, 64, 63, 62,
                        34, 32,         68, 70,
    ]
