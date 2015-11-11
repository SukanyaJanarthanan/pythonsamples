class person(object):
   def __init__(self,name,age):
       self.name = name
       self.age = age

   def __repr__(self):
        return "<name: %s, age: %s>" % (self.name, self.age)


def sort_byname(person):
    return person.age

jack = person('Jack', 19)
adam = person('Adam', 43)
becky = person('Becky', 89)
people = [jack, adam, becky]
print(jack)
print(sorted(people, key=sort_byname))

list = [5,4,7,7,7,65,56,43,2,76,98,3]
newlist = []
minimum = list[0]
for i in list:
    if i<minimum:
        minimum = i
    newlist.append(minimum)

print(newlist)

