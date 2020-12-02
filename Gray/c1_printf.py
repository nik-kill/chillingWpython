from ctypes import *

msvcrt = cdll.msvcrt
message_string = "Hey SUpp!\n"
msvcrt.printf("Testing: %s", message_string)

# for linux
# libc = CDLL("libc.so.6")
# message_string = "Heyy SUpp!\n"
# libc.printf("Testing: %s",message_string)
