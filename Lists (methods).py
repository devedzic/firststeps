'''
listA = [0, 1, 2, 3]
listA.extend([4, 5, 6])
print(listA)
listB = listA
listB = listA.extend([4, 5, 6])
print(listB)
'''

'''
values = [0, 1, 2, 3, 4]
values.insert(1, 8)
print(values)
'''

theList = [10, 11, 12, 13]
print(theList)
theList.remove(11)
print(theList)
print()

x = theList.pop(1)
print("list =", theList)
print("x =", x)
print()

listA = [1, 2, 3]
listB = [8, 9]
listC = listA + listB
print(listC)
print()

