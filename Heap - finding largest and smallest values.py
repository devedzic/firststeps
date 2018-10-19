import heapq


grades = [12, 34, 67, 234, 222, 456, 1123, 55]
print(heapq.nlargest(3, grades))                # find 3 largest items in grades
print(heapq.nsmallest(2, grades))               # find 2 smallest items in grades


stocks = [                                      # find 2 smallest items in a dictionary using the key parameter
    {'ticker': 'GOOG', 'price': 520.23},
    {'ticker': 'FB', 'price': 76.45},
    {'ticker': 'AAPL', 'price': 99.78}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))
