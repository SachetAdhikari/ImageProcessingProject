#from skimage import io
#from scikitimage import io
import numpy as np
from PIL import Image
from numpy import array
#img = Image.open('C:\\Users\\praneeth\\Desktop\\histeq_numpy1.jpg')
img = Image.open(
    'C:\\Users\\sache\\Desktop\\Python\\IP Project\\Images\\lena.png')
arr = array(img)
print(arr)
# arr=arr.transpose(2,0,1).reshape(-1,arr.shape[1])
if arr.ndim > 2:
    arr = arr[:, :, 0]
# 1kbcfsdfb72184t82bsdkmb dhsfb
ipnk = arr
x = max(map(max, ipnk))
print(x)
# x=255;
scale = 0
if(255 >= x > 127):
    scale = 255
elif(127 >= x > 63):
    scale = 127
elif(63 >= x > 31):
    scale = 63
elif(31 >= x > 15):
    scale = 31
elif(15 >= x > 7):
    scale = 15
elif(7 >= x > 3):
    scale = 7
else:
    scale = 3
print(scale)


def frequency(a, x):
    count = 0
    for j in a:
        for i in j:
            if i == x:
                count += 1
                return count


#x = 5;
#print(frequency(ipnk, x));
nk = [0]*(scale+1)
print(len(nk))
x = 0
# for a in range(1,n+1):
for a in range(0, scale):
    nk[x] = frequency(ipnk, a)
    x = x+1
print(nk)  # lnk=input("enter length")
# lnk=int(lnk);
# rs=[0]*lnk;
rs = [0]*len(nk)
rstot = [0]*len(nk)
rsmax = [0]*len(nk)
rsround = [0]*len(nk)
opnk = [0]*len(nk)
# running sum
tot = 0
i = 0
for x in nk:
    tot = tot+x
    rs[i] = tot
    i = i+1
# rs/total rs/total * max round
i = 0
for x in nk:
    rstot[i] = rs[i]/tot
    rsmax[i] = rstot[i]*(len(rs)-1)
    rsround[i] = round(rsmax[i])
    i = i+1
print("input")
print(nk)
print("running sum")
print(rs)
print("running sum/ tot")
print(rstot)
print("1111111111111111111111111111111111111111")
print("running sum rounding")
print(rsround)
# print(opnk);#output histogram
i = 0
for x in nk:
    opnk[rsround[i]] += nk[i]
    i = i+1
print("output")
print(opnk)
#n = 5
#m = 5
#opnkar = [[0] * m] * n
# for j in ipnk:
# for i in j:
# opnkar[j[i]]=rsround[i];
opnkar = ipnk
for j in range(len(ipnk)):
    for i in range(len(ipnk[j])):
        opnkar[j][i] = rsround[ipnk[j][i]]
print(opnkar)
# for i in range(len(opnkar)):
# print(*opnkar[i])
img = Image.fromarray(opnkar)
img.save('C:\\Users\\sache\\Desktop\\Python\\IP Project\\Images\\resultHistogram.png')
"""
image = io.imread('C:\\Users\\praneeth\\Desktop\\dip images\\test.png')
print(type(image))
print(image.tolist())
#plt.imshow(image); """
