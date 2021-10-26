import math
from PIL import Image, ImageDraw

colors = ['#FFFFFF', "#EFEFEF", "#c0ffee"]

ang = 10

def horizontal(w, h):

    img = Image.new("RGB", (w, h))
    dr = ImageDraw.Draw(img)

    s = ((w / len(colors)) * -1)
    wi = w / len(colors) + s
    dr.polygon(
        (
            (
                math.floor(s) + ang,
                0
            ), 
            (
                math.floor(s) - ang,
                h-1
            ),
            (
                math.floor(wi) - ang, 
                h-1
            ),
            (
                math.floor(wi) + ang,
                0
            )
        ), fill = colors[-1])

    for a, b in enumerate(colors):
        s = ((w / len(colors)) * a)
        wi = w / len(colors) + s
        dr.polygon(
            (
                (
                    math.floor(s) + ang,
                    0
                ), 
                (
                    math.floor(s) - ang,
                    h-1
                ),
                (
                    math.floor(wi) - ang, 
                    h-1
                ),
                (
                    math.floor(wi) + ang,
                    0
                )
            ), fill = b)

    s = ((w / len(colors)) * len(colors)-1)
    wi = w / len(colors) + s
    dr.polygon(
        (
            (
                math.floor(s) + ang,
                0
            ), 
            (
                math.floor(s) - ang,
                h-1
            ),
            (
                math.floor(wi) - ang, 
                h-1
            ),
            (
                math.floor(wi) + ang,
                0
            )
        ), fill = colors[0])

    img.save(sys.argv[5])

def vertical(w, h):
    h, w = w, h

    img = Image.new("RGB", (w, h))
    dr = ImageDraw.Draw(img)

    s = ((h / len(colors)) * -1)
    hi = h / len(colors) + s
    dr.polygon(
        (
            (
                0,
                math.floor(s) + ang
            ), 
            (
                w-1,
                math.floor(s) - ang
            ),
            (
                w-1,
                math.floor(hi) - ang
            ),
            (
                0,
                math.floor(hi) + ang
            )
        ), fill = colors[-1])

    for a, b in enumerate(colors):
        s = ((h / len(colors)) * a)
        hi = h / len(colors) + s
        dr.polygon(
            (
                (
                    0, 
                    math.floor(s) + ang
                ),
                (
                    w-1,
                    math.floor(s) - ang
                ),
                (
                    w-1, 
                    math.floor(hi) - ang
                ),
                (
                    0,
                    math.floor(hi) + ang
                )
            ), fill = b)

    s = ((h / len(colors)) * len(colors)-1)
    hi = h / len(colors) + s
    dr.polygon(
        (
            (
                0,
                math.floor(s) + ang
            ), 
            (
                w-1,
                math.floor(s) - ang
            ),
            (
                w-1,
                math.floor(hi) - ang
            ),
            (
                0,
                math.floor(hi) + ang
            )
        ), fill = colors[0])

    img.save(sys.argv[5])

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