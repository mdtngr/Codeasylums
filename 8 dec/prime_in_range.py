
#Prime numbers in a given range
import math
def task2():
    
    x= int(input("Enter a number "))
    t=0
    for i in range (2,x) :
        for y in range (2,i) :
            if i % y == 0:
                t=1
        
        if t==0:
            print(i)
        else:
            t=0
        

task2()

