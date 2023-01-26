import numpy as np
from PIL import Image

class Canvas:
    def __init__(self, width, heigth, colour):
        self.width = width
        self.height = heigth
        self.colour = colour

        # create and 3d numpy array of zeroes
        self.data = np.zeros((self.height, self.width, 3), dtype=uint8)
        # assign the colour data to the 3d array
        self.data[:] = self.colour

    def make(self, imagepath):
        #convert the current array into a image file
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)


class square:
    def __init__(self, x, y, width, colour):
        self.x = x
        self.y = y
        self.width = width
        self.colour = colour

    def draw(self, canvas):
        pass

class rectangle:
    def __init__(self, x, y, width, heigth, colour):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.colour = colour

    def draw(self, canvas):
        pass
