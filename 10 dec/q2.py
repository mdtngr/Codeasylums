#Add two lists using map and lambda
l1=[1,2,3,4,5,6]
l2=[6,5,4,3,2,1]

ans=list(map(lambda x,y :(x+y),l1,l2))
print(ans)