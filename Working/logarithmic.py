from math import log10
from PIL import Image
from numpy import array
img = Image.open("..\\InputImages\\lena.png")
arr = array(img)
img.close()
if arr.ndim > 2:
    arr = arr[:, :, 0]
width = len(arr[1])
height = len(arr)
filter = 1/9
for j in range(height):
    for i in range(width):
        # constant is 2
        arr[j][i] = round(
            int(0.5)*log10(1+arr[j][i])
        )
newImg = Image.fromarray(arr)
newImg.save("..\\OutputImages\\resultLogarithmic2.png")
