stocks = {
	'GOOG': 520.23,
	'FB': 76.45,
	'AAPL': 99.78,
    'AMZN': 123.23
}

print(min(stocks))      # result: 'AAPL' (by default, min is calculated on keys, not on values)
min_price = min(zip(stocks.values(), stocks.keys()))    # zip the list of values first, and the list of keys second
print(min_price)        # result: (76.45, 'FB')
print()


from operator import itemgetter

band_members = [
    {'fname': 'John', 'lname': 'Lennon'},
    {'fname': 'Paul', 'lname': 'McCartney'},
    {'fname': 'George', 'lname': 'Harrison'},
    {'fname': 'Ringo', 'lname': 'Starr'},
    {'fname': 'Ringo', 'lname': 'Starkey'}
]

for x in sorted(band_members, key=itemgetter('fname')):          # check out the result for 2 Ringos - not exactly right
    print(x)
print('------')
for x in sorted(band_members, key=itemgetter('fname', 'lname')): # check out the result for 2 Ringos now
    print(x)
print()


from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + ": " + str(self.user_id)

users = [
    User('John', 1),
    User('Paul', 2),
    User('George', 6),
    User('George', 3),
    User('Ringo', 4)
]

for user in users:      # result: users printed in the order specified in the list
    print(user)
print('-----')
for user in sorted(users, key=attrgetter('name')):            # result: users printed sorted by name
    print(user)
print('-----')
for user in sorted(users, key=attrgetter('name', 'user_id')): # result: users printed sorted by name and then by user_id
    print(user)

