#Write a Python program to count the number of strings where the string length is 2 or
#more and the first and last character are same from a given list of strings.

n=int(input())
l=[]

while n!=0:
    n=n-1
    s=input()
    l.append(s)
    
print("\n \n")    
fl = list(filter(lambda x: (len(x)>= 2) , l)) 
fl2 = list(filter(lambda x: (x[0]==x[-1]) , fl)) 
print(len(fl2))
    


