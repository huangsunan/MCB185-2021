#!/usr/bin/env python3

# Move the triple quotes downward to uncover each segment of code

"""

# Review: a list is constructed with square brackets
# and indexed by integers in square brackets

alist = ['cat', 'dog', 'fox']
print(alist[1])

# What if you could put text inside of the brackets instead of numbers?
# What would that look like?
# alist['red']
# That's what dictionaries are!

# A dictionary is constructed with curly brackets {}
# Like lists, dictionaries are indexed with square brackets []
# Individual items have key:value pairs where the key is usually a string

adict = {'cat':'meow', 'dog':'woof', 'fox':'????'}
print(adict['dog'])

# Dictionaries are used primarily for 2 things
# 1. efficient look-up tables
# 2. structures

# Look-up table for genetic code

gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}
dna = 'ATGGTTCGCCAAGGAAACCTCCATCCCATGTNTCGGAGAATCTCTCCCGCTCCGACCGCT'
# note the N right here               ^

# This code translates DNA to protein
pro = ''
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	if codon in gcode: pro += gcode[codon] # that's the dictionary lookup!
	else:              pro += 'X' # because sometimes there are Ns and such
print(pro)


# Dictionaries can be used as efficient storage containers
# This code counts k-mers

k = 2
count = {}
for i in range(len(dna) -k +1):
	kmer = dna[i:i+k]
	if kmer in count: count[kmer] += 1
	else:             count[kmer] = 1
for kmer in count:
	print(kmer, count[kmer])


# Another use of dictionaries is as 'structures'

person = {'name':'Ian', 'birthyear':1967, 'job':'Professor'}
print(person)

# Alternative syntax

person = {}
person['name'] = 'Ian'
person['birthyear'] = 1967
person['job'] = 'Professor'
print(person)

# A very common data structure is the list of dictionaries

pokemon = [
	{'name':'Arceus', 'HP':140, 'Speed':140},
	{'name':'Deoxys', 'HP':113, 'Speed':152},
	{'name':'Dream',  'HP':110, 'Speed':110},
]

for m in pokemon:
	print(m['name'])

for m in pokemon:
	m['HP'] -= 5

print(pokemon)

"""
