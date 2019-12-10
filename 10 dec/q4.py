#Write a Python program to print all unique values in a dictionary.

n=int(input("Enter the number of elements "))
s=set()
d=dict()

while n!=0:
    n=n-1
    key=input("Enter key ")
    val=input("Enter val ")
    d[key]=val   
    
s =set(list(filter(lambda x: (x) , d.values())))

for i in s:
    print(i)