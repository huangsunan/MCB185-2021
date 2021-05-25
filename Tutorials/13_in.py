#!/usr/bin/env python3

# Move the triple quotes downward to uncover each segment of code

"""

# The 'in' keyword is used in several different ways!

# 1. Used with range() function
for i in range(3): print(i)

# 2. Used to iterate over values in containers
for nt in 'ACGT': print(nt) # string container
for pet in ('cat', 'dog', 'bun'): print(pet) # tuple container
for p in [0.4, 0.3, 0.2, 0.2]: print(p) # list container

# 3. Used to iterate over keys of a dictionary
d = {'cat':'meow', 'dog':'woof', 'fox':'????'}
for animal in d: print(animal)

# 4. Used to search for items in a container (this is new)
protein = 'MVGGKKKTKICDKVSHEEDRISQLPEPLISEI'

# compare this clunky code
contains_proline = False
for aa in protein:
	if aa == 'P':
		contain_proline = True
		break
if contains_proline: print('found')

# to this elegant code
if 'P' in protein: print('found again')

# You can search through lists using 'in' of course
colors = ['red', 'blue', 'green']
if 'yellow' in colors: print('yellow!')
else: print('no yellow')

# You can search through dictionary keys with 'in'
if 'cat' in d: # also works as d.keys()
	print('yes, cat is in', d)

# You can also search through values
if 'woof' in d.values():
	print('yes, woof is a value of', d)
	
"""