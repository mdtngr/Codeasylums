#print the following pattern

#12345
# 2345
#  345
#   45
#    5

def design():
    n = int(input())
    
    for i in range(1,n):
        for z in range(1,n):
            if z<i:
                print(" ",end='')
            else:
                print(z,end='')
        print()
        
design()
        
        
    