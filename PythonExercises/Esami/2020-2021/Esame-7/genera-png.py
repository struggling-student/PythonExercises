
import images, sys, os, random

try:
    _, numcol, W, H = sys.argv
except :
    print('Usage: genera_png numcol width height')
    sys.exit()

numcol = int(numcol)
W      = int(W)
H      = int(H)

black  = (0,0,0)

img = [ [black]*W  for _ in range(H) ]
palette = [ (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150)) for _ in range(numcol-1) ]
for x in range(0,W,1):
    for y in range(0,H,1):
        c = random.choice(palette)
        #for X in range(x, x+4):
        #    for Y in range(y, y+4):
        try:
            img[y][x] = c
        except :
            pass

images.save(img, f'{W}-{H}-{numcol}.png')

print(len(set(palette)))

