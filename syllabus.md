Syllabus for MCB185
===================

## Files & Directories ##

+ `README.md` - an overview of the repository
+ `SYLLABUS.md` - this document
+ `GUMPY.md` - intro to GitHub, Unix, Markdown, and Python
+ `Tutorials` - tutorials written in python source code
+ `Programs` - programs for the students
+ `Solutions` - solved program problems
+ `Data` - data files used by tutorials and programs

## Lessons ##

The lessons are currently designed for a 10-week quarter with Lesson 9 being 2
weeks long. For grading purposes, there are homework assignments in weeks 1-8,
and a final project for weeks 9 + 10.

+ Lesson 1: Tools of the Trade
+ Lesson 2: Variables, Math, and Loops
+ Lesson 3: Loops and Conditionals
+ Lesson 4: Lists and Files
+ Lesson 5: Functions
+ Lesson 6: CLI and Modules
+ Lesson 7: Dictionaries and Regex
+ Lesson 8: Complex Data
+ Lesson 9: Projects

Lesson 1: Tools of the Trade
============================

## Learning Objectives ##

* Unix - basic commands and directory structure
* Python - write your first program
* GitHub - create your repository
* Markdown - simple and flexible text file formatting

## Lesson Plan ##

Follow the directions in `GUMPY.md`.

At the end of the lesson, you will have your own GitHub repository with your
first Python program: `hello_world.py`. Along the way you will have learned some
of the most useful Unix commands, be able to navigate the Unix directory
structure, and save typing with tab-completion. You will also learn how to use
Markdown to create simple text files that can be easily converted to HTML, PDF,
etc.

Lesson 2: Variables, Math, and Loops
====================================

## Learning Objectives ##

* Variables - strings, ints, floats, None, type()
* Math - math operators and functions
* Text - string operators and functions

## Tutorials ##

Start with `01_variables.py`. The first thing you will learn is about comments.
That is, text you put into programs that don't actually do anything other than
provide information. Comments start with a `#` sign, which is called number
sign, pound, or hash, but not hashtag. Comments are used during programming for
debugging. One way to comment-out a large section of code is with triple quotes.

In `01_variables.py` you will learn that variables are containers that can hold
different kinds of things, like numbers and text. Each variable has a *type*
which can be seen with the `type()` function. Variables of different types don't
always play well together, so you may need to convert them with functions like
`int()`, `float()`, or `str()`. You are also introduced to the `None` type,
which turns out to be a really useful for debugging later.

Next, follow `02_math.py`. Here, you will learn that the typical mathematics
operations you are already familar (addition, subtraction, multiplication,
division, exponentiation) are also in Python. However, the symbol for
multiplication is `*` and exponentiation is `**`. The standard rules for
precedence are: multiplication and division before addition and subtraction. But
what about exponentiation and other operations like `%` (modulo)? Use
parentheses when in doubt. Heck, use parentheses even when not in doubt.

In `02_math.py` you are first introduced to the concept of libraries (also
called modules). For example, the `log2()` function is in the `math` library.
You must first `import` that math libray and then the `log2()` function becomes
available.

	import math()
	print(math.log2(1))

Next, follow `03_text.py`. Here, you will learn that some of the math operators
like `+` and `*` also work on strings. You will also see the `len()` function
for the first time, which returns the length of a string (also the length of a
list, but that comes later). You are also introduced to the string slice syntax,
which allows you to retrieve part of a string. Finally, you will learn how to
format strings for printing.

In `04_loops.py` you will be _introduced_ to loops. We will be spending much
more time with loops in the next lesson. Here, you will learn how to iterate
over a `range()` of numbers or the characters in a string.

## Coding Exercises ##

It's time to change directories to your `learning_python` repository and write
some programs that you can check into your own repository.

Copy `codons.py` and `sumfac.py` to your `learning python` repo and
follow the directions in each file. You will find these in the `Programs`
directory.

## Python Manifest ##

### Operators

	=
	+
	-
	*
	/
	**
	%
	//
	\
	
### Keywords

	in
	
### Functions

	float()
	int()
	len()
	range()
	str()
	type()
	
### Libraries

A little bit of the `math` library was used in the tutorial. Here are some
useful constants and functions.

	math.e
	math.pi
	math.inf
	math.nan
	math.tau
	math.ceil()
	math.factorial()
	math.log()
	math.log2()
	math.floor()
	math.sqrt()

## File Manifest ##

	01_variables.py
	02_math.py
	03_text.py
	04_loops.py

Lesson 3: Loops and Conditionals
================================

## Learning Objectives ##

* Conditional Execution - Boolean type, if, elif, else, while, break, continue
* String Formatting - various ways or printing

## Tutorials ##

Start your tutorial session with `05_conditionals.py`. Here you will learn about
the `if` statement and its related parts `elif` and `else`. You will use `if`
statements constantly in your programs. Conditional statements evalute to either
`True` or `False`. These are known as Boolean values. The Boolean operators
include `and`, `or`, and `not`. You will also be introduce to the `while` loop,
which uses a conditional statement to stop the loop. In addition, you will be
introduced to the `continue` and `break` statements, which can be used with both
`for` and `while` loops to skip ahead or stop the loop entirely.

Next, follow `06_loops_and_conditionals.py`. The examples here demonstrate how
mixing loops and conditionals can make complex structures.

The tutorials are very short this lesson in order to make room for lots of
practice using loops and conditionals.

## Coding Exercises ##

For programming practice, try writing the following programs.

1. `gc.py`
2. `fizzbuzz.py`
3. `at_seq.py`
4. `anti.py`
5. `frame.py`
7. `aa_pairs.py`
7. `gc_win1.py`
8. `gc_win2.py`

Copy these to your `learning_python` directory and `git push` them from there.

## Python Manifest ##

### Operators

	and
	not
	or

### Keywords

	while
	break
	continue

### Functions

	
### Libraries

	random

## File Manifest ##

	05_conditionals.py
	06_loops_and_conditionals.py
	aa_pairs.py
	anti.py
	at_seq.py
	fizzbuzz.py
	gc.py
	gc_win1.py
	gc_win2.py

Lesson 4: Lists and Files
=========================

## Learning Objectives ##

* tuples - immutable, comma separated values (in parentheses)
* lists - mutable, comma separarted values [in brackets]
* list functions - append(), pop(), insert(), sort(), list()

## Tutorials ##

Start with `07_lists.py`, where you will learn how to create tuples and
lists. The Python *list* is what other languages call an *array*. A lot
of the work in programming is done by iterating over lists. Python has
some advanced/confusing list concepts, and if you're interested in
these, also check out the content in `07_lists_extra.py` where you will
see *list comprehension*.

Next, follow `08_assert.py` to learn about the `assert()` function and
how it can help you identify problems in your programs.

Lastly, `09_fileinput.py` shows you how to get data into your program,
whether that data comes from a file or Unix pipe.

## Coding Exercises ##

For programming practice, try writing the following programs. The
instructions are inside each file.

Copy these to your `learning_python` directory and also the data files.
Don't program in the `MCB185` directory !

1. `rand_seq.py`
2. `birthday.py`
3. `xcoverage.py`
4. `entropy.py`
5. `proc23.py`
6. `stats.py`
7. `seqstats.py` (requires `07_lists_extra.py`)

## Python Manifest ##

### Operators

	,
	[]

### Functions

	assert()
	len(list)
	list()
	zip()

### Methods

	list.append()
	list.insert()
	list.pop()
	list.split()
	list.sort()
	
	string.join()
	string.rstrip()
	string.startswith()

### Libraries

	sys.argv

## File Manifest ##

	00README.md
	07_lists.py
	07_lists_extra.py
	08_assert.py
	09_fileinput.py
	birthday.py
	entropy.py
	nucleotides.txt
	numbers.txt
	proc23.py
	rand_seq.py
	seqstats.py
	stats.py
	xcoverage.py

Lesson 5: Functions
===================

## Learning Objectives ##

* Open and read from named files, both normal and compressed
* Search for items inside lists
* Define functions
* Iterate through fasta files

## Tutorials ##

Start with `10_files.py`, where you will learn how to open and read from
named files, for example, those named on the command line. You can also
open and read from compressed files without first decompressing them
using the `gzip` library. If you want to learn how to write or append to
files, check out `10_files_extra.py`.

The next tutorial is really short, `11_in.py`, but it has two very
important concepts: the use of `in` for searching, and the `time`
library for benchmarking.

The main part of the lesson is `12_functions.py`. Functions are units of
code re-use and are one of the most important concepts in programming.
In addition to the instruction, you will also find a `read_fasta()`
function inside `12_functions.py`, which we will copy-paste into other
programs (for now, later we will put it in a proper module).

Python function syntax is highly customizable, but sort of confusing.
For that reason, you can find a more complete explanation in
`12_functions_extra.py`. Here also you will find *generator* functions,
which let you turn functions into iterators.

## Coding Exercises ##

For programming practice, try writing the following programs. The
instructions are inside each file.

Copy these to your `learning_python` directory and also the data files.
Don't program in the `MCB185` directory !

1. `exonic_snps.py`
2. `pepsearch.py`
3. `fasta_stats.py`
4. `rand_fasta.py`
5. `longest_orf.py`
6. `transmembrane.py`
7. `longest_cds.py` (requires `12_functions_extra.py`)

## Python Manifest ##

### Keywords

	def
	return
	with
	yield

### Functions

	open()

### Methods

	file.read()
	file.readline()
	file.readlines()
	
	time.perf_counter()

### Libraries

	gzip.open()

## File Manifest ##

	00README.md
	10_files.py
	10_files_extra.py
	11_in.py
	12_functions.py
	12_functions_extra.py
	exonic_snps.py
	exons.txt.gz
	fasta_stats.py
	longest_cds.py
	longest_orf.py
	pepsearch.py
	proteins.fasta.gz
	rand_fasta.py
	snps.txt.gz
	strings.txt.gz
	transcripts.fasta.gz
	transmembrane.py


Lesson 6: CLI and Modules
=========================

## Learning Objectives ##

## Tutorials ##

## Coding Exercises ##

## Python Manifest ##

### Keywords

### Operators

### Functions

### Methods

### Libraries

## File Manifest ##


Lesson 7: Dictionaries and Regex
================================

## Learning Objectives ##

## Tutorials ##

## Coding Exercises ##

## Python Manifest ##

### Keywords

### Operators

### Functions

### Methods

### Libraries

## File Manifest ##


Lesson 8: Complex Data
======================

## Learning Objectives ##

## Tutorials ##

## Coding Exercises ##

## Python Manifest ##

### Keywords

### Operators

### Functions

### Methods

### Libraries

## File Manifest ##


