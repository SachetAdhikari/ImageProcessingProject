import math
from PIL import Image
from numpy import array

img = Image.open('..\\InputImages\\lena.png')
arr = array(img)
print(arr)
# arr=arr.transpose(2,0,1).reshape(-1,arr.shape[1])
if arr.ndim > 2:
    arr = arr[:, :, 0]
print(arr)
# 1kbcfsdfb72184t82bsdkmb dhsfbnk=arr;#nk=[[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8, 5,8]];
# for i in range(len(nk)):
# print(*nk[i])
x = max(map(max, nk))
m = len(nk[1])
n = len(nk)
print(m, n)
opnk = nk
x = 0
#A=int(input("enter constaant"));
# f = open('log.txt')
# read = f.readline().split() print(read)
for j in range(len(nk)):
    for i in range(len(nk[j])):
        # opnk[j][i] = round(int(read[0])*math.log10(1+nk[j][i]))
        opnk[j][i] = round(int(2)*math.log10(1+nk[j][i]))
print(opnk)
print(" ")
# for i in range(len(opnk)):
# print(*opnk[i])
img = Image.fromarray(opnk)
img.save('..\\OutputImages\\resultLogarithmic.png')
