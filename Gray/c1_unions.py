from ctypes import *

class barley_amount(Union):
    _fields_ = [
        ("barley_long", c_long),
        ("barley_int", c_int),
        ("barley_char", c_char * 8),
    ]

val = input("enter amount")
my = barley_amount(int(val))

print ("amount as long: %ld" % my.barley_long)
print ("amount as int: %d" % my.barley_int)
print ("amount as char: %s" % my.barley_char)
