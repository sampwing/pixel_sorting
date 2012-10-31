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
    global row
    while column < width-1:
        sortColumn()
        column += 1
    while row < height - 1:
        sortRow()
        row += 1

def case0(x, y):
        y = getFirstNotBlackY(x, y)
        yend = getNextBlackY(x, y)
        return y, yend

def caseX0(x, y):
        x = getFirstNotBlackX(x, y)
        xend = getNextBlackX(x, y)
        return x, xend

def sortRow():
    x = 0
    y = row
    xend = 0

    while xend < width-1:
        x, xend = caseX0(x, y)
        if x < 0:
            break
        sortLength = xend-x

        unsorted = [0] * sortLength
        for i in xrange(sortLength):
            #unsorted[i] = img.pixels[x + i + y * img.width]
            unsorted[i] = pix[x + 1, y]


        _sorted = sorted(unsorted)

        for i in xrange(sortLength):
            pix[x + 1, y] = _sorted[i]
        x = xend+1
  



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
    c = pix[x, y]
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
