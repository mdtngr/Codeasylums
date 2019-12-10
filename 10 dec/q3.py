#Write a Python script to print a dictionary where the keys are numbers between 1 and 15
#(both included) and the values are square of keys

d={}

n=int(input("Input the number of key value pairs "))
while n!=0:
    n=n-1
    key=int(input("Enter Key "))
    val=int(input("Enter val "))
    d[key]=val

fl2 = list(map(lambda x: (x*x), d.keys()))


for i in fl2:
    print(d[i])



