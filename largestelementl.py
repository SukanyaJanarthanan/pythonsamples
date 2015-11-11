a = [3,5,6,7,8]

largest = a[0]
second_largest = a[0]
'''def largest_element(a,largest):
    for i in a:
        if i> largest:
           largest = i
    print (largest)'''

def second_largest_nmber(a,largest,second_largest):

    for i in a:
        if i>second_largest:
           second_largest = i
        if i>largest:
           tem = second_largest
           second_largest = largest
           largest = tem
    print(largest,second_largest)

#largest_element(a,largest)
second_largest_nmber(a,largest,second_largest)
maximum = max(a)
print(maximum)
a.remove(maximum)
print (max(a))
print(a)