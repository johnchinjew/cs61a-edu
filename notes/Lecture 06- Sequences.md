# Lecture 06: Sequences

## Sequences

> An ordered collection of values

- All sequences have a finite length
- Each element in a sequence has a discrete integer index
- You can also...
    - Retrieve an element at a position
    - Create a copy of a subsequence
    - Check for membership
    - Concatenate two sequences together

```
"hello world"[3] # access fourth element, with value "l"
lst = ["Hello", True, 1, -1]
lst[0]
```

### Strings

Sequence of characters.

### Lists

Sequence of values of any data type. (Thus, Python lists are *non-homogeneous*)

### `len` function

Retrieve length (number of elements) in any sequence

## Features of sequences

### Get item

get the *ith* element `<seq>[i]`

### Slice a subsequence

Creates a **COPY** of the sequence from *i* to *j* `<seq>[i:j:skip]`

```
lst[<start_inclusive>:<end_exclusive>:<step>]
```

- *start_inclusive default is 0*
- *end_exclusive default is index of end of list + 1*
- *step default is 1*

### Check membership

Check if the value of <expr> is in <seq> `expr> in <seq>`. Makes use of the `in` operator which evaluates to True or False.

### Concatenate

Combine two sequences into a single sequence <s1> + <s2>

## Sequence Processing

### Iterating through a sequence

You can use a **for statement** to iterate through the lementts of a sequence

*Rules for execution:*

For each element in <seq>:

1. Bind it to <name>
2. Execute <body>

```
for <name> in <seq>:
    <body>
```

### `range` function

> Creates a sequence containing the values within a specified range.

```
range(<start_inclusive>, <end_exclusive>, <step>)

>>> for x in range(1, 10 + 1, 2):
...    print(x)
1
3
5
7
9
```

### List comprehensions

> You can create a list out of a sequence using a list comprehension

```
[<expr> for <name> in <seq> if <cond>]
```

*Rules for execution:*

1. Add a new frame within the current frame as its parent
2. Create an empty result list that will be the value of the list comprehension
3. For each element in <seq>:
    1. Bind that element to <name> in the new frame from step 1
    2. if <cond> evaluates to a true value, then add the value of <expr> to the result list

## Mutability

### Mutable objects

Mutable objects have state and can change over the course of a program. For example, lists.

### List mutation methods

`<list>.append(el)`

`<list>.insert(i, el)` *inserts and shifts the rest of the elements over (inefficient sometimes)*

`<list>.remove(el)` *removes the first occurrence of el and shifts the rest of the elements over (inefficient sometimes)*

`<list>.pop(i)` *removes and returns the el*

**THESE METHODS MUTATE THE LIST. THEY DO NOT RETURN A NEW LIST! (Hence, methods cannot be chained)**

### Identity vs Equality

The **equality operator (`==`)** checks whether two expressions evaluate to equal values.

The **identity comparison operator (`is`)** checks whether two expressions evaluate to the same object

```
>>> l1 = [1, 2]
>>> l2 = [1, 2]
>>> l1 == l2
True
>>> l1 is l2
False
>>> l3 = l1 # l3 is now assigned to the same mutable list l3 is assigne to
>>> l1.append(3)
>>> l3
[1, 2, 3]
>>> l1 is l3
True
>>> l1[:] is l1 # slicing creates a copy
False 
```

### Dictionaries

- Mutable & **unordered**
- Stores mappings from keys to values
- Keys must be unique (there can be no duplicate keys)
- Keys must be **immutable**

```
>>> d = {'a': 1, 'b': [1, 2, 3], 'c': 3, (3, 4): 'c'}
>>> d['a']
1
>>> d['c'] = 10
>>> d['c']
10
```

### Tuples

- Immutable ordered sequence

```
t = (1, 2, 3)
```