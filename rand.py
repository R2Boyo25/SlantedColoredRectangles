import math
from PIL import Image, ImageDraw, ImageFilter

colors = ['#FFFFFF', "#EFEFEF", "#c0ffee"]

ang = 10

def polx(dr, s, i, wh, ang, color):
    h = wh[1]
    dr.polygon(
            (
                (
                    (math.floor(s) + ang)*10,
                    0
                ), 
                (
                    (math.floor(s) - ang)*10,
                    (h)*10
                ),
                (
                    (math.floor(i) - ang)*10, 
                    (h)*10
                ),
                (
                    (math.floor(i) + ang)*10,
                    0
                )
            ), fill = color)

def poly(dr, s, i, wh, ang, color):
    w = wh[0]
    dr.polygon(
            (
                (
                    0, 
                    (math.floor(s) + ang)*10
                ),
                (
                    (w)*10,
                    (math.floor(s) - ang)*10
                ),
                (
                    (w)*10, 
                    (math.floor(i) - ang)*10
                ),
                (
                    0,
                    (math.floor(i) + ang)*10
                )
            ), fill = color)

def horizontal(w, h):

    img = Image.new("RGB", (w*10, h*10))
    dr = ImageDraw.Draw(img)

    s = ((w / len(colors)) * -1)
    wi = w / len(colors) + s
    polx(dr, s, wi, (w, h), ang, colors[-1])

    for a, b in enumerate(colors):
        s = ((w / len(colors)) * a)
        wi = w / len(colors) + s
        polx(dr, s, wi, (w, h), ang, b)

    s = ((w / len(colors)) * len(colors)-1)
    wi = w / len(colors) + s
    polx(dr, s, wi, (w, h), ang, colors[0])

    nimg = img.resize((w, h), resample=Image.ANTIALIAS)

    nimg.save(sys.argv[5])

def vertical(w, h):
    h, w = w, h

    img = Image.new("RGB", (w*10, h*10))
    dr = ImageDraw.Draw(img)

    s = ((h / len(colors)) * -1)
    hi = h / len(colors) + s
    poly(dr, s, hi, (w, h), ang, colors[-1])

    for a, b in enumerate(colors):
        s = ((h / len(colors)) * a)
        hi = h / len(colors) + s
        poly(dr, s, hi, (w, h), ang, b)

    s = ((h / len(colors)) * len(colors)-1)
    hi = h / len(colors) + s
    poly(dr, s, hi, (w, h), ang, colors[0])

    nimg = img.resize((w, h), resample=Image.ANTIALIAS)

    nimg.save(sys.argv[5])

import sys

def setColors(colorss):
    global colors
    colors = []
    for color in colorss:
        colors.append('#' + color.lstrip('#'))

setColors(sys.argv[6:])
if sys.argv[1] == 'h':
    ang = int(sys.argv[4])
    horizontal(int(sys.argv[2]), int(sys.argv[3]))
elif sys.argv[1] == 'v':
    ang = int(sys.argv[4])
    vertical(int(sys.argv[2]), int(sys.argv[3]))