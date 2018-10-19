def drop_first_last(grades):
    first, *middle, last = grades
    print(middle)
    # avg = sum(middle) / len(middle)
    # print(avg)

drop_first_last([65, 76, 98, 54, 21])
drop_first_last([65, 76])
drop_first_last([65, 76, 98, 54, 21, 54, 65, 99, 88, 78])
print()

first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last)
print(names)
print()

for a, b in names:
    print(a, b)