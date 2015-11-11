'''mylist = [x*x for x in range(3)]
print(mylist)'''


mygenerator =(x*x for x in range(3))

for i in mygenerator:
    print(i)


for x in mygenerator:
    print(x)