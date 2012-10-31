from PIL import Image
img = Image.open('octo.png')
pix = img.load()

pix[1,2] = 0

img.save('ouput.png')
#print img.size

mode = 0 
def draw():
    while column < width-1:
        sortColumn()
        column += 1

def sortColumn():
    x = column
    y = 0
    yend = 0

    def case0():
        y = getFirstNotBlackY(x, y)
        yend = getNextBlackY(x, y)

    _switch = {0: lambda: case0}

    while yend < height - 1:
        _switch[mode]()

        if y < 0:
            break

        sortLength = yend - y

        unsorted = [0] * sortLength

        for i in xrange(sortLength):
            #unsorted[i] = img.pixels[x + (y + i) * img.width]
            unsorted[i] = pix[x, (y + i)]
        

        sorted = sort(unsorted)

        for i in xrange(sortLength):
            #img.pixels[x + (y+i) * img.width] = sorted[i]
            pix[x, (y+i)] = sorted[i]
        y = yend + 1
    
def getFirstNotBlackX(_x, _y):
    x = _x
    y = _y
    c = pix[x, y]
    while c  < blackValue:
        #c = img.pixels[x + y * img.width]
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
