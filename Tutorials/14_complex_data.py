#!/usr/bin/env python3

# Move the triple quotes downward to uncover each segment of code

"""

# Complex data is a mixture of lists and dictionaries

# The 2D list is very common (e.g. spreadsheet)
matrix = [
	[1, 2, 3],
	[5, 7, 9],
	['cat', 'dog', 'pig'],
]
print(matrix[0][1])

# Here's a list of dictionaries (like a spreadsheet with named columns)
records = [
	{'name': 'Ian',    'job': 'Professor'},
	{'name': 'Chris',  'job': 'Student'},
	{'name': 'Jordan', 'job': 'Programmer'}
]
for r in records: print(r['name'])

# There are also dictionaries of lists
genome = {
	'chrom1': ['gene-1', 'gene-2', 'gene-3'],
	'chrom2': ['gene-4', 'gene-5', 'gene-6'],
	'chromX': ['gene-7', 'gene-8'],
}
for chrm in genome:
	for gene in genome[chrm]:
		print(chrm, gene)

# Here's a dictionary of dictionaries, which can form a tree
taxa = {
	'Metazoa': {
		'Vertebrata': {
			'Mammalia': {
				'Primates': {
					'Hominidae': {
						'Homo': 'sapiens'
					}
				},
				'Rodentia': {
					'Muridae': {
						'Mus': 'musculus'
					}
				}
			},
			'Teleostei': {
				'Cypriniphsae': {
					'Danionidae': {
						'Danio': 'rerio'
					}
				}
			}
		}
	},
	'Viridiplantae': {
		'Tracheophyta': {
			'Magnolipsida': {
				'Pentapetalae': {
					'Brassicacea': {
						'Arabidopsis': 'thaliana'
					}
				}
			}
		}
	}
}

print(taxa) # doesn't print beautifully

import json
print(json.dumps(taxa, indent=4)) # does print beautifully

"""
