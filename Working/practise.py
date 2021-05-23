from PIL import Image
from numpy import array
img = Image.open("..\\InputImages\\BeforeNegativeTransformation.png")
arr = array(img)
img.close()
if arr.ndim > 2:
    # taking value from 0th index of 3rd dimension i.e r value in case of rgb and take values from other dimensions(1st and 2nd) as it is
    arr1 = arr[:, :, 0]
Image.fromarray(arr1).show()

width = len(arr[1])
height = len(arr)

# converting to grayscale
for j in range(height):
    for i in range(width):
        r, g, b = arr[j][i][0], arr[j][i][1], arr[j][i][2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        arr[j][i] = [gray, gray, gray, 255]
Image.fromarray(arr).show()
