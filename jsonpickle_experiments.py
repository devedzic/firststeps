from datetime import date

import jsonpickle


class A():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return 'a: ' + str(self.a) + ', b: ' + str(self.b) + ', c: ' + str(self.c)

    def __eq__(self, other):
        return True if isinstance(other, A) and self.a == other.a and self.b == other.b and self.c == other.c else False


class B():
    def __init__(self, aA, bB, dD):
        self.aA = aA
        self.bB = bB
        self.dD = dD

    def __str__(self):
        return 'aA: {}\nbB: {}\ndD: {}'.format(self.aA, self.bB, self.dD)

    def __eq__(self, other):
        if not isinstance(other, B):
            return False
        return self.aA == other.aA and self. bB == other.bB and self.dD == other.dD


a = A(1, 2, 3)
b = B(a, 22, date(1978, 3, 2))
b_json = jsonpickle.encode(b)
b_py = jsonpickle.decode(b_json)
print(b)
print(b_py)
print(b == b_py)
print()

a1 = A(11, 22, 32)
b1 = B(a1, 222, date(1946, 12, 30))
b1_json = jsonpickle.encode(b1)
b1_py = jsonpickle.decode(b1_json)
print(b1)
print(b1_py)
print(b1 == b1_py)


