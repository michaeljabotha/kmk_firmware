import board

from kb import KMKKeyboard
from side import LEFT
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split, SplitSide


keyboard = KMKKeyboard()

layers_ext = Layers()
modtap = ModTap()
split_side = SplitSide.LEFT if LEFT else SplitSide.RIGHT

split = Split(
    split_side=split_side,
    data_pin=board.GP1,
    data_pin2=board.GP0,
    use_pio=False,
    uart_flip=False,
    debug_enabled=False,
    )

keyboard.modules = [
    layers_ext,
    modtap,
    split,
    ]

# Cleaner key names
XXXX = KC.NO
____ = KC.TRNS
QQQQ = KC.NO

keyboard.debug_enabled = False

keyboard.keymap = [
    [
        KC.ESC,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,                              KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      QQQQ,
        KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,                               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       QQQQ,
        KC.LSFT,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,                               KC.H,       KC.J,       KC.K,       KC.L,       QQQQ,       QQQQ,
        KC.LCTL,    KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,                               KC.N,       KC.M,       KC.COMMA,   KC.DOT,     QQQQ,       QQQQ,
                                QQQQ,       QQQQ,       KC.N3,      KC.N2,      KC.N1,      KC.N1,      KC.N2,      KC.N3,      QQQQ,       QQQQ,
                                                                    KC.N5,      KC.N4,      KC.N4,      KC.N5,
    ],
]

if __name__ == '__main__':
    keyboard.go()
