from PIL import Image
import math
from numpy import array
img = Image.open('C:\\Users\\sache\\Desktop\\Python\\IP Project\\Images\\lena.png')
arr = array(img)
print(arr)
#arr=arr.transpose(2,0,1).reshape(-1,arr.shape[1])
if arr.ndim>2:
    arr=arr[:,:,0]
print(arr)
#1kbcfsdfb72184t82bsdkmb dhsfb
nk=arr;
#nk=[[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8,5,8],[8,5,8,8, 5,8]];
#for i in range(len(nk)):
# print(*nk[i])
x=max(map(max, nk));
m=len(nk[1]);
n=len(nk);
print(m,n);
opnk=nk;
x=0;
#A=int(input("enter constaant"));
f = open('thresh.txt')
read=f.readline().split() 
print(read)
A=int(read[0]);
for j in range(len(nk)):
    for i in range(len(nk[j])):
        if(nk[j][i]>A):
            opnk[j][i]=255;
        else:
            opnk[j][i]=0
print(opnk)
print("      ")
#for i in range(len(opnk)):
# print(*opnk[i])
img = Image.fromarray(opnk)
img.save('C:\\Users\\sache\\Desktop\\Python\\IP Project\\Images\\resultThresholding.png')