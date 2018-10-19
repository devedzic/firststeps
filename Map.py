income = [10, 20, 34]


def double_income(amount):
    return amount * 2

double_income_values = map(double_income, income)
print(double_income_values)                         # result: <map object at 0x054B86D0>
print(list(double_income_values))                   # result: [20, 40, 68]
