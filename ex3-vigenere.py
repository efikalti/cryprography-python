#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

listA = {u'Α': 1, u'Β': 2, u'Γ': 3, u'Δ': 4, u'Ε': 5, u'Ζ': 6, u'Η': 7, u'Θ': 8, u'Ι': 9, u'Κ': 10, u'Λ': 11, u'Μ': 12, u'Ν': 13, u'Ξ': 14, u'Ο': 15, u'Π': 16, u'Ρ': 17, u'Σ': 18, u'Τ': 19, u'Υ': 20, u'Φ': 21, u'Χ': 22, u'Ψ': 23, u'Ω': 0}
listB = {1: u'Α', 2: u'Β', 3: u'Γ', 4: u'Δ', 5: u'Ε', 6: u'Ζ', 7: u'Η', 8: u'Θ', 9: u'Ι', 10: u'Κ', 11: u'Λ', 12: u'Μ', 13: u'Ν', 14: u'Ξ', 15: u'Ο', 16: u'Π', 17: u'Ρ', 18: u'Σ', 19: u'Τ', 20: u'Υ', 21: u'Φ', 22: u'Χ', 23: u'Ψ', 0: u'Ω'}
gr_freq = {u'Α': 11.58, u'Β': 0.55, u'Γ': 1.72, u'Δ': 1.64, u'Ε': 8.23, u'Ζ': 0.27, u'Η': 5.01, u'Θ': 1.11, u'Ι': 9.52, u'Κ': 4.18, u'Λ': 2.78, u'Μ': 3.51, u'Ν': 6.18, u'Ξ': 0.35, u'Ο': 10.15, u'Π': 4.01, u'Ρ': 4.03, u'Σ': 7.63, u'Τ': 7.71, u'Υ': 4.22, u'Φ': 0.88, u'Χ': 0.46, u'Ψ': 0.16, u'Ω': 2.11}
gr_IC=0.069

def printf(format, *args):
	sys.stdout.write(format % args) 

def IC(message, k):
	sum = 0
	for i in range(24):
		letter = listB[i]
		appearences = 0
		for j in range(k):
			if (message[j] == letter):
				appearences = appearences + 1
		sum = sum  + ((appearences * (appearences-1))/float(k*(k-1)))
	return sum

def freqDiff(frequencies):
	total = 0
	for letter,value in frequencies.iteritems():
		total = total + value
	percent_freq = {}
	for letter in listA:
		percent_freq[letter] = 0
	for letter in percent_freq:
		percent_freq[letter] = (frequencies[letter]*100) / float(total)
	return percent_freq

def decryptMessage(message, key):
	decrypt = u''
	j = 0
	for i in range(len(message)):
		m = message[i]
		k = key[j]
		decrypt_num = (listA[m] - listA[k]) % 24
		decrypt = decrypt + listB[decrypt_num]
		j = j + 1
		if j == len(key):
			j = 0
	return decrypt

def main():
	message = u"ΕΝΠΠΧΙΦΤΔΛΠΞΝΑΒΧΛΟΨΙΟΓΖΩΠΖΓΓΔΚΑΚΑΑΝΜΦΕΔΟΡΑΤΒΔΩΥΟΩΙΝΥΗΑΠΡΜΩΔΥΨΠΡΕΡΟΛΕΝΑΤΤΑΙΤΤΡΡΡΟΛΕΝΑΤΓΑΚΛΣΗΑΛΩΑΛΦΡΗΣΝΨΛΟΥΨΔΑΔΛΚΓΑΑΗΙΚΨΨΙΜΟΔΥΨΖΖΘΑΔΧΩΓΛΘΥΙΛΝΞΛΣΙΖΖΒΚΛΒΣΚΤΙΑΙΝΣΓΛΔΕΙΝΣΒΟΔΧΙΝΣΖΦΨΦΨΙΙΨΖΥΓΞΕΕΚΡΦΝΕΔΗΒΟΛΟΞΩΑΛΕΟΡΓΖΑΩΡΕΘΜΩΤΟΨΙΑΒΚΩΗΚΦΑΤΨΟΛΧΝΩΨΜΗΔΟΔΗΞΟΙΠΕΘΑΤΔΛΟΨΣΝΓΘΧΩΧΝΗΑΦΥΙΕΔΚΓΣΤΖΖΒΠΨΖΘΥΦΨΘΖΧΟΛΕΝΑΤΕΙΙΑΔΩΨΘΥΚΟΦΝΚΧΡΩΗΑΓΗΘΥΓΟΒΗΙΖΚΖΔΥΓΤΝΤΖΨΔΔΤΚΧΥΤΖΜΛΘΣΣΤΙΗΙΖΚΠΣΝΑΤΩΚΠΦΟΟΑΧΙΔΛΡΔΕΘΥΙΤΙΧΤΒΜΗΑΑΡΓΖΑΗΛΑΡΠΧΙΣΤΙΓΕΘΥΙΡΞΜΑΕΠΖΓΝΦΗΣΕΩΨΙΦΨΔΕΛΣΝΕΑΓΑΩΚΑΝΓΣΑΒΦΙΚΤΛΑΓΟΙΘΝΘΤΖΧΨΑΙΙΑΚΤΟΔΕΧΟΔΟΧΦΤΦΗΒΡΓΤΛΒΑΙΟΓΦΜΠΥΝΟΒΗΣΖΑΔΣΑΜΚΡΝΠΨΔΛΣΛΕΚΑΔΖΟΚΑΣΧΨΘΜΜΟΛΧΡΖΙΝΣΓΛΒΧΤΜΑΤΤΣΝΜΧΣΚΡΜΘΜΜΥΝΤΙΧΤΒΣΚΡΒΙΤΥΗΖΓΡΖΤΕΕΚΡΦΗΤΟΥΚΡΓΝΤΔΛΠΥΤΡΓΛΤΧΥΙΩΨΛΤΖΨΝΝΞΜΟΓΛΒΤΨΓΒΩΑΥΤΠΣΝΩΔΟΔΛΘΣΜΟΑΡΓΣΦΨΑΦΦΤΣΛΒΛΥΝΜΧΧΥΤΙΙΑΛΕΩΔΝΡΗΦΕΩΛΟΡΚΒΣΚΡΥΤΖΣΣΥΥΙΑΨΓΥΔΤΣΓΞΛΗΥΖΕΘΓΣΜΠΔΒΧΕΩΡΖΖΒΧΤΒΑΕΟΒΗΙΝΣΙΥΝΙΝΘΜΠΔΓΡΚΘΛΛΥΙΦΤΒΣΨΛΦΓΖΣΣΚΟΝΨΤΟΙΙΕΙΔΨΚΙΙΔΨΗΨΚΟΑΛΡΝΚΘΤΩΔΥΤΠΣΝΥΔΖΕΨΒΑΦΑΥΝΜΜΕΚΡΦΝΗΑΡΟΒΡΝΚΒΟΗΑΤΘΤΙΟΚΡΦΡΚΒΔΥΩΡΓΝΩΤΠΘΑΡΓΣΖΖΧΙΖΝΧΤΧΨΣΝΕΘΣΛΨΟΧΤΒΤΧΨΝΘΦΧΝΥΤΙΚΣΚΙΙΛΔΗΨΛΤΩΔΙΕΨΜΕΙΡΚΦΤΑΑΑΖΑΦΤΚΧΧΔΝΦΜΜΗΦΚΟΧΤΒΟΒΛΠΝΠΣΘΖΖΦΗΙΣΕΘΑΩΨΤΖΟΑΛΡΗΙΚΑΤΤΨΙΣΖΟΓΛΒΡΟΧΡΠΨΩΦΙΓΟΔΕΙΤΓΦΙΠΡΕΘΜΩΑΛΕΘΑΝΡΝΥΗΝΘΛΧΣΥΚΦΠΓΣΛΠΦΝΦΝΩΝΑΛΤΓΜΝΝΧΕΘΑΤΖΘΘΚΩΜΗΦΙΠΦΙΨΨΒΤΧΨΩΝΦΓΟΙΧΡΝΤΦΕΒΗΨΖΞΖΗΚΡΦΡΗΘΤΧΕΙΓΕΡΝΓΛΒΝΔΘΜΠΥΡΝΞΜΗΚΡΒΗΓΥΜΧΡΕΜΗΩΜΖΖΕΗΤΖΕΩΔΓΝΤΝΤΩΛΝΧΤΜΟΓΧΔΕΓΡΝΠΨΠΕΣΙΩΔΛΩΡΕΙΙΙΧΝΑΣΖΓΛΨΙΦΔΡΝΗΛΡΠΓΡΝΗΑΔΡΓΖΑΩΣΔΩΤΜΑΥΨΨΖΜΝΣΚΡΥΝΝΘΣΗΑΔΒΨΚΕΩΧΨΑΙΖΑΡΛΒΝΗΒΖΥΤΣΝΓΖΑΜΖΤΝΔΒΖΥΤΙΥΣΘΥΙΛΦΥΛΡΠΖΖΒΖΨΣΥΚΑΔΖΚΘΥΓΟΙΧΙΝΝΥΦΝΜΖΩΝΠΒΝΨΚΒΖΥΔΓΡΑΜΩΘΤΦΤΖΣΣΤΖΒΗΞΟΙΠΞΝΑΨΒΝΠΤΩΝΛΣΤΖΒΝΕΤΛΜΠΕΟΖΚΔΕΖΨΝΒΓΣΣΑΛΡΗΑΛΣΑΦΟΕΙΜΗΚΛΒΡΔΧΙΔΚΦΔΙΝΦΖΜΨΘΗΜΑΩΕΟΑΚΚΟΖΞΨΗΙΝΑΔΣΑΜΚΘΥ"
	
	found = False
	length = 1
	n = 24
	k = len(message)

	while found==False:
		l = list()
		matrix = list()
		length = length + 1
		for i in range(length):
			j = 0
			index = i+j*length 
			while(index < k):
				l.append(message[index])
				j = j + 1
				index = i+j*length
			matrix.append(l)
			l = list()
		for m in matrix:
			part  = u''
			for b in m:
				part = part + b
			ic = IC(part, len(part))
			if ((gr_IC - ic) == 0 or (gr_IC - ic) < 0.01):
				found = True

	print 'We found the key legth,it is',length,'and we separated the message according to this legth.Resulting in these part messages:'
	#we know key legth and we have the message separated by the correct key legth
	temp = list()
	for m in matrix:
		part = u''
		for p in m:
			part = part + p
		temp.append(part)
		print part.encode('utf-8')
	matrix = temp

	print ""
	part = matrix[0]
	all_freq = {}
	#decrypt with all the letters and gather the frequencies
	j = 1
	for part in matrix:
		frequencies = {}
		for letter in listA:
			frequencies[letter] = list()
			num = listA[letter]
			letters = {}
			for l in listA:
				letters[l] = 0
			for i in range(len(part)):
				decrypt = (listA[part[i]] - num) % 24
				letters[listB[decrypt]] = letters[listB[decrypt]] + 1
			diff = freqDiff(letters)
			frequencies[letter] = diff
		all_freq[j] = frequencies
		j = j + 1

	print "For every one of this part, we found the frequencies for every letter of the alphabet.These are:"
	for key, value in all_freq.iteritems():
		print key,':'
		for key,values in value.iteritems():
			printf(key.encode('utf-8'))
			for k,v in values.iteritems():
				printf("[")
				printf(k.encode('utf-8'))
				printf(":")
				printf(str(v))
				printf("],")
			print ""
		print ""

	decrypt = decryptMessage(message,u'ΣΡΩΟΚΘΜ')
	print "message:"
	print decrypt.encode('utf-8')

if __name__ == '__main__':
	main()