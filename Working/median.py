from PIL import Image
import statistics
from numpy import array
img = Image.open('..\\InputImages\\lena.png')
arr = array(img)
print(arr)
# arr=arr.transpose(2,0,1).reshape(-1,arr.shape[1])
if arr.ndim > 2:
    arr = arr[:, :, 0]
print(arr)
# 1kbcfsdfb72184t82bsdkmb dhsfb
nk = arr
# for i in range(len(nk)):
# print(*nk[i])
x = max(map(max, nk))
m = len(nk[1])
n = len(nk)
print(m, n)
opnk = nk
x = 0
filter = [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, ]
for j in range(1, len(nk)-1):
    for i in range(1, len(nk[j])-1):
        data1 = [nk[j-1][i-1], nk[j-1][i], nk[j-1][i+1], nk[j][i - 1],
                 nk[j][i], nk[j][i+1], nk[j+1][i-1], nk[j+1][i], nk[j+1][i+1]]
        opnk[j][i] = round(statistics.median(data1))
print(opnk)
print("        ")
# for i in range(len(opnk)):
# print(*opnk[i])
img = Image.fromarray(opnk)
img.save('..\\OutputImages\\resultMedian.png')
