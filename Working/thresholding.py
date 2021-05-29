from PIL import Image
from numpy import array
img = Image.open("..\\InputImages\\Thresholding.jpg")
img.show()
arr = array(img)
img.close()
if arr.ndim > 2:
    arr = arr[:, :, 0]
width = len(arr[1])
height = len(arr)
thresholdValue = 120
for j in range(height):
    for i in range(width):
        if(arr[j][i] > thresholdValue):
            arr[j][i] = 255
        else:
            arr[j][i] = 0
newImg = Image.fromarray(arr)
newImg.save("..\\OutputImages\\resultThresholding.png")
newImg.show()
