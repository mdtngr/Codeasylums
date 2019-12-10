a=int(input())

while a!=0:
	a=a-1
	n=int(input())
	n=int(((3*n*n)+n)/2)
	n=n%1000007
	print(n)
