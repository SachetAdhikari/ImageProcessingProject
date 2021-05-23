from PIL import Image
from numpy import array
img = Image.open("..\\InputImages\\BeforeNegativeTransformation.png")
arr = array(img)
img.close()
width = len(arr[1])
height = len(arr)
filter = 1/9
for color in range(3):
    for j in range(1, height-1):
        for i in range(1, width-1):
            arr[j][i][color] = round(
                arr[j-1][i-1][color]*filter + arr[j-1][i][color]*filter + arr[j-1][i+1][color]*filter +
                arr[j][i-1][color]*filter + arr[j][i][color]*filter + arr[j][i+1][color]*filter +
                arr[j+1][i-1][color]*filter + arr[j+1][i][color] *
                filter + arr[j+1][i+1][color]*filter
            )
newImg = Image.fromarray(arr)
newImg.save("..\\OutputImages\\resultColorAverage.png")
