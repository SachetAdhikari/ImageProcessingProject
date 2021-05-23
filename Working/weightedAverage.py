from PIL import Image
from numpy import array
img = Image.open("..\\InputImages\\lena.png")
arr = array(img)
img.close()
if arr.ndim > 2:
    arr = arr[:, :, 0]
width = len(arr[1])
height = len(arr)
filter = [1/16, 2/16, 1/16, 2/16, 4/16, 2/16, 1/16, 2/16, 1/16]
for j in range(1, height-1):
    for i in range(1, width-1):
        arr[j][i] = round(
            arr[j-1][i-1]*filter[0] + arr[j-1][i]*filter[1] + arr[j-1][i+1]*filter[2] +
            arr[j][i-1]*filter[3] + arr[j][i]*filter[4] + arr[j][i+1]*filter[5] +
            arr[j+1][i-1]*filter[6] + arr[j+1][i] *
            filter[7] + arr[j+1][i+1]*filter[8]
        )
newImg = Image.fromarray(arr)
newImg.save("..\\OutputImages\\resultWeightedAverage.png")
