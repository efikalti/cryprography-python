#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

listA = {u'A': 1, u'B': 2, u'C': 3, u'D': 4, u'E': 5, u'F': 6, u'G': 7, u'H': 8, u'I': 9, u'J': 10, u'K': 11, u'L': 12, u'M': 13, u'N': 14, u'O': 15, u'P': 16, u'Q': 17, u'R': 18, u'S': 19,
		 u'T': 20, u'U': 21, u'V': 22, u'W': 23, u'X': 24, u'Y': 25, u'Z': 0}
listB = {1: u'A', 2: u'B', 3: u'C', 4: u'D', 5: u'E', 6: u'F', 7: u'G', 8: u'H', 9: u'I', 10: u'J', 11: u'K',
		 12: u'L', 13: u'M', 14: u'N', 15: u'O', 16: u'P', 17: u'Q', 18: u'R', 19: u'S',
		 20: u'T', 21: u'U', 22: u'V', 23: u'W', 24: u'X', 25: u'Y', 0: u'Z'}
en_freq = {u'A': 8.16, u'B': 1.49, u'C': 2.78, u'D': 4.25, u'E': 12.7, u'F': 2.23, u'G': 2.01, u'H': 6.09, u'I': 6.96, u'J': 0.15, u'K': 0.77, u'L': 4.02, u'M': 2.4, u'N': 6.75, u'O': 7.5,
		   u'P': 1.92, u'Q': 0.09, u'R': 5.98, u'S': 6.32, u'T': 9.05, u'U': 2.75, u'V': 0.97, u'W': 2.36, u'X': 0.15, u'Y': 1.97, u'Z': 0.07}
en_IC = 0.06

letter_num = 26

def printf(format, *args):
	sys.stdout.write(format % args)

def IC(message, k):
	sum = 0
	for i in range(letter_num):
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
	for i in range(0, len(message)):
		m = message[i]
		k = key[j]
		decrypt_num = (listA[m] - listA[k]) % letter_num
		decrypt = decrypt + listB[decrypt_num]
		j = j + 1
		if j == len(key):
			j = 0
		if i == 1:
			print k, m, decrypt_num
	return decrypt

def main():
	message = u"MYHSIFPFGIMUCEXIPRKHFFQPRVAGIDDVKVRXECSKAPFGHMESJWUSSEHNEZIXFFLPQDVTCEUGTEEMFRQXWYCLPPAMBSKSTTPGSMIDNSESZJBDWJWSPQYINUVRFXPVPCEOZQRBNLUIINSRPXLEEHKSTTPGCEIMCSKVVVTJQRBSIUCKJOIIXXOVHYEFLINOEXFDPZJVFKTETVFXTTVJVRTBXRVGJRAIFPSRGTDXYSIWYXWVFPAQSSEHNEZIXFVRXQPRURVWBXWVCEIMCSKVVVUCXYWJAAGPUHYIDTMJFFSYUSISMIDNSESRRPILVUFSPTEIHYMEGMTVRRPREEDISHXHVTFVQKIIMFRQILVKRCAUPZTVGMCFVTIIQPRUPVEGIMWICFGIAVVRZQASJHKLQLEPUIIQSLRGGSUHSESUQQCWJCLPEWEJPRVDXGRRVHFWINCIPPLMKVYEFTLRGXSAHIJHVTBTHLGZRFDQZGVVKPRUPCSASWYSUAQWEMSUIHTPFDVHEEIVRSYITLRJVWTJXFIIWQAZVGZRYPGYWEIDNXYOKKUKIJOSYZSEEQVLMHPVTKYEXRNOEXAJVBBFAXTHXSYEEBEUSLWONRZQRPAJVTZVZQGRVGJLMGHRBUYZZMERNIFWMEYKSABYTVRRPUIVZKSAAMKHCIYDVVHYEZBETVZRQGCNSEIQSLLARRUICDCIIFWEEQCIHTVESJWITRVSUOUCHESJWMCHXSEXXTRVGJAUILFIKXTTWVELEXXXZSJPUUINWCPNTZZCCIZIEERRPXLMCZSIXDWKHYIMTVFDCEZTEERKLQGEUWFLMKISFFYSWXLGTPAHIIHFKQILVFKLQKIIMEEFJVVCWXTTWVWEZQCXZCEWOGMVGFYFUSIHYISDSUBVWEXRDSEGDXIJCLXRDVLBZZQGWRZSVAILVFYSASJFFKLQJRZHPSRJWRZCIHTRECNQKKSZQVMEGIRQYMZVQZZCMACWKVISGVLFIKXTTAFFCHYXPCWFREDJUSJTMXVZBXQQCAFAVRMCHCWKXXTGYWCHDTRMWTXUBWFTRWKHXVAKLMIQRYVWYTRKCIXGGIRBUMYEVZGFRUCRFQVRFEIFDCIFDXYCJIIWSTOELQPVDSZWMNHFBFXPTWGOZVFWIDWJIDNXYOKMECSNIGSZJWZGSYFILVDRWEXRXCWKDTIUHYINXXKSIRQHWFTDIZLLFTVEDILVKRCAULLARRBGSXFVWEILVVRXQDJDSEAUAPGOJWMCHUWTXMISIGUMQPRUHYIBDAVFKLQNXFCBJDDQKVVTQDTCSNMXAVVHLVZISKVVTQDTCSRRPHSCCEKMHQVBUMQAMSSIXKLMCZEIHTVGSIMEWWFZUMQGWUCEXSXZVMFYDHICJVWFDFIIKIEBIEKYSPTWGWJIKDYVBJPMKIPCLATDVVUZQQCXPCLVXXZVGKIXACFINLMIXFRFATPXKCKLUCORBUATPXKCWIQAAYCUVUAPPCLHUTXPCLXDTEKMFYXXOVQRXFAILGVCAJEJQRRZDRWCUHQGHFBKKUKIPCLVETPMSJXAILVGVYZCEKIIEXBIEARGTXRVAVRIXXYARGTXRVAZRPHEERDEOWMESYIMGXJMFYMGIECKQMRLZBVWKDYRFVRAIGRHKPQNSLOIIYTRPCLLMKIKVVPAKIFTYYYPRZHPMZNSLFYIMGXJMFYPDRKVRXQDRCMKLQJRCCMIPWEKSKLQJRCCMIPPRUHYIGCRRHLVMAWFZUMQGWUCEXRXKYHWSDHPRJVVKUMXVKJAGPZPVVFNMEHYIETZVBKLOWEGHVVAUWKZLOQXXZGNVUIXVBKLQZMEUUSYDJXCUMELMKVZRYPRECKSZTQRBESDPKICLTAUQVBSYFXRRZCQQCMEMFYKDYKVVTQDTCSYEHTXYSGSITVKVVTALIIHFGDTEKSDEOWMESJXTTTFKVVFDGISRXQWEGDZRQHWPCLXTTTVCGPQWEMSKLQESNSIXABEBSKLUHPZTVJDTIRBUFQPYKWWYXISDOBIFWMJZZJQPAFBUIDUYCOUZQCXLFVXTTRZBKLQCEDSFJPTQFQIEONPVHLWGHIKVRXBDAVFCIFJWRZCYZXXVZVXGHJZUYXRDVRBVAIDVCRRHQRIEHNSDAHKVRXIXPCUZZQBIEOTLMCGVHFAAGOKVRXIXPCUZZQNSLHYERJXLFVEZSSCRRKQPWVQLVUICSMKLQEVFAZWQDJKVVWQILZBXWNGYKSJLMKIIWJIZISGCNIDQYKHYIKAMVHYIKSSECKJGAJZZKLMITICDMETXYSPRQKIIKZPXSMTHRXAGWWFVIFWIDGVPHTWSIKXTTCVBJPMKIKVVTQDTCSESIAIKIJJUVLKHFJGAJZZKLMITICDMETPVHLWRXKYHKSRGIVHYIIDVCRKSPDENOPAUILEOKMACECPRVDXIIGKSPDENOPAUILXFVIPLMKVYEFTEERZRFDPVFRROTPVHLWRXKYHWSDPAFFCHAUVVOJSZPAFFCHIWIISJGUTRTSRRPEVFUIIEHAZZCPQPHKCRPXBIEGYEBEMESJWEDPUWVVEXRKVVRMBIFTUIYDGIOTCXTXLGRPXJRZHV"

	found = False
	length = 1
	n = letter_num
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
			if ((en_IC - ic) == 0 or (en_IC - ic) < 0.01):
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
				decrypt = (listA[part[i]] - num) % letter_num
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
			print
			for k,v in values.iteritems():
				printf("[")
				printf(k.encode('utf-8'))
				printf(":")
				printf(str(v))
				printf("],")
			print ""
		print ""

	decrypt = decryptMessage(message,u'DLODQNQ')
	print "message:"
	print decrypt.encode('utf-8')

if __name__ == '__main__':
	main()
