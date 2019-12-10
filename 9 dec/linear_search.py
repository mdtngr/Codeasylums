def linearsearch():
        
    n=int(input("Enter size of list "))
    if n==0:
        print("enter a valid size")
        return
    l=[];
    while(n):
        n=n-1
        l.append(input("Enter value "))
        
    print(l)
    
    num=int(input("Enter number to be searched "))
    for i in l:
        if int(i) == num:
            print("Number found ")
            found=1
            break
        else:
            found=0
    if found == 0:
        print("Not found")
    
linearsearch()