import os
from PIL import Image


def crop(path, ip, height, width):
    im = Image.open(ip)
    imgwidth, imgheight = im.size
    k = 0
    for i in range(0, imgheight, height):
        for j in range(0, imgwidth, width):
            box = (j, i, j + width, i + height)
            a = im.crop(box)
            a.save(os.path.join(path, "IMG-%s.png" % k))

            k += 1


crop('/home/prime/Desktop', '/home/prime/Desktop/train_4249_0000.png', 256, 25)
