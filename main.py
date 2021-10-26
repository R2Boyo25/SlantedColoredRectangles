import math
from PIL import Image, ImageDraw, ImageFilter

colors = ['#FFFFFF', "#EFEFEF", "#c0ffee"]

ang = 10

def horizontal(w, h):

    img = Image.new("RGB", (w*10, h*10))
    dr = ImageDraw.Draw(img)

    s = ((w / len(colors)) * -1)
    wi = w / len(colors) + s
    dr.polygon(
        (
            (
                (math.floor(s) + ang)*10,
                0
            ), 
            (
                (math.floor(s) - ang)*10,
                (h-1)*10
            ),
            (
                (math.floor(wi) - ang)*10, 
                (h-1)*10
            ),
            (
                (math.floor(wi) + ang)*10,
                0
            )
        ), fill = colors[-1])

    for a, b in enumerate(colors):
        s = ((w / len(colors)) * a)
        wi = w / len(colors) + s
        dr.polygon(
            (
                (
                    (math.floor(s) + ang)*10,
                    0
                ), 
                (
                    (math.floor(s) - ang)*10,
                    (h-1)*10
                ),
                (
                    (math.floor(wi) - ang)*10, 
                    (h-1)*10
                ),
                (
                    (math.floor(wi) + ang)*10,
                    0
                )
            ), fill = b)

    s = ((w / len(colors)) * len(colors)-1)
    wi = w / len(colors) + s
    dr.polygon(
        (
            (
                (math.floor(s) + ang)*10,
                0
            ), 
            (
                (math.floor(s) - ang)*10,
                (h-1)*10
            ),
            (
                (math.floor(wi) - ang)*10, 
                (h-1)*10
            ),
            (
                (math.floor(wi) + ang)*10,
                0
            )
        ), fill = colors[0])

    nimg = img.resize((w, h), resample=Image.ANTIALIAS)

    nimg.save(sys.argv[5])

def vertical(w, h):
    h, w = w, h

    img = Image.new("RGB", (w*10, h*10))
    dr = ImageDraw.Draw(img)

    s = ((h / len(colors)) * -1)
    hi = h / len(colors) + s
    dr.polygon(
        (
            (
                0,
                (math.floor(s) + ang)*10
            ), 
            (
                (w-1)*10,
                (math.floor(s) - ang)*10
            ),
            (
                (w-1)*10,
                (math.floor(hi) - ang)*10
            ),
            (
                0,
                (math.floor(hi) + ang)*10
            )
        ), fill = colors[-1])

    for a, b in enumerate(colors):
        s = ((h / len(colors)) * a)
        hi = h / len(colors) + s
        dr.polygon(
            (
                (
                    0, 
                    (math.floor(s) + ang)*10
                ),
                (
                    (w-1)*10,
                    (math.floor(s) - ang)*10
                ),
                (
                    (w-1)*10, 
                    (math.floor(hi) - ang)*10
                ),
                (
                    0,
                    (math.floor(hi) + ang)*10
                )
            ), fill = b)

    s = ((h / len(colors)) * len(colors)-1)
    hi = h / len(colors) + s
    dr.polygon(
        (
            (
                0,
                (math.floor(s) + ang)*10
            ), 
            (
                (w-1)*10,
                (math.floor(s) - ang)*10
            ),
            (
                (w-1)*10,
                (math.floor(hi) - ang)*10
            ),
            (
                0,
                (math.floor(hi) + ang)*10
            )
        ), fill = colors[0])

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