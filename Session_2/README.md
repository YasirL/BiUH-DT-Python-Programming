# Advanced Features

Mastering Python's data types, statements, and functions allows you to write many useful programs. For example, to create a list like `[1, 3, 5, 7, ..., 99]`, you can use a loop:

```python
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
```

To get the first half of the list, you can also use a loop. However, in Python, "more code is not better—less is better; more complexity is not better—simplicity is better". Based on this idea, we introduce Python's powerful advanced features—if a function can be implemented in 1 line of code, never write 5 lines. Always remember: less code means higher development efficiency.

## 1. Slicing

Retrieving a portion of elements from a list or tuple is a very common operation. For example, given a list:

```python
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
```

How to get the first 3 elements?

### Naive Approach

```python
>>> [L[0], L[1], L[2]]
['Michael', 'Sarah', 'Tracy']
```

This is inefficient because it won’t work if you need to get the first N elements.

### Loop Approach

To get the first N elements (i.e., elements with indices 0 to N-1), you can use a loop:

```python
>>> r = []
>>> n = 3
>>> for i in range(n):
...     r.append(L[i])
...
>>> r
['Michael', 'Sarah', 'Tracy']
```

### Slicing Operator

For frequent operations of retrieving elements within a specific index range, loops are cumbersome. Thus, Python provides the **slicing** operator to simplify this:

```python
>>> L[0:3]
['Michael', 'Sarah', 'Tracy']
```

`L[0:3]` means "retrieve elements starting from index 0 up to (but not including) index 3"—i.e., elements at indices 0, 1, 2—exactly 3 elements.

- If the starting index is 0, you can omit it:
  
  ```python
  >>> L[:3]
  ['Michael', 'Sarah', 'Tracy']
  ```
- You can also start from index 1 and retrieve 2 elements:
  
  ```python
  >>> L[1:3]
  ['Sarah', 'Tracy']
  ```
- Python supports negative indexing (where `-1` refers to the last element), so you can also use **negative slicing**:
  
  ```python
  >>> L[-2:]  # Get the last 2 elements
  ['Bob', 'Jack']
  >>> L[-2:-1]  # Get the second-to-last element (excludes the last element)
  ['Bob']
  ```
  
  Remember: the index of the last element is `-1`.

### Practical Slicing Examples

First, create a sequence of numbers from 0 to 99:

```python
>>> L = list(range(100))
>>> L
[0, 1, 2, 3, ..., 99]
```

Use slicing to retrieve specific segments:

- First 10 elements:
  
  ```python
  >>> L[:10]
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```
- Last 10 elements:
  
  ```python
  >>> L[-10:]
  [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
  ```
- Elements from index 10 to 19:
  
  ```python
  >>> L[10:20]
  [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  ```
- First 10 elements, taking every 2nd element:
  
  ```python
  >>> L[:10:2]
  [0, 2, 4, 6, 8]
  ```
- All elements, taking every 5th element:
  
  ```python
  >>> L[::5]
  [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
  ```
- Copy the entire list (use `[:]` with no indices):
  
  ```python
  >>> L[:]
  [0, 1, 2, 3, ..., 99]
  ```

### Slicing for Tuples and Strings

- **Tuples**: Tuples are immutable lists, so slicing works for tuples too, and the result is still a tuple:
  
  ```python
  >>> (0, 1, 2, 3, 4, 5)[:3]
  (0, 1, 2)
  ```
- **Strings**: A string can be seen as a list of characters, so slicing applies to strings (result is still a string):
  
  ```python
  >>> 'ABCDEFG'[:3]
  'ABC'
  >>> 'ABCDEFG'[::2]
  'ACEG'
  ```
  
  Many programming languages provide dedicated string截取 (substring) functions, but Python uses slicing for all such operations—it’s extremely simple.

### Exercise

Implement a `trim()` function using slicing to remove leading and trailing spaces from a string. **Do not use the `str.strip()` method**:

```python
def trim(s):
    return s

# Test cases
if trim('hello ') != 'hello':
    print('Test failed!')
elif trim(' hello') != 'hello':
    print('Test failed!')
elif trim(' hello ') != 'hello':
    print('Test failed!')
elif trim(' hello world ') != 'hello world':
    print('Test failed!')
elif trim('') != '':
    print('Test failed!')
elif trim(' ') != '':
    print('Test failed!')
else:
    print('Test success!')
```

### Summary

With slicing, loops are no longer needed for many scenarios. Python slicing is highly flexible—one line of code can replace what would take multiple lines of loops.

## 2. Iteration

If you have a list or tuple, you can traverse it using a `for` loop—this traversal is called **iteration**.

In Python, iteration is implemented via `for ... in`, which is more abstract than the index-based `for` loops in languages like C:

```c
// C-style loop (uses indices)
for (i = 0; i < length; i++) {
    n = list[i];
}
```

Python’s `for` loop works not only for lists/tuples but also for other **iterable objects** (objects that support iteration).

### Iteration for Dictionaries

Dictionaries (`dict`) have no indices, but you can still iterate over them:

```python
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...     print(key)
...
a
c
b
```

By default, `for ... in` iterates over the **keys** of a `dict`. To iterate over **values**, use `for value in d.values()`; to iterate over both keys and values, use `for k, v in d.items()`:

```python
# Iterate over values
>>> for value in d.values():
...     print(value)
...
1
2
3

# Iterate over key-value pairs
>>> for k, v in d.items():
...     print(k, '=', v)
...
a = 1
b = 2
c = 3
```

### Iteration for Strings

Strings are iterable objects, so they work with `for` loops:

```python
>>> for ch in 'ABC':
...     print(ch)
...
A
B
C
```

### Check if an Object Is Iterable

To determine if an object is iterable, use the `Iterable` type from the `collections.abc` module:

```python
>>> from collections.abc import Iterable
>>> isinstance('abc', Iterable)  # Is string iterable?
True
>>> isinstance([1,2,3], Iterable)  # Is list iterable?
True
>>> isinstance(123, Iterable)  # Is integer iterable?
False
```

### Indexed Iteration for Lists

If you need to iterate over a list with indices (like Java), use Python’s built-in `enumerate()` function—it converts a list into an "index-element pair" iterator:

```python
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
```

Using two variables in a `for` loop is common in Python. For example:

```python
>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print(x, y)
...
1 1
2 4
3 9
```

### Exercise

Use iteration to find the minimum and maximum values in a list and return them as a tuple:

```python
def findMinAndMax(L):
    return (None, None)

# Test cases
if findMinAndMax([]) != (None, None):
    print('Test failed!')
elif findMinAndMax([7]) != (7, 7):
    print('Test failed!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('Test failed!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('Test failed!')
else:
    print('Test success!')
```

### Summary

Any iterable object can be used in a `for` loop—including custom data types—as long as they meet the iteration requirements.

## 3. List Comprehensions

List Comprehensions are Python’s built-in, simple yet powerful tool for creating lists.

### Basic Usage

To create `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, use `list(range(1, 11))`:

```python
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

To create `[1×1, 2×2, 3×3, ..., 10×10]`, you can use a loop:

```python
>>> L = []
>>> for x in range(1, 11):
...     L.append(x * x)
...
>>> L
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

With List Comprehensions, you can replace the loop with **one line of code**:

```python
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

The syntax for List Comprehensions is:  
`[expression for item in iterable]`  
Place the element to generate (`x * x`) first, followed by the `for` loop—this creates the list concisely.

### Add Conditionals to List Comprehensions

You can add an `if` statement after the `for` loop to filter elements. For example, keep only the squares of even numbers:

```python
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
```

### Nested Loops in List Comprehensions

Use **two levels of loops** to generate permutations. For example, generate all combinations of characters from `'ABC'` and `'XYZ'`:

```python
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

Three or more levels of loops are rarely used.

### Practical Examples

- List all files/directories in the current directory (use the `os` module):
  
  ```python
  >>> import os  # Import the os module (covered later in "Modules")
  >>> [d for d in os.listdir('.')]  # os.listdir('.') lists files and directories
  ['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
  ```
- Iterate over key-value pairs in a `dict` and generate a list:
  
  ```python
  >>> d = {'x': 'A', 'y': 'B', 'z': 'C'}
  >>> [k + '=' + v for k, v in d.items()]
  ['y=B', 'x=A', 'z=C']
  ```
- Convert all strings in a list to lowercase:
  
  ```python
  >>> L = ['Hello', 'World', 'IBM', 'Apple']
  >>> [s.lower() for s in L]
  ['hello', 'world', 'ibm', 'apple']
  ```

### `if ... else` in List Comprehensions

Be careful with the placement of `if ... else` in List Comprehensions:

1. **`if` after `for`**: Acts as a **filter** (cannot have `else`—how to filter if there’s an `else`?). Example:
   
   ```python
   >>> [x for x in range(1, 11) if x % 2 == 0]  # Keep even numbers
   [2, 4, 6, 8, 10]
   ```
   
   Adding `else` here causes a syntax error:
   
   ```python
   >>> [x for x in range(1, 11) if x % 2 == 0 else 0]
   File "<stdin>", line 1
       [x for x in range(1, 11) if x % 2 == 0 else 0]
                                              ^
   SyntaxError: invalid syntax
   ```

2. **`if ... else` before `for`**: Acts as an **expression** (must have `else`—the expression must return a value for every `x`). Example:
   
   ```python
   >>> [x if x % 2 == 0 else -x for x in range(1, 11)]
   [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
   ```
   
   Omitting `else` here causes a syntax error:
   
   ```python
   >>> [x if x % 2 == 0 for x in range(1, 11)]
   File "<stdin>", line 1
       [x if x % 2 == 0 for x in range(1, 11)]
                          ^
   SyntaxError: invalid syntax
   ```

### Exercise

If a list contains both strings and integers, calling `lower()` on non-string elements will cause an error. Use the built-in `isinstance()` function to check if a variable is a string, and modify the List Comprehension to run correctly:

```python
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = ???  # Modify this line

# Test case
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('Test success!')
else:
    print('Test failed!')
```

### Summary

List Comprehensions let you quickly generate lists or derive new lists from existing ones with concise code.

## 4. Generators

With List Comprehensions, you can create lists directly. However, lists are limited by memory—storing a list of 1 million elements wastes space if you only need the first few elements.

If list elements can be computed on-the-fly using an algorithm, you can generate elements **during iteration** instead of creating the entire list upfront. This memory-efficient mechanism is called a **generator**.

### Create a Generator

#### Method 1: Replace `[]` with `()` in List Comprehensions

Change the outer brackets of a List Comprehension to parentheses—this creates a generator instead of a list:

```python
>>> L = [x * x for x in range(10)]  # List
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> g = (x * x for x in range(10))  # Generator
>>> g
<generator object <genexpr> at 0x1022ef630>
```

#### Iterate Over a Generator

To retrieve elements from a generator one by one, use the `next()` function (it computes the next element on each call):

```python
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> next(g)
16
>>> next(g)
25
>>> next(g)
36
>>> next(g)
49
>>> next(g)
64
>>> next(g)
81
>>> next(g)  # No more elements—raises StopIteration
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Generators are **iterable**, so the correct way to iterate over them is using a `for` loop (avoids manual `next()` calls and `StopIteration` errors):

```python
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print(n)
...
0
1
4
9
16
25
36
49
64
81
```

#### Method 2: Use Functions with `yield`

For complex algorithms (e.g., the Fibonacci sequence) that can’t be expressed with List Comprehensions, use a **generator function** (a function containing the `yield` keyword).

First, a regular function to print the Fibonacci sequence:

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b  # Equivalent to: t = (b, a + b); a = t[0]; b = t[1]
        n = n + 1
    return 'done'

# Test: Print the first 6 Fibonacci numbers
>>> fib(6)
1
1
2
3
5
8
'done'
```

To convert this to a generator function, replace `print(b)` with `yield b`:

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # Pauses execution and returns b
        a, b = b, a + b
        n = n + 1
    return 'done'
```

A function with `yield` is no longer a regular function—it becomes a generator function. Calling it returns a generator object:

```python
>>> f = fib(6)
>>> f
<generator object fib at 0x104feaaa0>
```

### Execution Flow of Generator Functions

Regular functions execute sequentially and return once (via `return` or reaching the end). Generator functions have a different flow:

1. They execute **only when `next()` is called** (or in a `for` loop).
2. They pause at `yield` and return the value of `yield`.
3. They resume execution from the line after `yield` on the next call.

Example: A generator function that returns 1, 3, 5 sequentially:

```python
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

# Create a generator object
>>> o = odd()
>>> next(o)  # Executes up to first yield
step 1
1
>>> next(o)  # Resumes and executes up to second yield
step 2
3
>>> next(o)  # Resumes and executes up to third yield
step 3
5
>>> next(o)  # No more yields—raises StopIteration
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### Key Note: Multiple Generator Calls

Calling a generator function multiple times creates **independent generators**. For example:

```python
# Wrong: Creates a new generator every time
>>> next(odd())
step 1
1
>>> next(odd())
step 1
1

# Correct: Reuse one generator object
>>> g = odd()
>>> next(g)
step 1
1
>>> next(g)
step 2
3
```

### Retrieve the `return` Value of a Generator

When using a `for` loop to iterate over a generator, you **cannot get the `return` value** (the loop ignores it). To get the `return` value, catch the `StopIteration` error—the value is stored in `e.value`:

```python
>>> g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
...
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
Generator return value: done
```

### Exercise

Yang Hui’s Triangle is defined as follows:

```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
...
```

Treat each row as a list and write a generator to output the next row sequentially:

```python
def triangles():
    pass

# Expected output
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break
for t in results:
    print(t)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('Test success!')
else:
    print('Test failed!')
```

### Summary

Generators are powerful tools. In Python:

- Simple generators can be created by replacing `[]` with `()` in List Comprehensions.
- Complex generators use generator functions with `yield`.
- Generators compute elements on-the-fly (lazy evaluation) and are memory-efficient.
- Regular functions return results directly; generator functions return generator objects.

## 5. Iterators

### What Are Iterable Objects and Iterators?

We already know two types of objects that work with `for` loops:

1. **Collection data types**: `list`, `tuple`, `dict`, `set`, `str`.
2. **Generators**: Including generator expressions and generator functions with `yield`.

These objects are collectively called **iterable objects** (`Iterable`).

Generators have an additional feature: they can be called by the `next()` function to retrieve the next element sequentially until `StopIteration` is raised. Such objects are called **iterators** (`Iterator`).

### Check Iterable Objects and Iterators

Use `isinstance()` to check:

```python
# Check if an object is Iterable
>>> from collections.abc import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False

# Check if an object is Iterator
>>> from collections.abc import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

### Convert Iterable Objects to Iterators

Collections like `list`, `dict`, and `str` are `Iterable` but not `Iterator`. Use the `iter()` function to convert them to `Iterator`:

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

### Why Aren’t `list`/`dict`/`str` Iterators?

An `Iterator` represents a **data stream**. It computes elements on-the-fly (lazy evaluation) via `next()` and raises `StopIteration` when no more elements exist. This allows `Iterator` to represent **infinite data streams** (e.g., all natural numbers), which is impossible for finite collections like `list`.

###本质 of Python’s `for` Loop
Python’s `for` loop is essentially implemented by repeatedly calling `next()`:

```python
# Original for loop
for x in [1, 2, 3, 4, 5]:
    pass

# Equivalent implementation (using Iterator)
it = iter([1, 2, 3, 4, 5])  # Convert list to Iterator
while True:
    try:
        x = next(it)  # Get next element
    except StopIteration:  # Exit loop when no elements remain
        break
```

### Summary

- Objects that work with `for` loops are `Iterable`.
- Objects that work with `next()` are `Iterator`.
- Collections like `list`, `dict`, `str` are `Iterable` but not `Iterator` (convert via `iter()`).
- Python’s `for` loop relies on `Iterator` and `next()`.



## 1. Object-Oriented Programming (OOP)

OOP treats objects as the basic unit of programs. An object contains **data** (attributes) and **operations on data** (methods). Unlike procedural programming (which focuses on function execution order), OOP models programs as interactions between objects.

### 1.1 Classes and Instances

A **class** is an abstract template (e.g., `Student`), and an **instance** is a concrete object created from the class (e.g., `bart = Student('Bart Simpson', 59)`).

#### Define a Class

Use the `class` keyword, with the class name typically starting with an uppercase letter. The `object` in parentheses indicates inheritance from Python’s base `object` class (all classes eventually inherit from `object`).

```python
class Student(object):
    pass
```

#### Create an Instance

Call the class name with `()` (like a function) to create an instance:

```python
>>> bart = Student()
>>> bart
<__main__.Student object at 0x10a67a590>  # Memory address (unique for each instance)
>>> Student  # Class itself is a type
<class '__main__.Student'>
```

#### Bind Attributes to Instances

You can dynamically bind attributes to an instance (a Python-specific flexibility):

```python
>>> bart.name = 'Bart Simpson'  # Bind 'name' attribute to bart
>>> bart.name
'Bart Simpson'
```

#### Force Attribute Binding with `__init__`

To enforce binding of essential attributes (e.g., `name` and `score` for `Student`) during instance creation, define the special `__init__` method (double underscores before/after):

```python
class Student(object):
    # self: mandatory first parameter, refers to the instance itself
    def __init__(self, name, score):
        self.name = name  # Bind 'name' to the instance
        self.score = score  # Bind 'score' to the instance
```

- When creating an instance, pass parameters matching `__init__` (exclude `self`—Python passes it automatically):
  
  ```python
  >>> bart = Student('Bart Simpson', 59)
  >>> bart.name  # Access attribute
  'Bart Simpson'
  >>> bart.score
  59
  ```

### 1.2 Data Encapsulation

Encapsulation hides internal data and logic, allowing external code to interact with objects via methods (instead of directly accessing attributes).

#### Example: Encapsulate Score Printing

Instead of using an external function to print scores, define a `print_score` method inside the `Student` class:

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # Method: operates on the instance's data
    def print_score(self):
        print(f"{self.name}: {self.score}")

# Call the method on the instance
>>> bart = Student('Bart Simpson', 59)
>>> bart.print_score()
Bart Simpson: 59
```

#### Add New Methods

Extend the class with methods like `get_grade` to calculate grades:

```python
class Student(object):
    # ... (existing __init__ and print_score)
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

# Use the new method
>>> lisa = Student('Lisa', 99)
>>> lisa.get_grade()
'A'
```

### 1.3 Access Control

By default, external code can modify an instance’s attributes (e.g., `bart.score = 99`). To restrict external access, prefix attribute names with **double underscores (`__`)**—this makes them "private" (only accessible internally).

#### Define Private Attributes

```python
class Student(object):
    def __init__(self, name, score):
        self.__name = name  # Private attribute: __name
        self.__score = score  # Private attribute: __score

    def print_score(self):
        # Internal access to private attributes is allowed
        print(f"{self.__name}: {self.__score}")
```

- External access to private attributes will fail:
  
  ```python
  >>> bart = Student('Bart Simpson', 59)
  >>> bart.__name  # Error: no public attribute '__name'
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  AttributeError: 'Student' object has no attribute '__name'
  ```

#### Get/Set Private Attributes

To allow controlled external access/modification, add `get_xxx` (for reading) and `set_xxx` (for writing) methods:

```python
class Student(object):
    # ... (existing __init__)

    # Get private attribute __name
    def get_name(self):
        return self.__name

    # Get private attribute __score
    def get_score(self):
        return self.__score

    # Set private attribute __score (with validation)
    def set_score(self, score):
        if 0 <= score <= 100:  # Prevent invalid scores (e.g., 999)
            self.__score = score
        else:
            raise ValueError('Score must be between 0 and 100!')

# Use get/set methods
>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.set_score(88)  # Valid modification
>>> bart.get_score()
88
>>> bart.set_score(101)  # Invalid: raises ValueError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Score must be between 0 and 100!
```

#### Key Notes on Access Control

- **Special variables**: Names like `__xxx__` (e.g., `__name__`, `__doc__`) are public (not private) and have special purposes—avoid using this format for custom attributes.
- **Single underscore (`_xxx`)**: By convention, these are "protected" (external access is allowed but discouraged).
- **Private attribute "hacking"**: Python renames `__name` to `_Student__name` internally (to prevent conflicts). External code can access it via `bart._Student__name`, but this is strongly discouraged (version-dependent).

### 1.4 Inheritance and Polymorphism

#### Inheritance

A **subclass** inherits all features of its **base class** (parent class) and can add new methods or override existing ones.

##### Example: Animal Hierarchy

```python
# Base class
class Animal(object):
    def run(self):
        print('Animal is running...')

# Subclass 1: inherits from Animal
class Dog(Animal):
    # Override the run() method of the base class
    def run(self):
        print('Dog is running...')

    # Add new method
    def eat(self):
        print('Eating meat...')

# Subclass 2: inherits from Animal
class Cat(Animal):
    # Override run()
    def run(self):
        print('Cat is running...')
```

- Subclasses inherit base class methods (e.g., `Dog` and `Cat` use `Animal`’s `run()` if not overridden).
- Overridden methods in subclasses take priority:
  
  ```python
  >>> dog = Dog()
  >>> dog.run()  # Calls Dog's run() (not Animal's)
  Dog is running...
  >>> dog.eat()  # Calls Dog's new method
  Eating meat...
  ```

#### Polymorphism

Polymorphism allows a subclass instance to be treated as a base class instance. It enables flexible code that works with all subclasses of a base class.

##### Example: Polymorphic Function

Define a function `run_twice` that accepts an `Animal` (or its subclass) and calls `run()` twice:

```python
def run_twice(animal):
    animal.run()
    animal.run()

# Test with different types
>>> run_twice(Animal())  # Base class instance
Animal is running...
Animal is running...

>>> run_twice(Dog())  # Subclass instance (treated as Animal)
Dog is running...
Dog is running...

>>> run_twice(Cat())  # Another subclass instance
Cat is running...
Cat is running...
```

##### Benefits of Polymorphism

- **Open/Closed Principle**: Add new subclasses (e.g., `Tortoise(Animal)`) without modifying existing code (e.g., `run_twice`):
  
  ```python
  class Tortoise(Animal):
      def run(self):
          print('Tortoise is running slowly...')
  
  >>> run_twice(Tortoise())  # Works without changing run_twice
  Tortoise is running slowly...
  Tortoise is running slowly...
  ```

#### Type Checking with `isinstance`

Use `isinstance()` to verify if an instance belongs to a class or its subclass:

```python
>>> dog = Dog()
>>> isinstance(dog, Dog)  # dog is a Dog instance
True
>>> isinstance(dog, Animal)  # dog is also an Animal instance (inheritance)
True
>>> isinstance(Animal(), Dog)  # Animal is not a Dog (reverse is false)
False
```

### 1.5 Get Object Information

Use built-in functions to inspect an object’s type, attributes, and methods.

#### 1. `type()`: Check Object Type

```python
# Check basic types
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<class 'NoneType'>

# Check functions/classes
>>> type(abs)  # Built-in function
<class 'builtin_function_or_method'>
>>> class Animal(object): pass
>>> type(Animal())  # Instance of custom class
<class '__main__.Animal'>
```

#### 2. `isinstance()`: Check Inheritance Relationship

As shown earlier, `isinstance()` recognizes subclass instances as base class instances. It also supports checking against multiple types:

```python
# Check if x is list OR tuple
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True
```

#### 3. `dir()`: List Attributes and Methods

`dir(obj)` returns a list of all attributes/methods of `obj` (including special methods like `__len__`):

```python
>>> dir('ABC')  # Attributes/methods of string
['__add__', '__class__', ..., 'capitalize', 'lower', 'zfill']
```

#### 4. `getattr()`, `setattr()`, `hasattr()`: Manipulate Attributes Dynamically

- `hasattr(obj, 'attr')`: Check if `obj` has attribute `attr`.
- `getattr(obj, 'attr')`: Get the value of `attr` (raises `AttributeError` if missing).
- `setattr(obj, 'attr', value)`: Set the value of `attr`.

```python
class MyObject(object):
    def __init__(self):
        self.x = 9  # Instance attribute

    def power(self):
        return self.x * self.x

# Create instance
>>> obj = MyObject()

# Check/modify attributes
>>> hasattr(obj, 'x')  # Does obj have 'x'?
True
>>> obj.x
9
>>> hasattr(obj, 'y')  # Does obj have 'y'?
False
>>> setattr(obj, 'y', 19)  # Add 'y' attribute
>>> hasattr(obj, 'y')
True
>>> getattr(obj, 'y')
19

# Get non-existent attribute with default value
>>> getattr(obj, 'z', 404)  # Return 404 if 'z' is missing
404

# Get and call methods
>>> hasattr(obj, 'power')  # Does obj have 'power' method?
True
>>> fn = getattr(obj, 'power')  # Get the method
>>> fn()  # Call the method (same as obj.power())
81
```

### 1.6 Instance Attributes vs. Class Attributes

- **Instance attributes**: Belong to individual instances (unique for each instance).
- **Class attributes**: Belong to the class (shared by all instances of the class).

#### Example: Class Attribute

Define a `name` class attribute for `Student`:

```python
class Student(object):
    name = 'Student'  # Class attribute (shared by all instances)

# Create instances
>>> s1 = Student()
>>> s2 = Student()

# Access class attribute via instances (no instance attribute overrides it)
>>> s1.name  # s1 has no 'name' instance attribute → uses class attribute
'Student'
>>> s2.name
'Student'

# Access class attribute via the class
>>> Student.name
'Student'

# Bind instance attribute (hides class attribute)
>>> s1.name = 'Michael'  # s1 now has an instance attribute 'name'
>>> s1.name  # Instance attribute takes priority
'Michael'
>>> s2.name  # s2 still uses class attribute
'Student'

# Delete instance attribute (restores class attribute access)
>>> del s1.name
>>> s1.name
'Student'
```

#### Warning

Never use the same name for instance attributes and class attributes—this causes unexpected behavior (instance attributes override class attributes).

## 2. Advanced OOP Features

### 2.1 Use `__slots__` to Restrict Attributes

Python allows dynamic binding of attributes/methods to instances. To restrict which attributes an instance can have, define a special `__slots__` variable (a tuple of allowed attribute names) in the class.

#### Example: Restrict Attributes with `__slots__`

```python
class Student(object):
    # Allow only 'name' and 'age' attributes
    __slots__ = ('name', 'age')

# Test
>>> s = Student()
>>> s.name = 'Michael'  # Allowed
>>> s.age = 25  # Allowed
>>> s.score = 99  # Disallowed: no 'score' in __slots__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
```

#### Key Notes on `__slots__`

- `__slots__` only applies to the **current class**—it does not affect subclasses.

- Subclasses can define their own `__slots__` (combines with parent class `__slots__`):
  
  ```python
  class GraduateStudent(Student):
      __slots__ = ('score',)  # Add 'score' to allowed attributes
  
  >>> g = GraduateStudent()
  >>> g.score = 99  # Allowed (subclass __slots__)
  >>> g.name = 'Bob'  # Allowed (parent class __slots__)
  ```

### 2.2 Use `@property` for Controlled Attribute Access

`@property` is a decorator that converts a method into a "property" (accessed like an attribute, not a method). It enables parameter validation while keeping syntax simple.

#### Example: Convert Methods to Properties

```python
class Student(object):
    # Getter: @property + method → becomes a read-only property
    @property
    def score(self):
        return self._score  # Use _score (convention for "protected" attributes)

    # Setter: @<property_name>.setter + method → enables writing to the property
    @score.setter
    def score(self, value):
        # Validate parameter
        if not isinstance(value, int):
            raise ValueError('Score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('Score must be between 0 and 100!')
        self._score = value

# Use the property (no parentheses for method calls)
>>> s = Student()
>>> s.score = 60  # Calls score.setter (valid)
>>> s.score  # Calls score.getter → returns 60
60
>>> s.score = 999  # Invalid: raises ValueError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Score must be between 0 and 100!
```

#### Read-Only Properties

Omit the setter to create a read-only property (only `@property` is defined):

```python
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # Read-only property (no setter)
    @property
    def age(self):
        return 2025 - self._birth  # Calculated dynamically

>>> s = Student()
>>> s.birth = 2000  # Allowed (has setter)
>>> s.age  # Read-only: returns 25 (2025-2000)
25
>>> s.age = 26  # Error: no setter for 'age'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
```

#### Warning

Never use the same name for the property method and the instance attribute (e.g., `def birth(self): return self.birth`). This causes infinite recursion (calling `s.birth` triggers the method, which calls `self.birth` again).

### 2.3 Multiple Inheritance

Python supports multiple inheritance— a subclass can inherit from multiple base classes. This is useful for "mixing in" additional features (via **MixIn classes**).

#### Example: MixIn Design

Suppose we need to model animals with "runnable" and "flyable" features. Instead of deep inheritance hierarchies, use MixIn classes to combine functionalities:

```python
# Base class
class Animal(object):
    pass

# MixIn classes (add specific features)
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

# Subclasses: inherit from base class + MixIns
class Dog(Animal, RunnableMixIn):  # Dog → Animal + Runnable
    pass

class Bat(Animal, FlyableMixIn):  # Bat → Animal + Flyable
    pass

# Test
>>> dog = Dog()
>>> dog.run()  # Inherited from RunnableMixIn
Running...

>>> bat = Bat()
>>> bat.fly()  # Inherited from FlyableMixIn
Flying...
```

#### MixIn Naming Convention

Name MixIn classes with a `MixIn` suffix (e.g., `RunnableMixIn`, `FlyableMixIn`) to clarify their purpose (adding features, not core inheritance).

### 2.4 Customize Classes with Special Methods

Python allows customizing class behavior via special methods (named with `__xxx__`). These methods enable classes to behave like built-in types (e.g., `list`, `dict`).

#### 1. `__str__`: Pretty-Print Instances

`__str__` defines the string representation of an instance (for users).

```python
class Student(object):
    def __init__(self, name):
        self.name = name

    # Customize print output
    def __str__(self):
        return f"Student object (name: {self.name})"

>>> print(Student('Michael'))  # Uses __str__
Student object (name: Michael)
```

#### 2. `__repr__`: Debug-Friendly Representation

`__repr__` defines the string representation for developers (used when directly referencing the instance, not `print`). To avoid redundancy, assign `__repr__ = __str__`:

```python
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student object (name: {self.name})"

    __repr__ = __str__  # Reuse __str__ for __repr__

>>> s = Student('Michael')
>>> s  # Uses __repr__ (now same as __str__)
Student object (name: Michael)
```

#### 3. `__iter__`: Support `for` Loops

To make a class iterable (work with `for ... in`), define `__iter__` (returns an iterator) and `__next__` (returns the next element, raises `StopIteration` when done).

##### Example: Fibonacci Sequence Generator

```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # Initialize counters

    # Return self as the iterator
    def __iter__(self):
        return self

    # Return next element (called by for loop)
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # Update values
        if self.a > 100000:  # Stop condition
            raise StopIteration()
        return self.a

# Iterate with for loop
>>> for n in Fib():
...     print(n)
1
1
2
3
5
...  # Stops when a > 100000
```

#### 4. `__getitem__`: Support Indexing/Slicing

To make a class support indexing (like `list[0]`) or slicing (like `list[1:3]`), define `__getitem__`.

##### Example: Indexing for Fib Class

```python
class Fib(object):
    # ... (existing __init__ and __iter__)

    def __getitem__(self, n):
        if isinstance(n, int):  # n is an index
            a, b = 1, 1
            for _ in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):  # n is a slice (e.g., 1:3)
            start = n.start if n.start is not None else 0
            stop = n.stop
            a, b = 1, 1
            result = []
            for i in range(stop):
                if i >= start:
                    result.append(a)
                a, b = b, a + b
            return result

# Test indexing and slicing
>>> f = Fib()
>>> f[0]  # Index 0
1
>>> f[10]  # Index 10
89
>>> f[0:5]  # Slice 0-4
[1, 1, 2, 3, 5]
```

#### 5. `__getattr__`: Dynamic Attribute Access

`__getattr__` is called when accessing a non-existent attribute. It enables dynamic attribute generation.

##### Example: Dynamic Score Attribute

```python
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    # Return value for non-existent attributes
    def __getattr__(self, attr):
        if attr == 'score':
            return 99  # Dynamic 'score' attribute
        # Raise error for other non-existent attributes
        raise AttributeError(f"'Student' object has no attribute '{attr}'")

>>> s = Student()
>>> s.name  # Exists → no __getattr__
'Michael'
>>> s.score  # Does not exist → __getattr__ returns 99
99
>>> s.age  # Does not exist → __getattr__ raises error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
```

##### Practical Use: Dynamic API Calls

Use `__getattr__` to implement chainable API calls (e.g., for REST APIs):

```python
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        # Return new Chain instance with updated path
        return Chain(f"{self._path}/{path}")

    def __str__(self):
        return self._path

    __repr__ = __str__

# Chainable calls
>>> Chain().status.user.timeline.list
'/status/user/timeline/list'
```

#### 6. `__call__`: Call Instances Like Functions

Define `__call__` to allow calling an instance directly (like a function).

##### Example: Callable Student Instance

```python
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"My name is {self.name}.")

# Call the instance
>>> s = Student('Michael')
>>> s()  # Equivalent to s.__call__()
My name is Michael.
```

##### Check Callability

Use `callable()` to check if an object is callable (functions, instances with `__call__`, etc.):

```python
>>> callable(Student())  # Instance with __call__
True
>>> callable(max)  # Built-in function
True
>>> callable([1, 2, 3])  # List (not callable)
False
```

### 2.5 Use Enumeration Classes

To define a set of related constants (e.g., months, weekdays), use Python’s `Enum` class (from the `enum` module) instead of plain integers. This ensures type safety and readability.

#### Example: Basic Enumeration

```python
from enum import Enum

# Define Month enum (names: Jan-Dec; values: 1-12 auto-assigned)
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# Iterate over enum members
for name, member in Month.__members__.items():
    print(f"{name} → {member}, {member.value}")  # value: auto-incrementing int
```

#### Custom Enumeration with `unique`

Use the `@unique` decorator to ensure no duplicate values:

```python
from enum import Enum, unique

@unique  # Prevents duplicate values
class Weekday(Enum):
    Sun = 0  # Custom value (not auto-assigned)
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# Access enum members
>>> Weekday.Mon  # By name
<Weekday.Mon: 1>
>>> Weekday['Tue']  # By name string
<Weekday.Tue: 2>
>>> Weekday(3)  # By value
<Weekday.Wed: 3>
>>> Weekday.Mon.value  # Get value
1

# Compare enum members
>>> Weekday.Mon == Weekday.Tue
False
>>> Weekday.Mon == Weekday(1)
True
```

### 2.6 Use Metaclasses

A **metaclass** is the "class of a class"—it controls how classes are created or modified. Metaclasses are advanced and rarely used, but they are powerful for frameworks (e.g., ORMs).

#### 1. `type()`: Create Classes Dynamically

`type()` can create classes at runtime (in addition to checking types). It takes three arguments:

1. Class name (string).
2. Tuple of base classes (inheritance).
3. Dictionary of class attributes/methods.

##### Example: Dynamic Class Creation

```python
# Step 1: Define a function (will be a class method)
def fn(self, name='world'):
    print(f"Hello, {name}.")

# Step 2: Create Hello class via type()
Hello = type('Hello', (object,), dict(hello=fn))  # hello: method name → fn

# Use the dynamically created class
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> type(Hello)  # Hello's type is type (metaclass)
<class 'type'>
```

#### 2. Custom Metaclasses

Define a custom metaclass by inheriting from `type` and overriding `__new__` (called when creating a class).

##### Example: Add `add` Method to `MyList`

```python
# Custom metaclass (inherits from type)
class ListMetaclass(type):
    # __new__: creates the class object
    def __new__(cls, name, bases, attrs):
        # Add 'add' method to the class
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# Use the metaclass to create MyList
class MyList(list, metaclass=ListMetaclass):
    pass

# Test: MyList has add() method (list does not)
>>> L = MyList()
>>> L.add(1)
>>> L
[1]

>>> L2 = list()
>>> L2.add(1)  # Error: list has no add()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'add'
```

##### Practical Use: ORM Framework

Metaclasses are used in ORMs (Object-Relational Mapping) to map classes to database tables dynamically. For example:

```python
# Step 1: Define Field class (maps to database columns)
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

# Step 2: Define specific field types
class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')

# Step 3: Custom metaclass for ORM
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':  # Skip base class
            return type.__new__(cls, name, bases, attrs)
        mappings = {}
        # Collect Field attributes
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                attrs.pop(k)  # Remove Field from class attributes
        attrs['__mappings__'] = mappings  # Store column mappings
        attrs['__table__'] = name  # Table name = class name
        return type.__new__(cls, name, bases, attrs)

# Step 4: Base Model class (uses the metaclass)
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Model' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        self[key] = value

    # Save instance to database (generates SQL)
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = f"insert into {self.__table__} ({','.join(fields)}) values ({','.join(params)})"
        print(f"SQL: {sql}")
        print(f"ARGS: {args}")

# Step 5: Define User class (maps to User table)
class User(Model):
    # Class attributes → database columns
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# Test: Save User instance
>>> u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
>>> u.save()
SQL: insert into User (id, name, email, password) values (?, ?, ?, ?)
ARGS: [12345, 'Michael', 'test@orm.org', 'my-pwd']
```
