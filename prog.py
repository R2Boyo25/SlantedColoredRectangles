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

def perc(cur, all):
    return cur/all

def total(objs):
    totl = 0
    for amnt, colr in objs:
        totl += amnt
    return totl

def percNum(perc, num):
    return perc * num

def hor(wh : "(width, height)", objs, *args, strtcolr = "#00000000", endcolr = "#00000000", angl = 20, totl = 0):
    img = Image.new("RGBA", (wh[0] * 10, wh[1] * 10))
    dr = ImageDraw.Draw(img)

    # start notch
    strt = -0.10 * wh[0]
    widt = 0
    polx(dr, strt, widt, wh, angl, strtcolr)

    totl = total(objs) if totl == 0 else totl
    totlperc = 0

    for amnt, colr in objs:
        aprc = percNum(perc(amnt, totl), wh[0])

        strt = totlperc
        totlperc += aprc 
        widt = totlperc
        
        polx(dr, math.floor(strt), math.ceil(widt), wh, angl, colr)

    # end notch
    strt = wh[0]
    widt = wh[0] + ( 0.10 * wh[0] )
    polx(dr, strt, widt, wh, angl, endcolr)

    nimg = img.resize( (wh[0], wh[1] ), resample = Image.ANTIALIAS )

    return nimg

def ver(wh : "(width, height)", objs, *args, strtcolr = "#00000000", endcolr = "#00000000", angl = 10, totl = 0):
    img = Image.new("RGBA", (wh[0] * 10, wh[1] * 10))
    dr = ImageDraw.Draw(img)

    # start notch
    strt = -0.10 * wh[1]
    high = 0
    poly(dr, strt, high, wh, angl, strtcolr)

    totl = total(objs) if totl == 0 else totl
    totlperc = 0

    for amnt, colr in objs:
        aprc = percNum(perc(amnt, totl), wh[1])

        strt = totlperc
        totlperc += aprc 
        high = totlperc
        
        poly(dr, math.floor(strt), math.ceil(high), wh, angl, colr)

    # end notch
    strt = wh[1]
    high = wh[1] + ( 0.10 * wh[1] )
    poly(dr, strt, high, wh, angl, endcolr)

    nimg = img.resize( (wh[0], wh[1] ), resample = Image.ANTIALIAS )

    return nimg


if __name__ == '__main__':
    import subprocess, sys
    df = subprocess.Popen(["df", "/"], stdout=subprocess.PIPE)
    output = df.communicate()[0]
    #device, size, used, available, percent, mountpoint = \
    e = output.decode().split("\n")[1].split()

    print(e[2], e[3])

    #colors = [(20, '#FF0000'), (30, "#00FF00"), (50, "#c0ffee")]

    colors = [(int(e[2]), '#FE8411'), (int(e[3]), "#FFFFFF")]

    #hor((300, 100), colors, strtcolr = "#010000", endcolr = "#010000").save(sys.argv[1])
    #ver((100, 300), colors, strtcolr = "#010000", endcolr = "#010000").save(sys.argv[1])
    hor((300, 100), colors, angl = -20).save(sys.argv[1])
    #ver((100, 300), colors).save(sys.argv[1])
