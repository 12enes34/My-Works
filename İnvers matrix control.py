from copy import copy
import numpy as np
x=int(input("matrix size:"))
list=[]
s=0
z=0
for i in range(x*x):
    
    list.append(int(input(f"{z}th line {s}th column")))
    s+=1
    if s==x:
        s=0
        z+=1
a=np.array(list)
c=a.reshape(x,x)
v=copy(c)

for i in range(x):
    for j in range(x):
        v[j][i]=c[i][j]

num=0
for i in range(x):
    for j in range(x):
        if c[i][j]==v[i][j]:
            num+=1
    
if num==x*x:
    print("is symmetrical")
else:
    print("is not symmetrical")

for i in range(x):
    for j in range(x):
        print(c[i][j],end=" ")
    print()