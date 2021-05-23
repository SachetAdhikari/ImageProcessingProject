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
for j in range(height-2):
    for i in range(width-2):
        arr[j][i] = round(
            arr[j][i]*filter + arr[j][i+1]*filter + arr[j][i+2]*filter +
            arr[j+1][i]*filter + arr[j+1][i+1]*filter + arr[j+1][i+2]*filter +
            arr[j+2][i]*filter + arr[j+2][i+1]*filter + arr[j+2][i+2]*filter
        )
newImg = Image.fromarray(arr)
newImg.save("..\\OutputImages\\resultAverage.png")
