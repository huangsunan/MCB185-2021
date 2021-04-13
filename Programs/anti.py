#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

# cut -------------------------------------------------------------------------

anti = ''
for i in range(len(dna)):
	nt = dna[i]
	if   nt == 'A': nt = 'T'
	elif nt == 'C': nt = 'G'
	elif nt == 'G': nt = 'C'
	elif nt == 'T': nt = 'A'
	else:
		print('error')
	anti = nt + anti
print(anti)


# cut -------------------------------------------------------------------------

"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
