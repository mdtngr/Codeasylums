#Print list in some pattern lis=[1,2,3,[4,5,6]]
#1
#2
#3
# 4
# 5
# 6

def nestedlist(l,n):
    for i in l:
        if type(i)==type(0):
            print(n,end="")
            print(i)
        else:
            nestedlist(i,n+" ")
            
lis=[1,2,3,4,5,[6,7,8],9,10]
nestedlist(lis,"")

