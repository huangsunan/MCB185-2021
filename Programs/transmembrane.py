#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# cut -------------------------------------------------------------------------

def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				words = line.split()
				name = words[0][1:]
				seqs = []
			else:
				words = line.split()
				name = words[0][1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

def kd_hydropathy(aa):
	if aa == 'I': return 4.5
	if aa == 'V': return 4.2
	if aa == 'L': return 3.8
	if aa == 'F': return 2.8
	if aa == 'C': return 2.5
	if aa == 'M': return 1.9
	if aa == 'A': return 1.8
	if aa == 'G': return -0.4
	if aa == 'T': return -0.7
	if aa == 'S': return -0.8
	if aa == 'W': return -0.9
	if aa == 'Y': return -1.3
	if aa == 'P': return -1.6
	if aa == 'H': return -3.2
	if aa == 'E': return -3.5
	if aa == 'Q': return -3.5
	if aa == 'D': return -3.5
	if aa == 'N': return -3.5
	if aa == 'K': return -3.9
	if aa == 'R': return -4.5
	return 0 # unknown

def hah(pep, w, t):
	for i in range(len(pep)):
		seq = pep[i:i+w]
		hydro = 0
		for aa in seq:
			hydro += kd_hydropathy(aa)
		if hydro/w > t and 'P' not in seq: return True
	return False

for name, seq in read_fasta(sys.argv[1]):
	nterm = seq[0:30]
	cterm = seq[30:]
	if hah(nterm, 8, 2.5) and hah(cterm, 11, 2):
		print(name)

# cut -------------------------------------------------------------------------

"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
