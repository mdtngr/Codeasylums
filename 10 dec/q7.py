#Write a Python program to replace dictionary values with their average.
from functools import reduce
d={'a':1,'b':2,'c':5}
a=int(reduce(lambda x,y:int(x)+int(y),d.values()))
num=list(map(lambda x:1,d.values()))
no=int(reduce(lambda x,y:x+y,num))
a=a/no

for i in d.keys():
    d[i]=a
    
print(d)
    