#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

# cut -------------------------------------------------------------------------

gc = 0
for i in range(len(dna)):
	if dna[i] == 'C' or dna[i] == 'G':
		gc += 1

print('%.2f' % (gc / len(dna)))
print('{:.2f}'.format(gc / len(dna)))
print(f'{gc/len(dna):.2f}')

# cut -------------------------------------------------------------------------

"""
python3 gc.py
0.42
0.42
0.42
"""
