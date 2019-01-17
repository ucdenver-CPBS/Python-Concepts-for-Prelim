# Python Concepts for the Prelim
Python packages and concepts that you should be very familiar with before the prelim.

You can find lots of exercises at the [Rosalind](http://rosalind.info/problems/locations/) website.
But first, check to see what looks familiar here.


## Concepts:
### [loops](loops_examples.py)
- for
- while
- [list comprehension](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
```python
print([x + 1 for x in [1, 2, 3]])
```
### [abstraction](abstraction_examples.py)
- functions
	- reasons to use
		- reuse duplicated code
		- paramaterization
		- make code easier to read
	- example
```python
def add_one(x):
	return x + 1
```
- classes
    - example
```python
class Human:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return "%s is %d years old" % (self.name, self.age)
```
### [scope](scope_examples.py)
- local
- global
### [parallelism](parallelism_examples.py)
- reasons to use:
    - large amount of data to process
    - processing tasks can be made independent
    - some initial overhead is worth the speed up
    - make use of cluster
- example
```python
import  multiprocessing
from time import sleep
def fun1(name):
    sleep(2)
    print(f"Hello {name}")
names = ["Jennifer", "Emily", "Kendra"]

print("There are %d cores on this computer" % multiprocessing.cpu_count())

# I like to leave one core available so I can still use my computer
num_cores_to_use = multiprocessing.cpu_count() - 1

pool = multiprocessing.Pool(num_cores_to_use)
pool.map(fun1, names)
```
- more in depth examples [here](https://sebastianraschka.com/Articles/2014_multiprocessing.html)
### [strings](strings_examples.py)
- reasons to use
    - names, fields, headers, qualitative data
    - file locations
    - token lists (such as for NLP tasks)
- [formatting](https://realpython.com/python-string-formatting/)
    - format operators: %s, %d
    -example
```python
name = "Harrison"
age = 22

print("%s is %d years old" % (name, age))

print("%s is %d years old".format(name, age))

print(f"{name} is {age} years old")
```
### [parsing](parsing_examples.py)
- files
    - sequence files
    - text files
    - example
```python
filename = 'filename.txt'
sep = ','
with open(filename) as f:
	for line in f.readlines():
		# Remove white space at end and split by a separator token
		row = line.strip().split(sep)
		for col in row:
			print(col)
```

- search <!-- TODO: -->
- sort  <!-- TODO: -->
	- example: `x.sort()`
### IDE
- [Pycharm](https://www.jetbrains.com/pycharm/) *this is the one I recommend*
- [Sublime Text](https://www.sublimetext.com/)
- Vi/Vim
- Emacs
- Whatever text editor you like really...BUT learn how to use it properly
    - Learn the keyboard shortcuts
        - Refactor (this will save you a lot of time)
        - Jump to error
        - Insert comment
        - Jump to implementation (go straight to where the function or class was defined in the code)
    - Learn the built in debugger
        - More on this below
    - How to run and test quickly
    - How to spot errors and warning before you run
    
### [debugging](https://www.jetbrains.com/help/pycharm/part-1-debugging-python-code.html)
- reasons to use
    - code is broken
- breakpoints
    - set breakpoints before you expect code to fail
    - use conditions to break on particular iterations of a loop
- variable inspection
    - see what each variable is at the break point
    - set variables before continuing to see how changes in input affect the code
- call stack
    - see what function calls lead to your break
    - go back to see how things looked in those functions

### version control
- [git](https://www.github.com)

### pseudocode
- high level
- not code

### commenting
- reasons to use
    - explain to others what your code is doing
    - explain to yourself what your code is doing
- example //TODO
```python
num_list = [1, 8, 7, 3, 5]
last = 0
sorted_num_list = []

```

Packages:
- [argparse](https://docs.python.org/3.3/library/argparse.html)
	- Easily define command line inputs
- [numpy](numpy_examples.py)
