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

Copy `codons.py`, `gc.py`, and `sumfac.py` to your `learning python` repo and
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
