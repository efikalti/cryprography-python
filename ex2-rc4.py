#!/usr/bin/python
import base64

message = "Never send a human to do a machine's job"
key = "MATRIX"

#KSA Phase
S = range(256)
j = 0
keylength = len(key)
for i in range(256):
	k = i % keylength
	j = (j + S[i] + ord(key[k])) % 256
	#swap
	S[i] , S[j] = S[j] , S[i]

#PRGA Phase
i = 0
j = 0
crypt = list()
for c in message:
	i = ( i + 1 ) % 256
	j = ( j + S[i] ) % 256
	S[i] , S[j] = S[j] , S[i]
	crypt.append(chr(ord(c) ^ S[(S[i] + S[j]) % 256]))
encode = base64.b64encode
print encode(''.join(crypt))