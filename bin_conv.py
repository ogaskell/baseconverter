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


def ui_bin_to_ui_dec(n):
    if n.lstrip("-") != n:
        raise ValueError("Negative symbols are not supported in binary")
    else:
        d = int(n, 2)

    return d
