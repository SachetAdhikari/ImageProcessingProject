from statistics import median
from PIL import Image
from numpy import array
# img = Image.open("..\\InputImages\\Median.png")
img = Image.open("..\\OutputImages\\resultThresholding.png")
img.show()
arr = array(img)
img.close()
if arr.ndim > 2:
    arr = arr[:, :, 0]
width = len(arr[1])
height = len(arr)
for j in range(1, height-1):
    for i in range(1, width-1):
        data = [arr[j-1][i-1], arr[j-1][i], arr[j-1][i+1],
                arr[j][i-1], arr[j][i], arr[j][i+1],
                arr[j+1][i-1], arr[j+1][i], arr[j+1][i+1]]
        arr[j][i] = median(data)
newImg = Image.fromarray(arr)
# newImg.save("..\\OutputImages\\resultMedian.png")
newImg.show()
