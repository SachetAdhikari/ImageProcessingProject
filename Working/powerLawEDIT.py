from PIL import Image
import math
from numpy import array
img = Image.open('..\\InputImages\\lena.png')  # A=1 or 2
arr = array(img)
print(arr)
# arr=arr.transpose(2,0,1).reshape(-1,arr.shape[1])
if arr.ndim > 2:
    arr = arr[:, :, 0]
print(arr)
# 1kbcfsdfb72184t82bsdkmb dhsfb
nk = arr
#nk=[[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8, 5,8]];
# for i in range(len(nk)):
# print(*nk[i])
x = max(map(max, nk))
m = len(nk[1])
n = len(nk)
print(m, n)
opnk = nk
print(math.pow(2, 3))
x = 0
#A=int(input("enter constant"));
#B=int(input("enter Gamma"));
# f = open('powerlaw.txt') ####################################
# read=f.readline().split()
# print(read)
for j in range(len(nk)):
    for i in range(len(nk[j])):
        # opnk[j][i]=round(int(read[0])*math.pow(nk[j][i],int(read[1])))
        # 2 and 3 given as input for constant and gamma
        opnk[j][i] = round(int(2)*math.pow(nk[j][i], int(3)))
print(opnk)
print("              ")
# for i in range(len(opnk)):
# print(*opnk[i])
img = Image.fromarray(opnk)
img.save('..\\OutputImages\\resultPowerLaw.png')
