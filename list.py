a = [12,3,4,5,6,7,8,1,90]

def listcalc(a):
    number = int(input("Enter a number"))
    new_list = []
    for i in a:
        if i>=number:
            new_list.append(i)
    return new_list

updated_list = listcalc(a)
print(updated_list)
print("changes made in local for git")


