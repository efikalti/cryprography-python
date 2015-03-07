#!/usr/bin/python
from Crypto.Cipher import ARC4

crypto = ARC4.new("MATRIX")
message = 'Never send a human to do a machine s job'
crypto_message = crypto.encrypt(message)
print crypto_message