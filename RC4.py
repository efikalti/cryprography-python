#!/usr/bin/env python

import binascii

message = "fasten your seat belt Dorothy, cause Kansas is going bye-bye"
binary = bin(int(binascii.hexlify(message), 16))


