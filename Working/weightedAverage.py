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
for j in range(height-2):
    for i in range(width-2):
        arr[j][i] = round(
            arr[j][i]*filter[0] + arr[j][i+1]*filter[1] + arr[j][i+2]*filter[2] +
            arr[j+1][i]*filter[3] + arr[j+1][i+1]*filter[4] + arr[j+1][i+2]*filter[5] +
            arr[j+2][i]*filter[6] + arr[j+2][i+1] *
            filter[7] + arr[j+2][i+2]*filter[8]
        )
newImg = Image.fromarray(arr)
newImg.save("..\\OutputImages\\resultWeightedAverage.png")
