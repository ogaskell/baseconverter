"""Functions to render pages."""

from django.shortcuts import render, redirect
import bin_conv as bc

bases = {"bin": "2 - Binary",
         "dec": "10 - Decimal",
         "hex": "16 - Hexadecimal"}


def index(request):
    """Index page on site."""
    return render(request, 'app/index.html', {})


def convert(request):
    """Page to convert numbers."""
    if request.method == "GET":
        return redirect("index")
    elif request.method == "POST":
        inbase = request.POST.get('sbase', '')
        inputv = request.POST.get('in', '')

        outbase = request.POST.get('tbase', '')

        error = ""

        try:
            signed = {"on": True, "": False}[request.POST.get('signed', '')]
        except KeyError:
            signed = False

        try:
            floating = {"on": True, "": False}[request.POST.get('floating')]
        except KeyError:
            floating = False

        if inputv == "":
            result = "ERROR"
            error = "Blank input value"
        elif inbase == outbase:
            result = "ERROR"
            error = "Input base and output base cannot be the same"
        else:
            if inbase == "bin":
                print("OK")
                if outbase == "dec":
                    if not signed and not floating:
                        result = bc.ui_bin_to_ui_dec(inputv)
                    if signed and not floating:
                        result = bc.ti_bin_to_ti_dec(inputv)
                    if signed and floating:
                        result = bc.tf_bin_to_tf_dec(inputv)
                    if not signed and floating:
                        result = "ERROR"
                        error = "Floating Binary must also be signed"
                elif outbase == "hex":
                    result = bc.bin_to_hex(inputv)
                else:
                    result = "ERROR"
                    error = "Unknown error 0 occured"
            elif inbase == "dec":
                if outbase == "bin":
                    if not signed and not floating:
                        result = bc.ui_dec_to_ui_bin(inputv)
                    if signed and not floating:
                        result = bc.ti_dec_to_ti_bin(inputv)
                    if signed and floating:
                        result = bc.tf_dec_to_tf_bin(inputv)
                    if not signed and floating:
                        result = "ERROR"
                        error = "Floating Binary must also be signed"
                elif outbase == "hex":
                    if not signed and not floating:
                        result = bc.ui_dec_to_ui_hex(inputv)
                    if signed and not floating:
                        result = bc.ti_dec_to_ti_hex(inputv)
                    if signed and floating:
                        result = bc.tf_dec_to_tf_hex(inputv)
                    if not signed and floating:
                        result = "ERROR"
                        error = "Floating hex must also be signed"
                else:
                    result = "ERROR"
                    error = "Unknown error 1 occured"
            elif inbase == "hex":
                if outbase == "dec":
                    if not signed and not floating:
                        result = bc.ui_hex_to_ui_dec(inputv)
                    if signed and not floating:
                        result = bc.ti_hex_to_ti_dec(inputv)
                    if signed and floating:
                        result = bc.tf_hex_to_tf_dec(inputv)
                    if not signed and floating:
                        result = "ERROR"
                        error = "Floating hex must also be signed"
                if outbase == "bin":
                    result = bc.hex_to_bin(inputv)
                else:
                    result = "ERROR"
                    error = "Unknown error 2 occured"
            else:
                result = "ERROR"
                error = "Unknown error 3 occured"

        return render(request, 'app/convert.html', {"input":      str(inputv),
                                                    "inbase":     bases[str(inbase)],
                                                    "result":     str(result),
                                                    "resultbase": bases[str(outbase)],
                                                    "floating":   str(floating),
                                                    "signed":     str(signed),
                                                    "error":      error,
                                                    })
