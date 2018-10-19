# File I/O

f = open('workfile', 'w+b')
f.write(bytes(2))
f.close()
f = open('workfile', 'r+b')
print(f.read())
f.close()

print()

'''
f = open('workfile.txt', 'w')
f.write("eee")
f.close()
f = open('workfile.txt', 'r')
s = f.readline()
print(s)
print(len(s))
'''

f = open('workfile.txt', 'w')
f.write("eee" + '\n')
f.write("www" + '\n')
f.close()
f = open('workfile.txt', 'r')
# print(list(f))
s = f.readlines()
# s = f.readline()
# s = f.read()
print(s)
print(type(s))
print(len(s))

'''
i = 5
print(i.bit_length())
'''

print('%26s %3d' %("ggg", 3))
print('%-26s %3d' %("ggg", 3))
print()

aString = "12 45.5 abc 9"
strList = aString.split()
print(strList)
