#Print -ve if no is =-ve and cube if not

def task1():
    
    n= int(input("How many \n"))
    arr=[]
    for i in range(0,n):
        arr.append(input())
        
   
    for i in range(0,n) :
        if int(arr[i]) > 0:
            print(int(arr[i])*int(arr[i])*int(arr[i]))
            
        else:
            print(" -ve ")
            
