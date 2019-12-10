#Write a Python program to count number of items in a dictionary value that is a list
#(using map)
count =0
l=[1,2,3,4,[5,6,4,4]]
m=list(map(lambda x: int(type(x)==type(list())),l))

for i in m:
    if int(i)==1:
        count=count+1;
print(count)