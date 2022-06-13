
from keyboard import *


keyboard = Keyboard()

___ = TRANSPARENT
BOOT = BOOTLOADER
L1 = LAYER_TAP(1)

# QWERTY
# L2D = LAYER_TAP(2, D)
# L3B = LAYER_TAP(3, B)
# Dvorak
L2E = LAYER_TAP(2, E)
L3X = LAYER_TAP(3, X)

LSFT4 = LAYER_MODS(4, MODS(LSHIFT))
RSFT4 = LAYER_MODS(4, MODS(RSHIFT))
L5O = LAYER_TAP(5, O)

# Semicolon Ctrl for QWERTY
SCC = MODS_TAP(MODS(RCTRL), ';')
# S Ctrl for Dvorak
# SCC = MODS_TAP(MODS(RCTRL), S)

# H Ctrl for Dvorak
HCTRL = MODS_TAP(MODS(RCTRL), H)

# SPACE Ctrl
SPACECTRL = MODS_TAP(MODS(RCTRL), SPACE)

SINS = MODS_KEY(MODS(SHIFT), INSERT)

keyboard.keymap = (
    # Dvorak
    # layer 0
    # 'H' 'SPACE' Ctrl # # exchange ';' and '"', U and I #
    (
        ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '[', ']', BACKSPACE,
        TAB, ';', ',', '.',   P,   Y,   F,   G,   C,   R,   L, '/', '=', '|',
        CAPS,  A, L5O, L2E,   I,   U,   D,HCTRL,  T,   N,   S, '-',    ENTER,
        #LSFT4,'"',  Q,   J,   K, L3X,   B,   M,   W,   V,   Z,         RSFT4,
        LSFT4,'"',  Q,   J,   K, L3X,   B,   M,   W,   V,   Z, MODS_TAP(MODS(RSHIFT), UP),
        #LCTRL, LGUI, LALT,      SPACECTRL,            RALT, MENU,  L1, RCTRL
        LCTRL, LGUI, LALT, SPACECTRL, RALT, MODS_TAP(MODS(RGUI), LEFT), LAYER_TAP(1, DOWN), MODS_TAP(MODS(RCTRL), RIGHT)
    ),

    # layer 1 Fn layer
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, ___,  UP, ___, ___, ___, ___, ___, ___, ___,SUSPEND,___,___,___,
        ___,LEFT,DOWN,RIGHT,___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___,BOOT, ___,MACRO(0), ___, ___, ___,       ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 2 E Nav Layer
    (
        '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, ___, ___, ___, ___, ___,___,PGUP, HOME, END,SINS,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
        ___, ___, ___, ___, ___, ___,LEFT,DOWN, UP,RIGHT, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___,PGDN,___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 3 X hardware function
    (
        BT_TOGGLE,BT1,BT2, BT3,BT4,BT5,BT6,BT7, BT8, BT9, BT0, ___, ___, ___,
        RGB_MOD, ___, ___, ___, ___, ___,___,USB_TOGGLE,___,___,___,___,___, ___,
        RGB_TOGGLE,HUE_RGB,RGB_HUE,SAT_RGB,RGB_SAT,___,___,___,___,___,___,___,      ___,
        ___, ___, ___, ___, ___, ___, ___, ___,VAL_RGB,RGB_VAL, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 4 modify 'SHIFT' layer, means: SHIFT + these keys
    # TODO: How to realize SHIFT + BACKSPACE = DEL?
    # Why E/X/H need to write again in this layer? bcz if no, long press will triger L2E L3X, not the Shift+E/X/H we want
    # Caps->ESC to realize Ctrl+Shift+Esc

    (
        '`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ESC, ___, ___,   E, ___, ___, ___,   H, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___,   X, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,              SPACE,                ___, ___, ___, ___
    ),

    # layer 5
    (
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, ___, ___, ___, ___, ___,MS_W_UP, MS_UL,MS_UP,  MS_UR, MS_BTN4, ___, ___, ___,
        ___, ___, ___, ___, ___, ___,MS_BTN1, MS_LT,MS_BTN3,MS_RT, MS_BTN2, ___,      ___,
        ___, ___, ___, ___, ___, ___,MS_W_DN, MS_DL,MS_DN,  MS_DR, MS_BTN5,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),
)

# Use different keymaps on different connections
# Valid keys are "USB" and "BT0"-"BT9"
# Connection not in this map will use default keymap defined above.
keyboard.profiles = {
    # For example, BT8 is connected to a Mac
    "BT8": (
        # QWERTY
        # layer 0
        (
            ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
            TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
            CAPS,  A,   S,   D,   F,   G,   H,   J,   K,   L, SCC, '"',    ENTER,
            LSHIFT,Z,   X,   C,   V,   B,   N,   M, ',', '.', '/',        RSHIFT,
            LCTRL, LALT, LGUI,          SPACE,            MENU, RALT,  L1, RCTRL
        ),

        # layer 1
        (
            '`',  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
            ___, ___,  UP, ___, ___, ___, ___, ___, ___, ___,SUSPEND,___,___,___,
            ___,LEFT,DOWN,RIGHT,___, ___, ___, ___, ___, ___, ___, ___,      ___,
            ___, ___, ___, ___, ___,BOOT, ___,MACRO(1), ___, ___, ___,       ___,
            ___, ___, ___,                ___,               ___, ___, ___,  ___
        ),
    )
}

# send text when a MACRO key is press down or release, n means the number MACRO(n)
def macro_handler(dev, n, is_down):
    if is_down:
        dev.send_text('You pressed macro #{}\n'.format(n))
    else:
        dev.send_text('You released macro #{}\n'.format(n))

# send text when two keys (named pair keys) are press down simultaneously, n means the order
def pairs_handler(dev, n):
    dev.send_text('You just triggered pair keys #{}\n'.format(n))


keyboard.macro_handler = macro_handler
keyboard.pairs_handler = pairs_handler

# the numbers below is not related with QWERTY layout, just means location
# ESC(0)    1(1)   2(2)   3(3)   4(4)   5(5)   6(6)   7(7)   8(8)   9(9)   0(10)  -(11)  =(12)  BACKSPACE(13)
# TAB(27)   Q(26)  W(25)  E(24)  R(23)  T(22)  Y(21)  U(20)  I(19)  O(18)  P(17)  [(16)  ](15)   \(14)
# CAPS(28)  A(29)  S(30)  D(31)  F(32)  G(33)  H(34)  J(35)  K(36)  L(37)  ;(38)  "(39)      ENTER(40)
#LSHIFT(52) Z(51)  X(50)  C(49)  V(48)  B(47)  N(46)  M(45)  ,(44)  .(43)  /(42)            RSHIFT(41)
# LCTRL(53)  LGUI(54)  LALT(55)               SPACE(56)          RALT(57)  MENU(58)  Fn(59)  RCTRL(60)

# Pairs: J & K, U & I
# keyboard.pairs = [{35, 36}, {20, 19}]

# keyboard.verbose = False

keyboard.run()
