from PIL import Image
from numpy import array
img = Image.open("..\\InputImages\\Average.jpg")
# img = Image.open("..\\OutputImages\\resultThresholding.png")
img.show()
arr = array(img)
img.close()
if arr.ndim > 2:
    arr = arr[:, :, 0]
width = len(arr[1])
height = len(arr)
filter = 1/9
for j in range(1, height-1):
    for i in range(1, width-1):
        arr[j][i] = round(
            arr[j-1][i-1]*filter + arr[j-1][i]*filter + arr[j-1][i+1]*filter +
            arr[j][i-1]*filter + arr[j][i]*filter + arr[j][i+1]*filter +
            arr[j+1][i-1]*filter + arr[j+1][i]*filter + arr[j+1][i+1]*filter
        )
newImg = Image.fromarray(arr)
newImg.save("..\\OutputImages\\resultAverage.png")
newImg.show()
