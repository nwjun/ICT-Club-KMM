# :blue_book: W1_Notes

## :open_file_folder: Notes, Exercise and Practice 
- [PDF_W1_Notes](https://drive.google.com/file/d/1ZPF-R9N115jEW_Nl9UAG2xa4Rwu3mSUN/view?usp=sharing)
- [PDF_W1_Exercise](https://drive.google.com/file/d/1ZPF-R9N115jEW_Nl9UAG2xa4Rwu3mSUN/view?usp=sharing)
- [W1_Exercise](https://github.com/nwjun/ICT-Club-KMM/tree/main/W1/Exercise)
- [W1_Exercise_Solution](https://github.com/nwjun/ICT-Club-KMM/blob/main/W1/Exercise/W1_Exercise_Solution.py)

<br>

## :pushpin: Outline
- [Python](#python)
- [Print()](#print)
- [Escape Characters](#escape-characters)
- [Input](#input)
- [Variables](#variables)
- [Identifiers](#identifiers)
- [Built-in Data Type](#built-in-data-type)
- [Type Conversion](#type-conversion)
- [Operators](#operators)
- [Reference](#bookreference)

<br>


## Python?

- high level programming language
- use interpreter to translate to machine language
- Usage : Data science, games, machine learning
- easy to learn, shorter syntax

<br>
<br>

## Print()

- used to display output on the console
- can be in form of message or value in variable 



### Definition and Usage

- `print()` function prints the specified message to the screen, or other standard output device

- The message can be a string, or any other object, the object will be converted into a string before written to the screen



### Syntax

print(*object(s)*, sep=*separator*, end=*end*, file=*file*, flush=*flush*)



### Parameter Values


| Parameter         | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| object(s)         | Any object, and as many as you like. Will be converted to string before printed |
| sep='*separator*' | Optional. Specify how to separate the objects, if there is more than one. Default is ' ' |
| end='*end*'       | Optional. Specify what to print at the end. Default is '\n' (line feed) |
| *file*            | Optional. An object with a write method. Default is sys.stdout |
| *flush*           | Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False |



```python
a = 6
b = "6"

print("Hello world!")
>>>Hello world!

print(a)
>>>6

print("I am " + b + " years old")
>>>I am 6 years old

print(a*6)
>>>36

print(b*6)
>>>666666

print(a,b)
>>>6 6

print(a,b,sep=",",end="?")
>>>6,6?
```

<br>
<br>

## Escape Characters

- To insert characters that are illegal in a string, use an escape character
- An escape character is a backslash `\` followed by the character you want to insert

```python
a = "His name is "Someone" "
# invalid syntax

a = "His name is \"Someone\""
print(a)
>>>His name is "Someone"

//alternative
a = 'His name is "Someone"'
```



| Code | Result          |
| ---- | --------------- |
| \\`  | Single Quote(') |
| \\\  | Backslash(\\)   |
| \n   | New line        |
| \t   | Tab             |

<br>
<br>

## Input()

- accept data entered by user



### Syntax

input(*prompt*)



### Parameter Values

| Parameter | Description                                                |
| --------- | ---------------------------------------------------------- |
| *prompt*  | A String, representing a default message before the input. |



```python
a = input("What's your name?")
print("Hi " + a)

>>> What's your name? >Kelly
>>> Hi Kelly
```


<br>
<br>

## Variables

- containers for storing data values
- no need declare variable with particular type
- string variables can be declared by using single quotes or double quotes
- casting can be used to specify the data type of variable


<br>
<br>

## Identifiers

- first character can't be a digit

- any length consisting letters, digits, and underscore(_)

- case-sensitive

- any name except reserved word (eg: int, return, string)

 ![Python-Keywords](https://github.com/nwjun/ICT-Club-KMM/blob/main/W1/PythonKeywords.png) 

```python
x = 6 #type int
y = "hello world" #type str
1foobar = 8 #wrong
_foobar = 8 #correct
foobar = 8 #correct
```

<br>
<br>

## Built-in Data type

- Data types are the classification or categorization of data items



| Type     |                     |
| -------- | ------------------- |
| Text     | str                 |
| Numeric  | int, float, complex |
| Sequence | list, tuple, range  |
| Boolean  | bool                |

```python
a = 7
type(a)
>>> <class 'int'>

b = "hello world"
type(b)
>>> <class 'str'>

c = 1j
type(c)
>>> <class 'complex'>

d = 4.5
type(d)
>>> <class 'float'>

e = True
type(e)
>>> <class 'bool'>

f = [6,5,4]
type(f)
>>> <class 'list'>

g = ("apple", "banana")
type(g)
>>> <class 'tuple'>

h = range(6)
type(h)
>>> <class 'range'>
```

<br>
<br>


## Type Conversion

| Function     | Explanation                                            |
| ------------ | ------------------------------------------------------ |
| int()        | convert any data type to integer                       |
| float()      | convert any data type to floating-point number         |
| tuple()      | convert to tuple                                       |
| list()       | convert any data type to a list                        |
| dict()       | convert a tuple of order(key, value) into a dictionary |
| char(number) | converts number to its corresponding ASCII number      |



```python
num = '4'
word = 'Hello'
tup = (('a',1),('b',2))
character = 87

a = int(num)
print(s*8)
>>>32

b = tuple(word)
print(b)
>>>('H','e','l','l','o')

c = list(word)
print(c)
>>>['H','e','l','l','o']

d = dict(tup)
print(d)
>>>{'a': 1,'b': 2}

e = char(character)
print(e)
>>>W
```

<br>
<br>


## Operators

### Arithmetic Operators

- used with numeric values to perform common mathematical operations

  

| Operator | Name           | Python expression |
| -------- | -------------- | ----------------- |
| +        | Addition       | x + y             |
| -        | Subtraction    | x - y             |
| *        | Multiplication | x * y             |
| /        | Division       | x / y             |
| %        | Modulus        | x % y             |
| **       | Exponentiation | x ** y            |
| //       | Floor division | x // y            |

```python
x = 3
y = 2

print(x**y)
>>> 9
# 3 to the power of 2 = 9

print(x%y)
>>> 1
# remainder of 3/2 = 1

print(x//y)
>>> 1
# floor(3/2) = floor(1.5) = 1
```

<br>

### Assignment Operators

- assign values to variables



| Operator | Example | Same as    |
| -------- | ------- | ---------- |
| =        | x = 6   |            |
| +=       | x += 2  | x = x + 2  |
| -=       | x -= 2  | x = x - 2  |
| *=       | x *= 2  | x = x * 2  |
| /=       | x /= 2  | x = x / 2  |
| %=       | x %= 2  | x = x % 2  |
| **=      | x //= 2 | x = x // 2 |



### Comparison Operators

- to compare two values
- mostly used in if or while statement



| Operator | Name                     | Example |
| -------- | ------------------------ | ------- |
| ==       | Equal                    | x == y  |
| !=       | Not equal                | x != y  |
| >        | Greater than             | x > y   |
| <        | Less than                | x < y   |
| >=       | Greater than or equal to | x >= y  |
| <=       | Less than or equal to    | x <= y  |

<br>

### Logical Operators

- used to combine conditional statements

| Operators | Description                                  | Example               |
| --------- | -------------------------------------------- | --------------------- |
| and       | Return True if both statements are true      | x < 5 and x < 10      |
| or        | Return True if one of the statements is true | x < 5 or x <4         |
| not       | Reverse the result                           | not(x < 5 and x < 10) |

<br>

### Identity Operators

| Operator | Description                                            | Example    |
| -------- | ------------------------------------------------------ | ---------- |
| is       | Returns True if both variables are the same object     | x is y     |
| is not   | Returns True if both variables are not the same object | x is not y |

<br>

### Membership Operators

| Operator | Description                                                  | Example    |
| -------- | ------------------------------------------------------------ | ---------- |
| in       | Returns True if a sequence with the specified value is present in the object | x in y     |
| not in   | Returns True if a sequence with the specified value is not present in the object | x not in y |

<br>

### Precedence Level

| Operators                                    | Meaning                                           | Association   |
| -------------------------------------------- | ------------------------------------------------- | ------------- |
| ()                                           | Parenthesis                                       | Inside out    |
| **                                           | Exponent                                          | Right to left |
| *, /, //, %                                  | Multiplication, Division, Floor division, Modulus | Left to right |
| +, -                                         | Addition, subtraction                             | Left to right |
| ==, !=, >, >=, <, <=, is, is not, in, not in | Comparisons, Identity, membership operators       |               |
| not                                          | Logical NOT                                       |               |
| and                                          | Logical AND                                       |               |
| or                                           | Logical OR                                        |               |

<br>
<br>
<br>
<br>


## :book:Reference

GeeksforGeeks. (2021, January 21). *Type Conversion in Python*. https://www.geeksforgeeks.org/type-conversion-python/

King, K. N. (2008). *C Programming: A Modern Approach, 2nd Edition* (2nd ed.). W. W. Norton & Company.

*Python Data Types*. (n.d.). W3schools. Retrieved February 12, 2021, from https://www.w3schools.com/python/python_datatypes.asp

*Python Escape Characters*. (n.d.). W3schools. Retrieved February 19, 2021, from https://www.w3schools.com/python/gloss_python_escape_characters.asp

*Python input() Function*. (n.d.). W3schools. Retrieved February 12, 2021, from https://www.w3schools.com/python/ref_func_input.asp

*Python Operators*. (n.d.). W3schools. Retrieved February 12, 2021, from https://www.w3schools.com/python/python_operators.asp

*Python print() Function*. (n.d.). W3schools. Retrieved February 12, 2021, from https://www.w3schools.com/python/ref_func_print.asp
