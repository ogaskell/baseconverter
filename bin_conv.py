"""KEY
u: unsigned integer
t: two's compliment
s: sign+magnitude

i: integer
f: floating point

bin: Binary,      Base 2
oct: Octal,       Base 8
dec: Decimal,     Base 10
hex: Hexadecimal, Base 16
"""

import math

# DEC TO BIN


def ui_dec_to_ui_bin(n, bits=0):
    n = float(n)
    if n < 0:
        raise ValueError("Negative number " + str(n) + " cannot be converted to unsigned binary")
    elif n % 1 != 0:
        raise ValueError("Fractional number " + str(n) + " cannot be converted to integer.")
    else:
        b = str(bin(int(n)))[2:]

    if bits == 0:
        return b
    elif bits < 0:
        raise ValueError("Number of bits cannot be negative, bits="+str(bits))
    elif bits % 1 != 0:
        raise ValueError("Number of bits cannot be fractional, bits="+str(bits))
    else:
        return ('{:0>'+str(int(bits))+'}').format(b)


def ti_dec_to_ti_bin(n):
    return "UNIMPLEMENTED"


def tf_dec_to_tf_bin(n):
    return "UNIMPLEMENTED"


# BIN TO DEC


def ui_bin_to_ui_dec(n):
    n = n.replace(" ", "")
    if n.lstrip("-") != n:
        raise ValueError("Negative symbols are not supported in binary")
    elif str(n).replace("1", "").replace("0", "") != "":
        raise ValueError("Binary cannot contain characters other than 1, 0 and whitespace")
    else:
        d = int(n, 2)

    return d


def ti_bin_to_ti_dec(n):
    return "UNIMPLEMENTED"


def tf_bin_to_tf_dec(n):
    return "UNIMPLEMENTED"


# DEC TO HEX


def ui_dec_to_ui_hex(n):
    return "UNIMPLEMENTED"


def ti_dec_to_ti_hex(n):
    return "UNIMPLEMENTED"


def tf_dec_to_tf_hex(n):
    return "UNIMPLEMENTED"


# HEX TO DEC


def ui_hex_to_ui_dec(n):
    return "UNIMPLEMENTED"


def ti_hex_to_ti_dec(n):
    return "UNIMPLEMENTED"


def tf_hex_to_tf_dec(n):
    return "UNIMPLEMENTED"


# BIN TO HEX

hexnums = list("0123456789ABCDEF")
binnums = ["0000",
           "0001",
           "0010",
           "0011",
           "0100",
           "0101",
           "0110",
           "0111",
           "1000",
           "1001",
           "1010",
           "1011",
           "1100",
           "1101",
           "1110",
           "1111",
           ]


def bin_to_hex(n):
    b = ('{:0>' + str(math.ceil(len(n)/4)*4) + '}').format(n.replace(" ", ""))
    splitb = [b[i:i+4] for i in range(0, len(b), 4)]

    splith = list(map(lambda x: hexnums[binnums.index('{:0<4}'.format(x))], splitb))
    h = "".join(splith)

    return h


# HEX TO BIN


def hex_to_bin(n):
    h = list(n)

    splitb = list(map(lambda x: binnums[hexnums.index(x)], h))
    b = "".join(splitb)

    return b
