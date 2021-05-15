#from skimage import io
import numpy as np
from PIL import Image
import math
from numpy import array
#img = Image.open('C:\\Users\\praneeth\\Desktop\\histeq_numpy1.jpg')
img = Image.open('C:\\Users\\sache\\Desktop\\Python\\IP Project\\Images\\lena.png')
arr = array(img)
print(arr)
#arr=arr.transpose(2,0,1).reshape(-1,arr.shape[1])
if arr.ndim>2:
    arr=arr[:,:,0]
    nk=arr;
nk=[[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8]];
x=max(map(max, nk));
print(x);
scale=0;
if(255>=x>127):
    scale=255;
elif(127>=x>63):
    scale=127;
elif(63>=x>31):
    scale=63;
elif(31>=x>15):
    scale=31;
elif(15>=x>7):
    scale=15;
elif(7>=x>3):
    scale=7;
else:
    scale=3;
print(scale);
#for i in range(len(nk)):
# print(*nk[i])
m=len(nk[1]);
n=len(nk);
print(m,n);
opnk=nk; x=0;
for j in range(len(nk)):
    for i in range(len(nk[j])):
        opnk[j][i]=scale-nk[j][i];
print(opnk)
print("           ")
#for i in range(len(opnk)):
# print(*opnk[i])
img = Image.fromarray(opnk)
img.save('C:\\Users\\sache\\Desktop\\Python\\IP Project\\Images\\resultNegative.png')