from PIL import Image
img = Image.open('octo.png')
pix = img.load()

pix[1,2] = 0


mode = 0 
loops = 1

blackValue = -10000000
brigthnessValue = 60
whiteValue = -6000000

row = 0
column = 0
width, height = img.size

def draw():
    global column
    while column < width-1:
        sortColumn()
        column += 1

def case0(x, y):
        y = getFirstNotBlackY(x, y)
        yend = getNextBlackY(x, y)
        return y, yend

def sortColumn():
    x = column
    y = 0
    yend = 0
    while yend < height - 1:
        if mode == 0: 
            y, yend = case0(x, y)
        if y < 0:
            break
        sortLength = yend - y
        unsorted = [0] * sortLength
        for i in xrange(sortLength):
            unsorted[i] = pix[x, (y + i)]
        _sorted = sorted(unsorted)
        for i in xrange(sortLength):
            pix[x, (y+i)] = _sorted[i]
        y = yend + 1
    
def getFirstNotBlackX(_x, _y):
    x = _x
    y = _y
    c = pix[x, y]
    while c  < blackValue:
        x += 1
        if x >= width:
            return -1
        c = pix[x, y]
    return x

def getNextBlackX(_x, _y):
    x = _x + 1
    y = _y
    d = pix[x, y]
    prc, blackValue
    while c > blackValue:
        x += 1
        if x >= width:
            return width - 1
        c = pix[x, y]
    return x-1

def getFirstNotBlackY(_x, _y):
    x = _x
    y = _y
    if y < height:
        c = pix[x, y]
        while c < blackValue:
            y += 1
            if y >= height:
                return -1
    return y

def getNextBlackY(_x, _y):
    x = _x
    y = _y + 1
    if y < height:
        c = pix[x, y]
        while c > blackValue:
            y += 1
            if y >= height:
                return height - 1

    return y-1

draw()
img.save('ouput.png')
#primg.size
