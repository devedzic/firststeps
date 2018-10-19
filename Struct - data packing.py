from struct import *

print(calcsize('i'))        # calculate the size of an int (in bytes)
print(calcsize('f'))        # calculate the size of a float (in bytes)
print(calcsize('iif'))      # calculate the size of 2 ints and 1 float (in bytes)

packed_data = pack('iif', 2, 3, 4.5)    # pack 2 ints and 1 float
print(packed_data)                      # result: b'\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x90@'
print(unpack('iif', packed_data))       # unpack 2 ints and 1 float
