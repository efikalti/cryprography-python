#!/usr/bin/env python

import zipfile

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print "Password is", password
		return True
	except:
		return False

def main():
	zFile = zipfile.ZipFile("test_zip.zip")
	infile = open("english.txt", "r")
	for password in infile:
		password = password.strip('\n')
		success = extractFile(zFile, password)
		if success:
			break
	infile.close()

if __name__ == '__main__':
	main()