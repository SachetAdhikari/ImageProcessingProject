from math import log10, pow
from PIL import Image
from numpy import array
img = Image.open("..\\InputImages\\PowerLaw.png")
# img.show()
arr = array(img)
img.close()
if arr.ndim > 2:
    arr = arr[:, :, 0]
Image.fromarray(arr).show()
width = len(arr[1])
height = len(arr)
filter = 1/9
for j in range(height):
    for i in range(width):
        # constant and gamma values are is 2 and 3
        arr[j][i] = round(
            int(2)*pow(arr[j][i], int(1.5))
        )
newImg = Image.fromarray(arr)
# newImg.save("..\\OutputImages\\resultPowerLaw.png")
newImg.show()
