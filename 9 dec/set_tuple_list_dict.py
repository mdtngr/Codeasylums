#set
y={1,2,3,4,1}
x={2,4}
print((y-x))

s=set([1,2,3,4])
frs=frozenset([1,2,3])
s.add(5)
print(s)

#tuple
p=(1,2)
print(p[-1])

#list
lt=[1,2,3,'k']
for i in lt:
    print(i)
    
#Dictionary

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
print(dict.keys())
print(dict.values())
print(dict.items())

for (i,j) in dict.items():
    print(i," ",j)
dict.pop('Age')

for (i,j) in dict.items():
    print(i," ",j)

