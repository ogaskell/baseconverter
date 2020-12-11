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

        try:
            signed = {"on": True, "": False}[request.POST.get('signed', '')]
        except KeyError:
            signed = False

        try:
            floating = {"on": True, "": False}[request.POST.get('floating')]
        except KeyError:
            floating = False

        return render(request, 'app/convert.html', {"input":      str(inputv),
                                                    "inbase":     bases[str(inbase)],
                                                    "result":     "80",
                                                    "resultbase": bases[str(outbase)],
                                                    "floating":   str(floating),
                                                    "signed":     str(signed),
                                                    })
