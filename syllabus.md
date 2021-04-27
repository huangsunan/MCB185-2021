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

Lesson 4: Tuples and Lists
==========================

## Learning Objectives ##

* tuples - immutable, comma separated values (in parentheses)
* lists - mutable, comma separarted values [in brackets]
* list functions - append(), pop(), insert(), sort()

## Tutorials ##

In `07_lists.py`, you will learn how to create tuples and lists. The Python
*list* is what other languages call an *array*. A lot of the work in programming
is done by iterating over lists. You will also be introduced to the `zip()` and
`enumerate()` functions. Finally, you will see a bit of optional syntactic sugar
called *list comprehension*.

## Coding Exercises ##

For programming practice, try writing the following programs. The instructions
are inside each file.

Copy these to your `learning_python` directory and also the data files.

1. `birthday.py`
2. `stats.py`
3. `entropy.py`
4. `xcoverage.py`

## Python Manifest ##

### Operators

	,
	[]

### Functions

	enumerate()
	len(list)
	list()
	zip()

### Methods

	list.append()
	list.insert()
	string.join()
	list.pop()
	list.sort()
	list.split()

### Libraries

	sys

## File Manifest ##

	00README.md
	07_lists.py
	birthday.py
	entropy.py
	stats.py
	xcoverage.py


Lesson 5: Functions
===================

## Learning Objectives ##

* Define functions
* Use assertions
* Open and read from named files
* Search for items inside lists

## Tutorials ##

The only tutorial this lesson is `08_functions.py`, where you will learn how to
write blocks of code that perform specific duties whenever you call them.
Functions are the building blocks of complex programs. Here, you will also
observe that floating point math is an approximation of real math. As a result,
we have to use functions like `math.isclose()` to check for equality. This
tutorial also introduces `assert()`, which you can use to ensure your functions
receive proper values.

## Coding Exercises ##

For programming practice, try writing `randomfun.py` in the Programs directory.


## Python Manifest ##

### Keywords

	def
	return
	with
	yield

### Functions

### Methods

### Libraries

## File Manifest ##

	08_functions.py
	randomfun.py

