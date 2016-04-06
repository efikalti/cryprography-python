#!/usr/bin/python
import base64

text_message = "Neversendahumantodoamachinesjob"
text_key = "MATRIX"

aDict = dict(zip('abcdefghijklmnopqrstuvwxyz.!?()-ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                              ['00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001',
                              '11010','11011','11100','11101','11110','11111',
                              '00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001']))


# the function below converts a text of the form 'something' to
# a binary string according to our 5-bit encoding
def text_enc(text):
    text = text[::-1]
    length = len(text)
    coded_text = ''
    for i in range(length):
        coded_text = aDict[text[i]] + coded_text
    return coded_text.lower()


# The function below converts a binary string to an alphabetic text
# according to our 5-bit encoding
def text_dec(binary_string):
    length = len(binary_string)
    inv_map = {v: k for k, v in aDict.items()}
    decoded_text = ''
    for i in range(0,length,5):
        decoded_text = inv_map[binary_string[i:i+5]] + decoded_text # + in strings is the join function.
    decoded_text = decoded_text[::-1]
    return decoded_text.lower()


if __name__ == "__main__":
	print "Message:", text_message
	print "Key:", text_key
	# Convert message and key to binary
	message = text_enc(text_message)
	key = text_enc(text_key)
	print "Message in 5-bit binary:", message
	print "Key in 5-bit binary:", key

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
	print "encoded message:", encode(''.join(crypt))
