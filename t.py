# """Testing @property"""
#
# class B:
#     def __init__(self, x, y):
#         self.__x = x
#         self.y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         self.__x = value
#
#
# b = B(1, 2)
# print(b.x)

# """Testing date.isoformat()"""
#
# from datetime import date
# print(date.fromisoformat("1978-03-02"))

"""Getting project root directory"""

import os
print(__file__)
print(os.path.abspath(os.path.dirname(__file__)))

