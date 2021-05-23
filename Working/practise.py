from PIL import Image
from numpy import array
img = Image.open('..\\InputImages\\lena.png')
arr = array(img)
if arr.ndim > 2:
    arr = arr[:, :, 0]
nk = arr
x = max(map(max, nk))
m = len(nk[1])
n = len(nk)
print(m, n)
print(x)
# print(nk[1])
