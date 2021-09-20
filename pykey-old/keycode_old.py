# SPDX-FileCopyrightText: 2021 Pierre Constantineau
# SPDX-License-Identifier: MIT
"""
These keycodes are based on Universal Serial Bus HID Usage Tables Document 
Version 1.12
Chapter 10: Keyboard/Keypad Page(0x07) - Page 53
https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
"""

class Keycode:
    NO        = 0x00
    XXXXXXX   = 0x00
    ROLL_OVER = 0x01
    TRANSPARENT = 0x01
    TRNS      = 0x01
    _______   = 0x01 
    POST_FAIL = 0x02  
    UNDEFINED = 0x03

    A = 0x04
    B = 0x05
    C = 0x06
    D = 0x07
    E = 0x08
    F = 0x09
    G = 0x0A
    H = 0x0B
    I = 0x0C
    J = 0x0D
    K = 0x0E
    L = 0x0F
    M = 0x10
    N = 0x11
    O = 0x12
    P = 0x13
    Q = 0x14
    R = 0x15
    S = 0x16
    T = 0x17
    U = 0x18
    V = 0x19
    W = 0x1A
    X = 0x1B
    Y = 0x1C
    Z = 0x1D
    ONE = 0x1E
    TWO = 0x1F
    THREE = 0x20
    FOUR = 0x21
    FIVE = 0x22
    SIX = 0x23
    SEVEN = 0x24
    EIGHT = 0x25
    NINE = 0x26
    ZERO = 0x27
    ENTER = 0x28
    ESCAPE = 0x29
    BSPACE = 0x2A
    TAB = 0x2B
    SPACE = 0x2C
    MINUS = 0x2D
    EQUAL = 0x2E
    LBRACKET = 0x2F
    RBRACKET = 0x30
    BSLASH = 0x31
    NONUS_HASH = 0x32
    SCOLON = 0x33
    QUOTE = 0x34
    GRAVE = 0x35
    COMMA = 0x36
    DOT = 0x37
    SLASH = 0x38
    CAPSLOCK = 0x39
    F1 = 0x3A
    F2 = 0x3B
    F3 = 0x3C
    F4 = 0x3D
    F5 = 0x3E
    F6 = 0x3F
    F7 = 0x40
    F8 = 0x41
    F9 = 0x42
    F10 = 0x43
    F11 = 0x44
    F12 = 0x45
    PSCREEN = 0x46
    SCROLLLOCK = 0x47
    PAUSE = 0x48
    INSERT = 0x49
    HOME = 0x4A
    PGUP = 0x4B
    DELETE = 0x4C
    END = 0x4D
    PGDOWN = 0x4E
    RIGHT = 0x4F
    LEFT = 0x50
    DOWN = 0x51
    UP = 0x52
    NUMLOCK = 0x53
    KP_SLASH = 0x54
    KP_ASTERISK = 0x55
    KP_MINUS = 0x56
    KP_PLUS = 0x57
    KP_ENTER = 0x58
    KP_1 = 0x59
    KP_2 = 0x5A
    KP_3 = 0x5B
    KP_4 = 0x5C
    KP_5 = 0x5D
    KP_6 = 0x5E
    KP_7 = 0x5F
    KP_8 = 0x60
    KP_9 = 0x61
    KP_0 = 0x62
    KP_DOT = 0x63
    NONUS_BSLASH = 0x64
    APPLICATION = 0x65
    POWER = 0x66
    KP_EQUAL = 0x67
    F13 = 0x68
    F14 = 0x69
    F15 = 0x6A
    F16 = 0x6B
    F17 = 0x6C
    F18 = 0x6D
    F19 = 0x6E
    F20 = 0x6F
    F21 = 0x70
    F22 = 0x71
    F23 = 0x72
    F24 = 0x73
    EXECUTE = 0x74
    HELP = 0x75
    MENU = 0x76
    SELECT = 0x77
    STOP = 0x78
    AGAIN = 0x79
    UNDO = 0x7A
    CUT = 0x7B
    COPY = 0x7C
    PASTE = 0x7D
    FIND = 0x7E
    MUTE = 0x7F
    VOLUP = 0x80
    VOLDOWN = 0x81
    LOCKING_CAPS = 0x82
    LOCKING_NUM = 0x83
    LOCKING_SCROLL = 0x84
    KP_COMMA = 0x85
    KP_EQUAL_AS400 = 0x86
    INT1 = 0x87
    INT2 = 0x88
    INT3 = 0x89
    INT4 = 0x8A
    INT5 = 0x8B
    INT6 = 0x8C
    INT7 = 0x8D
    INT8 = 0x8E
    INT9 = 0x8F
    LANG1 = 0x90
    LANG2 = 0x91
    LANG3 = 0x92
    LANG4 = 0x93
    LANG5 = 0x94
    LANG6 = 0x95
    LANG7 = 0x96
    LANG8 = 0x97
    LANG9 = 0x98
    ALT_ERASE = 0x99
    SYSREQ = 0x9A
    CANCEL = 0x9B
    CLEAR = 0x9C
    PRIOR = 0x9D
    RETURN = 0x9E
    SEPARATOR = 0x9F
    OUT = 0xA0
    OPER = 0xA1
    CLEAR_AGAIN = 0xA2
    CRSEL = 0xA3
    EXSEL = 0xA4

    # LAST OF THE VALID KEYCODES ANYTHING BELOW SHOULD BE FILTERED OUT
    RESERVED_A5 = 0xA5  # Used as macro identifier
    RESERVED_A6 = 0xA6
    RESERVED_A7 = 0xA7
    RESERVED_A8 = 0xA8
    RESERVED_A9 = 0xA9
    RESERVED_AA = 0xAA
    RESERVED_AB = 0xAB
    RESERVED_AC = 0xAC
    RESERVED_AD = 0xAD
    RESERVED_AE = 0xAE
    RESERVED_AF = 0xAF

    LCTRL       = 0xE0
    LSHIFT      = 0xE1
    LALT        = 0xE2
    LGUI        = 0xE3
    RCTRL       = 0xE4
    RSHIFT      = 0xE5
    RALT        = 0xE6
    RGUI        = 0xE7

    LAYER_0  =    0xF0
    LAYER_1  =    0xF1
    LAYER_2  =    0xF2
    LAYER_3  =    0xF3
    LAYER_4  =    0xF4
    LAYER_5  =    0xF5
    LAYER_6  =    0xF6
    LAYER_7  =    0xF7
    LAYER_8  =    0xF8
    LAYER_9  =    0xF9
    LAYER_A  =    0xFA
    LAYER_B  =    0xFB
    LAYER_C  =    0xFC
    LAYER_D  =    0xFD
    LAYER_E  =    0xFE
    LAYER_F  =    0xFF


    LCTL = LCTRL
    RCTL = RCTRL
    LSFT = LSHIFT
    RSFT = RSHIFT
    ESC  = ESCAPE
    BSPC = BSPACE
    ENT  = ENTER
    DEL  = DELETE
    INS  = INSERT
    CAPS = CAPSLOCK
    CLCK = CAPSLOCK
    RGHT = RIGHT
    PGDN = PGDOWN
    PSCR = PSCREEN
    SLCK = SCROLLLOCK
    PAUS = PAUSE
    BRK  = PAUSE
    NLCK = NUMLOCK
    SPC  = SPACE
    MINS = MINUS
    EQL  = EQUAL
    GRV  = GRAVE
    RBRC = RBRACKET
    LBRC = LBRACKET
    COMM = COMMA
    BSLS = BSLASH
    SLSH = SLASH
    SCLN = SCOLON
    QUOT = QUOTE
    APP  = APPLICATION
    NUHS = NONUS_HASH
    NUBS = NONUS_BSLASH
    LCAP = LOCKING_CAPS
    LNUM = LOCKING_NUM
    LSCR = LOCKING_SCROLL
    ERAS = ALT_ERASE
    CLR  = CLEAR
    # Japanese specific
    ZKHK = GRAVE
    RO   = INT1
    KANA = INT2
    JYEN = INT3
    HENK = INT4
    MHEN = INT5
    # Korean specific 
    HAEN = LANG1
    HANJ = LANG2
    # Keypad 
    P1   = KP_1
    P2   = KP_2
    P3   = KP_3
    P4   = KP_4
    P5   = KP_5
    P6   = KP_6
    P7   = KP_7
    P8   = KP_8
    P9   = KP_9
    P0   = KP_0
    PDOT = KP_DOT
    PCMM = KP_COMMA
    PSLS = KP_SLASH
    PAST = KP_ASTERISK
    PMNS = KP_MINUS
    PPLS = KP_PLUS
    PEQL = KP_EQUAL
    PENT = KP_ENTER
    # Unix function key
    EXEC = EXECUTE
    SLCT = SELECT
    AGIN = AGAIN
    PSTE = PASTE


    # GUI key aliases
    LCMD = LGUI
    LWIN = LGUI
    RCMD = RGUI
    RWIN = RGUI

    BIT_LCTRL = (1)
    BIT_LSHIFT = (2)
    BIT_LALT = (4)
    BIT_LGUI = (8)
    BIT_RCTRL = (16)
    BIT_RSHIFT = (32)
    BIT_RALT = (64)
    BIT_RGUI = (128)

    MOD_LCTRL = (BIT_LCTRL << 8)
    MOD_LSHIFT = (BIT_LSHIFT << 8)
    MOD_LALT = (BIT_LALT << 8)
    MOD_LGUI = (BIT_LGUI << 8)
    MOD_RCTRL = (BIT_RCTRL << 8)
    MOD_RSHIFT = (BIT_RSHIFT << 8)
    MOD_RALT = (BIT_RALT << 8)
    MOD_RGUI = (BIT_RGUI << 8)

    def MOD(M, KC):
        return ( KC |  M )

    def LALT(KEY):
        return  ( KEY | ((4) << 8) ) 

    def RALT(KEY):
        return  ( KEY | ((64)<< 8) ) 

    def LCTL(KEY): 
        return  ( KEY | ((1)<< 8) ) 

    def RCTL(KEY): 
        return  ( KEY | ((16) << 8) ) 

    def RSFT(KEY): 
        return  ( KEY | ((32) << 8) ) 

    def LSFT(KEY): 
        return  ( KEY | ((2) << 8) ) 

    def LGUI(KEY): 
        return  ( KEY | ((8) << 8) ) 

    def RGUI(KEY): 
        return  ( KEY | ((128) << 8) ) 

    def S(KEY):
        return  ( KEY | ((2) << 8) ) 

    LT =  MOD(MOD_LSHIFT, COMMA)
    GT =  MOD(MOD_LSHIFT, DOT)

    TILD = MOD(MOD_LSHIFT, GRV)
    EXLM = MOD(MOD_LSHIFT, ONE)
    AT   = MOD(MOD_LSHIFT, TWO)
    HASH = MOD(MOD_LSHIFT, THREE)
    DLR  = MOD(MOD_LSHIFT, FOUR)
    PERC = MOD(MOD_LSHIFT, FIVE)
    CIRC = MOD(MOD_LSHIFT, SIX)
    AMPR = MOD(MOD_LSHIFT, SEVEN)
    ASTR = MOD(MOD_LSHIFT, EIGHT)
    LPRN = MOD(MOD_LSHIFT, NINE)
    RPRN = MOD(MOD_LSHIFT, ZERO)
    UNDS = MOD(MOD_LSHIFT, MINUS)
    PLUS = MOD(MOD_LSHIFT, EQUAL)

    LCBR = MOD(MOD_LSHIFT, LBRC)
    RCBR = MOD(MOD_LSHIFT, RBRC)
    PIPE = MOD(MOD_LSHIFT, BSLS)

    COLN = MOD(MOD_LSHIFT, SCLN)
    DQUO = MOD(MOD_LSHIFT, QUOTE)
    DQT = DQUO

    LT   = MOD(MOD_LSHIFT, COMMA)
    GT   = MOD(MOD_LSHIFT, DOT)
    QUES = MOD(MOD_LSHIFT, SLASH)

    NUTL = MOD(MOD_LSHIFT,NUHS)
    NUPI = MOD(MOD_LSHIFT,NUBS)


    LABK = LT
    RABK = GT

    def MC(KC):
        return (( KC << 8 ) | 0xA5 )            # move KC to upper 8 bits and use RESERVED_A5 keycode for marking this as a macro.

    def KB(KC): 
        return (( KC << 8 ) | 0xA6 )             # move KC to upper 8 bits and use RESERVED_A6 keycode for marking this as a special keyboard function.

    def MK(KC): 
        return (( KC << 8 ) | 0xA7 )             # move KC to upper 8 bits and use RESERVED_A7 keycode for marking this as a media key.

    def MS(KC):
        return (( KC << 8 ) | 0xA9 )           # move KC to upper 8 bits and use RESERVED_A9 keycode for marking this as a mouse key.

    # Mousekey
    MS_OFF  =   MS(A)
    MS_UP   =   MS(B)
    MS_DOWN =   MS(C)
    MS_LEFT =   MS(D)
    MS_RIGHT =  MS(E)
    MS_BTN1  =  MS(F)
    MS_BTN2  =  MS(G)
    MS_BTN3  =  MS(H)
    MS_BTN4  =  MS(I)
    MS_BTN5  =  MS(J)
    MS_WH_UP   = MS(K)
    MS_WH_DOWN = MS(L)
    MS_WH_DN   = MS_WH_DOWN
    MS_WH_LEFT =   MS(M)
    MS_WH_RIGHT =  MS(N)
    MS_ACCEL0 =  MS(O)  
    MS_ACCEL1 =  MS(P)  
    MS_ACCEL2 =  MS(Q)  
    MS_U = MS_UP
    MS_D = MS_DOWN
    MS_L = MS_LEFT
    MS_R = MS_RIGHT
    BTN1 = MS_BTN1
    BTN2 = MS_BTN2
    BTN3 = MS_BTN3
    BTN4 = MS_BTN4
    BTN5 = MS_BTN5
    WH_U = MS_WH_UP
    WH_D = MS_WH_DOWN
    WH_L = MS_WH_LEFT
    WH_R = MS_WH_RIGHT
    ACL0 = MS_ACCEL0
    ACL1 = MS_ACCEL1
    ACL2 = MS_ACCEL2