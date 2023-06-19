#!/usr/bin/python3

from subprocess import call
from sys import argv

user_string = ' '.join(argv[1:])[:14]
hex_string = ' '.join([hex(ord(z)) for z in user_string])

call('/usr/bin/ipmitool raw 0x6 0x58 0xC2 0 0 0 0 0 0 0 0 0 0 0 0', shell=True)
call('/usr/bin/ipmitool raw 0x6 0x58 0xC1 0 0 {0} {1}'.format(str(len(user_string)), hex_string), shell=True)
