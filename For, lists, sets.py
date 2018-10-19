'''
Multi-line comment
'''

'''
for i in range(10):
    if i is 5:
        continue
    print(i)
'''

for i in range(10):
    if (i % 4) is 0:
        continue
    print(i)

groceries = {'a', 'b', 'a'}
print(groceries)
print(['a', 'b', 'a'])
print({'a', 'b', 'a'})

classmates = {'Tony': ' cool but smells', 'Emma': ' sits behind me', 'Lucy': ' asks too many questions'}

for k, v in classmates.items():
    print(k + v)

