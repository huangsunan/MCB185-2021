Final Projects
==============

Reviewing what you know so far:

- Unix
- Variables, math, text
- Loops and conditionals
- Lists and dictionaries
- Functions and libraries
- CLI w/ argparse
- Files and complex data

At this point, you know enough programming concepts to be a very effective
software developer. Let's show off your knowledge with a final project. You are
encouraged to work in teams and to consult your instructor frequently. Here are
some ideas.

## Complexity Filter ##

Make a program that inputs genomic sequence and outputs a masked version of the
sequence where low-complexity regions are replaced either with an ambiguity
character (N for nt, X for aa) or lowercase. Your program should work with
either nucleotide or amino acid sequence and have separate default thresholds
for each. The output should allow for lowercase, N, or X, as appropriate. It
should also report the sequence as a FASTA file in 80 column width.

## Scoring Matrix ##

Make a scoring matrix, like BLOSUM62, using actual multiple alignment data. You
can use nucleotides or amino acids.

## SNP Annotation ##

Cross-reference SNPs from 23andme to genes. Ever wondered which SNPs lie in
which genes? Or for more resolution, which SNPs probably break proteins and
which are just markers in the middle of knowhere? Get some 23andme data and
intersect it with genome data.

## Motif Drawing ##

You know those really cool drawings of motifs with different height letters?
Write your own program to make those pictures. Use SVG for the output.

## Elvish Generator ##

Ever wonder how games create new fantasy names? By making digrams and trigrams
of the letter frequencies. You can write that program. Generate your own Elvish
by mixing Welsch and Finnish, for example.

## Smith Waterman ##

The classic pairwise alignment program is a great exercise for your brain. You
can do Needleman-Wunsch if you prefer or even make a program that does both.

## Viterbi ##

Make an HMM to model _something_ and then the Viterbi algorith to decode the
most likely path. Examples include CpG islands, exons, introns, ORFs.

## Teaching ##

Nobody learns more than the teacher! Write a tutorial and example programs for
future MCB185/MCB186 lessons. Here are some potential topics.

- regular expressions
- matplotlib
- numpy
- pandas
- scipy
- scikit-learn
- OpenCV
- sqlite3

