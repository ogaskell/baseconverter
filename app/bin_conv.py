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

# DEC TO BIN


def ui_dec_to_ui_bin(n, bits=0):
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
    if n.lstrip("-") != n:
        raise ValueError("Negative symbols are not supported in binary")
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


def bin_to_hex(n):
    return "UNIMPLEMENTED"


# HEX TO BIN


def hex_to_bin(n):
    return "UNIMPLEMENTED"
