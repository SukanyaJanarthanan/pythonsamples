import os
def multiply(a,b):
    return a*b

list = map(multiply,[1,2,3],[2,3,4])
for i in list:
    print (i)

list1=map(lambda x,y: x*y, [1,25,4],[2,3,1])
for i in list1:
    print(i)


integers = [x for x in range(11)]
print(integers)
mapv = map(lambda x: x*2,integers)
for x in mapv:
    print(x ,end=' ')
print('\n')

filterv = filter(lambda x: x%2==0,integers)
for j in filterv:
    print(j, end = ' ')

print(os.listdir('C:\\Python34\\lib'))