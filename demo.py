import numpy as np
from PIL import Image

data = np.zeros((5, 5, 3), dtype=np.uint8)
data[:] = [155, 250, 120]
data[1:3, 1:3] = [255, 0, 0]
data[1:2, 2:3] = [123, 45, 26]

img = Image.fromarray(data, "RGB")
img.save("canvas.png")