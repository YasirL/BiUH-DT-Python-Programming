# Python Tutorial (Liao Xuefeng) - Pages 26-102
Translated with Code Examples for GitHub


## 1. Python Basics
This section covers core foundational concepts of Python, including data types, string handling, common data structures (list/tuple/dict/set), conditional logic, loops, and pattern matching.


### 1.1 Data Types and Variables
Python supports multiple built-in data types for storing different kinds of data. Variables act as references to these data objects.

#### 1.1.1 Integers (`int`)
Python supports integers of any size (positive, negative, or zero). Hexadecimal integers are prefixed with `0x`, and underscores (`_`) can be used to improve readability of large integers.

```python
# Decimal integer
a = 100
print(a)  # Output: 100

# Negative integer
b = -8080
print(b)  # Output: -8080

# Hexadecimal integer (0x prefix)
c = 0xff00
print(c)  # Output: 65280

# Large integer with underscores (enhances readability)
d = 10_000_000_000
print(d)  # Output: 10000000000
```

#### 1.1.2 Floating-Point Numbers (`float`)
Floating-point numbers (decimals) can be written in standard or scientific notation (using `e` for powers of 10). Note that floating-point operations may have rounding errors.

```python
# Standard floating-point
a = 3.14
print(a)  # Output: 3.14

# Negative floating-point
b = -9.01
print(b)  # Output: -9.01

# Scientific notation (1.23 × 10^9)
c = 1.23e9
print(c)  # Output: 1230000000.0

# Small floating-point (1.2 × 10^-5)
d = 1.2e-5
print(d)  # Output: 1.2e-05
```

#### 1.1.3 Strings (`str`)
Strings are sequences of characters enclosed in single quotes (`'`), double quotes (`"`), or triple quotes (`'''`/`"""`) for multi-line text. Escape characters (e.g., `\n`, `\t`) handle special formatting.

```python
# Single quotes (supports apostrophes with escape)
a = 'I\'m OK'
print(a)  # Output: I'm OK

# Double quotes
b = "Hello, world"
print(b)  # Output: Hello, world

# Multi-line string (triple quotes)
c = '''Line 1
Line 2
Line 3'''
print(c)
# Output:
# Line 1
# Line 2
# Line 3

# Escape characters: \n (newline), \t (tab), \\ (backslash)
d = 'Hello\nPython\tWorld'
print(d)
# Output:
# Hello
# Python	World

# Raw string (disables escape, prefixed with r)
e = r'C:\Users\Name'
print(e)  # Output: C:\Users\Name
```

#### 1.1.4 Booleans (`bool`)
Booleans represent logical values: `True` (1) or `False` (0). They support `and` (conjunction), `or` (disjunction), and `not` (negation) operations.

```python
# Boolean values
a = True
b = False
print(a)  # Output: True
print(int(a))  # Output: 1 (True → 1)
print(int(b))  # Output: 0 (False → 0)

# Logical operations
print(a and b)  # Output: False (both must be True)
print(a or b)   # Output: True (at least one True)
print(not a)    # Output: False (negation)

# Boolean comparisons
print(3 > 2)  # Output: True
print(3 == 2) # Output: False
```

#### 1.1.5 None Value
`None` is a special value representing "empty" or "no value". It is not equivalent to `0` or empty strings.

```python
a = None
print(a)  # Output: None
print(a == 0)  # Output: False
print(a == '') # Output: False
```

#### 1.1.6 Variables
Variables store references to data objects. They are defined with `=`, and can be reassigned to different data types (dynamic typing).

```python
# Define a variable (integer)
x = 10
print(x)  # Output: 10

# Reassign to a string (dynamic typing)
x = 'Hello'
print(x)  # Output: Hello

# Assign multiple variables at once
a, b, c = 1, 2.5, 'Python'
print(a, b, c)  # Output: 1 2.5 Python
```

#### 1.1.7 Constants
Constants are "unchangeable variables" (by convention, use ALL_UPPERCASE names). Python does not enforce immutability, so this is a coding practice.

```python
# Constant (convention: ALL_UPPERCASE)
PI = 3.14159265359
print(PI * 2)  # Output: 6.28318530718

# Warning: Python allows reassigning constants (not recommended)
PI = 3.14
print(PI)  # Output: 3.14
```


### 1.2 Strings and Encoding
Character encoding ensures text is stored/transmitted correctly. Key encodings: ASCII (1-byte, English), Unicode (2-byte, global), and UTF-8 (variable-byte, space-efficient).

#### 1.2.1 Character Encoding Basics
- **ASCII**: Only supports English (1 byte, 0-127).  
- **Unicode**: Supports all languages (2 bytes for common characters).  
- **UTF-8**: A variable-length encoding (1 byte for English, 3 bytes for Chinese), widely used for files/websites.

#### 1.2.2 String Encoding/Decoding
- `ord(c)`: Get the Unicode code of a single character.  
- `chr(code)`: Convert a Unicode code to a character.  
- `str.encode(encoding)`: Convert string to `bytes` (for storage/transmission).  
- `bytes.decode(encoding)`: Convert `bytes` back to string.

```python
# Get Unicode code (ord())
print(ord('A'))  # Output: 65
print(ord('中')) # Output: 20013

# Convert code to character (chr())
print(chr(66))   # Output: B
print(chr(25991))# Output: 文

# Encode string to bytes (UTF-8)
s = '中文'
b = s.encode('utf-8')
print(b)  # Output: b'\xe4\xb8\xad\xe6\x96\x87'

# Decode bytes to string
print(b.decode('utf-8'))  # Output: 中文

# Handle decoding errors (ignore invalid bytes)
b_invalid = b'\xe4\xb8\xad\xff'
print(b_invalid.decode('utf-8', errors='ignore'))  # Output: 中
```

#### 1.2.3 String Formatting
Three common ways to format strings:

##### 1. `%` Operator
Use placeholders like `%s` (string), `%d` (integer), `%.2f` (float with 2 decimals).

```python
# Format string with %
print('Hello, %s' % 'World')          # Output: Hello, World
print('Age: %d, Score: %.2f' % (25, 98.5))  # Output: Age: 25, Score: 98.50
print('Growth rate: %d %%' % 7)       # Output: Growth rate: 7 % (%% for literal %)
```

##### 2. `str.format()` Method
Use `{0}`, `{1}` (positional) or `{name}` (keyword) placeholders.

```python
# Positional formatting
print('Hello, {0}! Score: {1:.1f}'.format('Alice', 97.5))  # Output: Hello, Alice! Score: 97.5

# Keyword formatting
print('Name: {name}, Age: {age}'.format(name='Bob', age=22))  # Output: Name: Bob, Age: 22
```

##### 3. F-Strings (Python 3.6+)
Prefix the string with `f` and use `{variable}` for direct substitution.

```python
name = 'Charlie'
age = 20
print(f'Name: {name}, Age next year: {age + 1}')  # Output: Name: Charlie, Age next year: 21

# Format float (2 decimals)
pi = 3.14159
print(f'Pi: {pi:.2f}')  # Output: Pi: 3.14
```


### 1.3 Using `list` and `tuple`
#### 1.3.1 `list`: Mutable Ordered Collection
A `list` is a dynamic, ordered collection that allows adding/removing/modifying elements.

##### Basic Operations
```python
# Define a list
fruits = ['apple', 'banana', 'cherry']
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Access elements by index (0-based)
print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: cherry (last element)

# Modify elements
fruits[1] = 'orange'
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# Add elements to the end
fruits.append('date')
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'date']

# Insert element at index 1
fruits.insert(1, 'grape')
print(fruits)  # Output: ['apple', 'grape', 'orange', 'cherry', 'date']

# Remove last element (returns the removed element)
last = fruits.pop()
print(last)    # Output: date
print(fruits)  # Output: ['apple', 'grape', 'orange', 'cherry']

# Remove element at index 2
fruits.pop(2)
print(fruits)  # Output: ['apple', 'grape', 'cherry']
```

##### Nested Lists
A `list` can contain other `list`s (2D/3D "arrays").

```python
# Nested list (2D)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1])  # Output: 2 (1st row, 2nd element)

# Flatten the matrix
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 1.3.2 `tuple`: Immutable Ordered Collection
A `tuple` is similar to `list`, but **cannot be modified after creation** (safer for fixed data).

##### Basic Operations
```python
# Define a tuple
colors = ('red', 'green', 'blue')
print(colors)  # Output: ('red', 'green', 'blue')

# Access elements (same as list)
print(colors[1])   # Output: green
print(colors[-1])  # Output: blue

# Error: Cannot modify tuple elements
# colors[0] = 'yellow'  # Raises TypeError: 'tuple' object does not support item assignment
```

##### Single-Element `tuple`
Add a trailing comma (`,`) to avoid ambiguity with parentheses in math expressions.

```python
# Single-element tuple (must add comma)
a = (1,)
print(type(a))  # Output: <class 'tuple'>

# Without comma: treated as integer
b = (1)
print(type(b))  # Output: <class 'int'>
```

##### "Mutable" `tuple` (with Mutable Elements)
If a `tuple` contains mutable objects (e.g., `list`), the internal objects can be modified (but the `tuple`’s structure remains fixed).

```python
# Tuple with a list (mutable element)
t = ('a', 'b', ['X', 'Y'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)  # Output: ('a', 'b', ['X', 'Y'])

# Error: Cannot replace the list itself
# t[2] = ['A', 'B']  # Raises TypeError
```


### 1.4 Conditional Judgment
Use `if-elif-else` to implement conditional logic. Python uses **indentation** (4 spaces) to define code blocks.

#### 1.4.1 Basic `if` Statement
Execute code only if the condition is `True`.

```python
age = 18
if age >= 18:
    print('Adult')  # Output: Adult
```

#### 1.4.2 `if-else` Statement
Execute one block if the condition is `True`, another if `False`.

```python
age = 15
if age >= 18:
    print('Adult')
else:
    print('Teenager')  # Output: Teenager
```

#### 1.4.3 `if-elif-else` Statement
Handle multiple conditions (checks from top to bottom; stops at the first `True` condition).

```python
score = 85
if score >= 90:
    print('Grade A')
elif score >= 80:
    print('Grade B')  # Output: Grade B
elif score >= 60:
    print('Grade C')
else:
    print('Grade F')
```

#### 1.4.4 Simplified Condition Check
A condition is `True` if it is a non-zero number, non-empty string/list/dict, etc.

```python
# Non-empty string → True
s = 'Hello'
if s:
    print('String is not empty')  # Output: String is not empty

# Empty list → False
L = []
if L:
    print('List is not empty')
else:
    print('List is empty')  # Output: List is empty
```

#### 1.4.5 Handling User Input with `input()`
`input()` reads user input as a `string`; convert to other types (e.g., `int`) if needed.

```python
# Get user input (returns string)
birth_year = input('Enter your birth year: ')
birth_year = int(birth_year)  # Convert to integer

if 2024 - birth_year >= 18:
    print('You are an adult')
else:
    print('You are a minor')

# Example output:
# Enter your birth year: 2005
# You are a minor
```


### 1.5 Pattern Matching (`match` Statement)
The `match` statement (Python 3.10+) simplifies multi-condition checks by matching a variable against patterns.

#### 1.5.1 Basic `match-case` Matching
Use `case` to match specific values; `_` matches any other value.

```python
score = 'B'
match score:
    case 'A':
        print('Excellent')
    case 'B':
        print('Good')  # Output: Good
    case 'C':
        print('Pass')
    case _:
        print('Fail')
```

#### 1.5.2 Complex Matching (Ranges, Multiple Values)
Match ranges or multiple values with `|` (OR).

```python
age = 15
match age:
    case x if x < 10:
        print(f'Child (age {x})')
    case 10:
        print('10 years old')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('Teenager')  # Output: Teenager
    case _:
        print('Adult')
```

#### 1.5.3 List Matching
Match lists of specific lengths or structures.

```python
args = ['gcc', 'hello.c', 'world.c']
match args:
    case ['gcc']:
        print('gcc: missing source files')
    case ['gcc', file1, *files]:
        print(f'Compile: {file1}, {", ".join(files)}')  # Output: Compile: hello.c, world.c
    case ['clean']:
        print('Cleaning project')
    case _:
        print('Invalid command')
```


### 1.6 Loops
Loops repeat code blocks. Python supports `for-in` (iterating over collections) and `while` (loop while a condition is `True`).

#### 1.6.1 `for-in` Loop
Iterate over `list`, `tuple`, `string`, or other iterable objects.

```python
# Iterate over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Iterate over a string
for char in 'Python':
    print(char, end=' ')  # Output: P y t h o n 

# Iterate over a range (0-9, exclusive of 10)
sum = 0
for x in range(10):
    sum += x
print('\nSum:', sum)  # Output: Sum: 45
```

#### 1.6.2 `while` Loop
Run code as long as the condition is `True`.

```python
# Calculate sum of odd numbers < 100
sum_odd = 0
n = 99
while n > 0:
    sum_odd += n
    n -= 2
print('Sum of odds < 100:', sum_odd)  # Output: Sum of odds < 100: 2500
```

#### 1.6.3 `break` Statement
Exit the loop early.

```python
# Print numbers 1-10, then exit
n = 1
while n <= 100:
    if n > 10:
        break  # Exit loop when n > 10
    print(n)
    n += 1
# Output: 1 2 3 4 5 6 7 8 9 10
```

#### 1.6.4 `continue` Statement
Skip the current iteration and start the next.

```python
# Print only odd numbers
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # Skip even numbers
    print(n)
# Output: 1 3 5 7 9
```


### 1.7 Using `dict` and `set`
#### 1.7.1 `dict`: Key-Value Mapping
A `dict` (dictionary) stores key-value pairs for fast lookups (O(1) time complexity). Keys must be **immutable** (e.g., `str`, `int`, `tuple`).

##### Basic Operations
```python
# Define a dict
student = {'name': 'Alice', 'age': 20, 'score': 95}
print(student)  # Output: {'name': 'Alice', 'age': 20, 'score': 95}

# Access value by key
print(student['name'])  # Output: Alice

# Add new key-value pair
student['gender'] = 'Female'
print(student)  # Output: {'name': 'Alice', 'age': 20, 'score': 95, 'gender': 'Female'}

# Modify value
student['score'] = 98
print(student['score'])  # Output: 98

# Check if key exists
print('age' in student)  # Output: True
print('grade' in student)  # Output: False

# Safe lookup with get() (returns None if key not found)
print(student.get('grade', 'N/A'))  # Output: N/A

# Delete key-value pair
student.pop('gender')
print(student)  # Output: {'name': 'Alice', 'age': 20, 'score': 98}
```

##### Key Immutability
Keys cannot be mutable (e.g., `list`), as mutable objects cannot be hashed.

```python
# Valid: key is a tuple (immutable)
d = {(1, 2): 'point'}
print(d[(1, 2)])  # Output: point

# Error: key is a list (mutable)
# d = {[1, 2]: 'list'}  # Raises TypeError: unhashable type: 'list'
```

#### 1.7.2 `set`: Unordered Unique Collection
A `set` stores unique, unordered elements (no duplicates). It supports mathematical operations like intersection and union.

##### Basic Operations
```python
# Define a set (from a list)
s = set([1, 2, 2, 3])
print(s)  # Output: {1, 2, 3} (duplicates removed)

# Add element
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

# Add duplicate (no effect)
s.add(2)
print(s)  # Output: {1, 2, 3, 4}

# Remove element
s.remove(3)
print(s)  # Output: {1, 2, 4}
```

##### Mathematical Operations
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}

# Intersection (common elements)
print(s1 & s2)  # Output: {2, 3}

# Union (all unique elements)
print(s1 | s2)  # Output: {1, 2, 3, 4}

# Difference (elements in s1 not in s2)
print(s1 - s2)  # Output: {1}
```


## 2. Functions
Functions encapsulate reusable code. Python supports defining custom functions, handling parameters flexibly, and recursive calls.


### 2.1 Calling Functions
#### 2.1.1 Built-in Functions
Python provides many built-in functions (e.g., `abs()`, `max()`, `int()`) that can be called directly.

```python
# Calculate absolute value
print(abs(-10))  # Output: 10

# Find maximum value
print(max(1, 3, -5, 7))  # Output: 7

# Type conversion
print(int('123'))    # Output: 123 (string → int)
print(float(123))    # Output: 123.0 (int → float)
print(str(123.45))   # Output: '123.45' (float → string)
print(bool(0))       # Output: False (int → bool)
```

#### 2.1.2 Function Aliases
Assign a function to a variable to create an alias.

```python
# Alias for abs()
f = abs
print(f(-5))  # Output: 5
```


### 2.2 Defining Functions
Use the `def` keyword to define a function, followed by the function name, parameters, and code block (indented).

#### 2.2.1 Basic Function Definition
```python
# Define a function to calculate absolute value
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

# Call the function
print(my_abs(-99))  # Output: 99
```

#### 2.2.2 Empty Function with `pass`
Use `pass` as a placeholder for functions with unimplemented logic.

```python
# Empty function (to be implemented later)
def empty_func():
    pass  # No error; acts as a placeholder

# Use pass in conditional statements
age = 18
if age >= 18:
    pass  # No action if condition is True
```

#### 2.2.3 Parameter Check
Use `isinstance()` to validate parameter types.

```python
def my_abs(x):
    # Check if x is int or float
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type')  # Raise error for invalid types
    if x >= 0:
        return x
    else:
        return -x

# Valid call
print(my_abs(10.5))  # Output: 10.5

# Invalid call (raises error)
# my_abs('A')  # Raises TypeError: Bad operand type
```

#### 2.2.4 Returning Multiple Values
Python functions return multiple values as a `tuple` (parentheses optional).

```python
# Function to calculate new coordinates
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny  # Returns a tuple (nx, ny)

# Receive multiple values
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)  # Output: 151.96152422706632 70.0

# Receive as a tuple
pos = move(100, 100, 60, math.pi / 6)
print(pos)  # Output: (151.96152422706632, 70.0)
```


### 2.3 Function Parameters
Python supports flexible parameter types to simplify function calls.

#### 2.3.1 Positional Parameters
Parameters that require values to be passed in order.

```python
# Function with two positional parameters
def power(x, n):
    result = 1
    while n > 0:
        result *= x
        n -= 1
    return result

# Call with positional arguments
print(power(2, 3))  # Output: 8 (2^3)
```

#### 2.3.2 Default Parameters
Parameters with default values (simplify calls for common cases).

```python
# Function with a default parameter (n=2)
def power(x, n=2):
    result = 1
    while n > 0:
        result *= x
        n -= 1
    return result

# Call without default parameter (uses n=2)
print(power(5))  # Output: 25 (5^2)

# Call with custom value for default parameter
print(power(5, 3))  # Output: 125 (5^3)
```

**Warning**: Default parameters must point to **immutable objects** (e.g., `None`, `int`). Using mutable objects (e.g., `list`) causes unexpected behavior.

```python
# Bad: default parameter is a mutable list
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())  # Output: ['END'] (correct first call)
print(add_end())  # Output: ['END', 'END'] (wrong: L retains previous value)

# Good: use None (immutable)
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())  # Output: ['END']
print(add_end())  # Output: ['END'] (correct)
```

#### 2.3.3 Variable-Length Parameters (`*args`)
Accept any number of positional arguments (stored as a `tuple`).

```python
# Function with variable-length parameters
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

# Call with multiple arguments
print(calc(1, 2, 3))  # Output: 14 (1² + 2² + 3²)

# Unpack a list/tuple into variable-length parameters
nums = [1, 2, 3]
print(calc(*nums))  # Output: 14 (equivalent to calc(1, 2, 3))
```

#### 2.3.4 Keyword Parameters (`**kw`)
Accept any number of keyword arguments (stored as a `dict`).

```python
# Function with keyword parameters
def person(name, age, **kw):
    print(f'Name: {name}, Age: {age}, Other: {kw}')

# Call with mandatory parameters only
person('Bob', 35)  # Output: Name: Bob, Age: 35, Other: {}

# Call with additional keyword arguments
person('Alice', 28, city='Beijing', job='Engineer')  # Output: Name: Alice, Age: 28, Other: {'city': 'Beijing', 'job': 'Engineer'}

# Unpack a dict into keyword parameters
extra = {'city': 'Shanghai', 'job': 'Designer'}
person('Charlie', 30, **extra)  # Output: Name: Charlie, Age: 30, Other: {'city': 'Shanghai', 'job': 'Designer'}
```

#### 2.3.5 Named Keyword Parameters
Restrict keyword arguments to specific names (use `*` as a separator).

```python
# Function with named keyword parameters
def person(name, age, *, city, job):
    print(f'Name: {name}, Age: {age}, City: {city}, Job: {job}')

# Valid call (must specify parameter names)
person('David', 25, city='Guangzhou', job='Teacher')  # Output: Name: David, Age: 25, City: Guangzhou, Job: Teacher

# Error: missing parameter names
# person('David', 25, 'Guangzhou', 'Teacher')  # Raises TypeError
```

#### 2.3.6 Parameter Combination
Parameters must be defined in this order: positional → default → variable-length (`*args`) → named keyword → keyword (`**kw`).

```python
# Function with combined parameters
def f(a, b, c=0, *args, d, **kw):
    print(f'a={a}, b={b}, c={c}, args={args}, d={d}, kw={kw}')

# Call the function
f(1, 2, 3, 'x', 'y', d=4, x=99, y=88)
# Output: a=1, b=2, c=3, args=('x', 'y'), d=4, kw={'x': 99, 'y': 88}
```


### 2.4 Recursive Functions
A recursive function calls itself to solve smaller subproblems. It simplifies logic for problems like factorials and the Hanoi Tower.

#### 2.4.1 Basic Recursive Function (Factorial)
```python
# Recursive function to calculate factorial (n! = n × (n-1) × ... × 1)
def fact(n):
    if n == 1:
        return 1  # Base case: stop recursion
    return n * fact(n - 1)  # Recursive case

print(fact(5))  # Output: 120 (5! = 5×4×3×2×1)
```

#### 2.4.2 Tail Recursion
Tail recursion occurs when the recursive call is the last operation (optimized in some languages to avoid stack overflow). Python does **not** optimize tail recursion, so deep recursion may cause stack overflow.

```python
# Tail-recursive factorial (no optimization in Python)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

def fact(n):
    return fact_iter(n, 1)

print(fact(5))  # Output: 120
```

#### 2.4.3 Hanoi Tower Example
The Hanoi Tower problem can be solved elegantly with recursion:
- Move `n-1` disks from tower `a` to `b` (using `c` as a helper).  
- Move the `n`-th disk from `a` to `c`.  
- Move `n-1` disks from `b` to `c` (using `a` as a helper).

```python
def move(n, a, b, c):
    if n == 1:
        print(f'{a} --> {c}')  # Base case: move 1 disk
    else:
        move(n-1, a, c, b)    # Step 1: move n-1 disks from a to b
        print(f'{a} --> {c}')  # Step 2: move n-th disk from a to c
        move(n-1, b, a, c)    # Step 3: move n-1 disks from b to c

# Test with 3 disks
move(3, 'A', 'B', 'C')
# Output:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
```