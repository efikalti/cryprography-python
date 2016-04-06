#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def printf(format, *args):
    sys.stdout.write(format % args)


listA = {u'Α': 1, u'Β': 2, u'Γ': 3, u'Δ': 4, u'Ε': 5, u'Ζ': 6, u'Η': 7, u'Θ': 8, u'Ι': 9, u'Κ': 10, u'Λ': 11, u'Μ': 12, u'Ν': 13, u'Ξ': 14, u'Ο': 15, u'Π': 16, u'Ρ': 17, u'Σ': 18, u'Τ': 19, u'Υ': 20, u'Φ': 21, u'Χ': 22, u'Ψ': 23, u'Ω': 0}
listB = {1: u'Α', 2: u'Β', 3: u'Γ', 4: u'Δ', 5: u'Ε', 6: u'Ζ', 7: u'Η', 8: u'Θ', 9: u'Ι', 10: u'Κ', 11: u'Λ', 12: u'Μ', 13: u'Ν', 14: u'Ξ', 15: u'Ο', 16: u'Π', 17: u'Ρ', 18: u'Σ', 19: u'Τ', 20: u'Υ', 21: u'Φ', 22: u'Χ', 23: u'Ψ', 0: u'Ω'}

message = u'ΟΚΗΘΜΦΔΖΘΓΟΘΧΥΚΧΣΦΘΜΦΜΧΓΟΣΨΧΚΠΦΧΘΖΚΠ'

for shift in range(24):
    for i in range(len(message)):
		index = (listA[message[i]]+shift) % 24
		printf(listB[index].encode('utf-8'))
    print ""
