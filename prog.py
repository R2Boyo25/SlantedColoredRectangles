import math
from PIL import Image, ImageDraw

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

def perc(cur, all):
    return cur/all

def total(objs):
    totl = 0
    for amnt, colr in objs:
        totl += amnt
    return totl

def percNum(perc, num):
    return perc * num

def hor(wh, objs, *args, strtcolr = "#00000000", endcolr = "#00000000", angl = 20):
    img = Image.new("RGBA", (wh[0] * 10, wh[1] * 10))
    dr = ImageDraw.Draw(img)

    # start notch
    strt = -0.10 * wh[0]
    widt = 0
    polx(dr, strt, widt, wh, angl, strtcolr)

    totl = total(objs)
    totlperc = 0

    print(totl)

    for amnt, colr in objs:
        aprc = percNum(perc(amnt, totl), wh[0])

        strt = totlperc
        totlperc += aprc 
        widt = totlperc

        print(totlperc)
        
        polx(dr, math.floor(strt), math.ceil(widt), wh, angl, colr)

    # end notch
    strt = wh[0]
    widt = wh[0] + ( 0.10 * wh[0] )
    polx(dr, strt, widt, wh, angl, endcolr)

    nimg = img.resize( (wh[0], wh[1] ), resample = Image.ANTIALIAS )

    return nimg


if __name__ == '__main__':
    colors = [(20, '#FF0000'), (30, "#00FF00"), (50, "#c0ffee")]

    hor((300, 100), colors).show()

    quit()

    ang = 10

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