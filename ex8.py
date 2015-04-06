#!/usr/bin/python

import crypt

encrypted = "$6$ANrWqWm8$ALDlgQkIyB3/I7Zcqohd2t147EBHagFE2.GHFy.zP5eAHxHbujjnCMLJvrWFqMo6LZ5g5.5eMu61tebZ/djLM."
salt = "$6$ANrWqWm8$"
S = range(10)

for i in S:
	for j in S:
		for k in S:
			for l in S:
				for m in S:
					for n in S:
						password ='' + str(i) + str(j) + str(k) + str(l) + str(m) + str(n)
						en = crypt.crypt(password, salt)
						if en in encrypted:
							print "password: ",password
							break
    				else:
        				continue
    				break
    			else:
    				continue
    			break
    		else:
    			continue
    		break
    	else:
    		continue
    	break
print password