#!/usr/bin/env python

import zipfile, os

def extractFile(zFile, password):
	try:
		os.remove("test_zip")
	except:
		pass
	try:
		zFile.extractall(pwd=password)
		stats = os.stat('test_zip')
		if (stats.st_size >= 59):
			print "Password is", password
			return True
		else:
			os.remove("test_zip")
	except:
		return False

def main():
	zFile = zipfile.ZipFile("test_zip.zip")
	infile = open(u"english.txt", "r")
	for password in infile:
		password = password.strip()
		success = extractFile(zFile, password)
		if success:
			break
	infile.close()

if __name__ == '__main__':
	main()