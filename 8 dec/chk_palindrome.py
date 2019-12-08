#Check palindrome
def func():
    n= int(input("enter val "))
    
    temp=n
    num=0
    while(temp!=0):
        num=num*10+(temp%10)
        temp=int(temp/10)
    
    print("NUMBER ")    
    print(num)

        
    if num == n :
        print("Yes")
    else:
        print("no")
        
func()        

