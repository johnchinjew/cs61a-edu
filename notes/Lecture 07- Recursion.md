# Lecture 07: Recursion

## Recursive functions

The body of the function calls itself (directly/indirectly)

## Reading recursive functions (WWPD, Env Diags)

- Environment diagrams follow the same rules for recursion
- **Recursive tree**:

/Screen Shot 2018-06-27 at 11.27.41 AM.png

## Writing recursive functions

```python3
def factorial(n):
    """Calculates number!"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

### Structure of a recursive function

1. One or more **base cases**, usu. the *smallest input*
    - **Smallest input** is the input which requires almost no work to solve
2. One or more **recursive calls** with *simpler* arguments
    - **Simpler** means closer to the base case
3. **Using the recursive call** to solve our larger problem

### Recursive "Leap of Faith"

We must assume the recursive call works. Easier to work out if we use tangible values:

```
5! = 5 * 4!
4! = 4 * 3!
.
.
.
```

## Verifying the correctness of recursive functions

1. Verify that the base cases work as expected
2. For each larger case, verify that it works by **assuming the smaller recursive calls are correct**

## Example: Sum Digits

```python3
def sum_digits(n):
    """Calculates the sum of the digits `n`"""
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)
```

## Example: Count Up

```python3
def count_up(n):
    """Prints the numbers from 1 to n"""
    if n == 1:
        return print(1)
    count_up(n-1)
    print(n)
```

Or, w/o `return`

```python3
def count_up(n):
    """Prints the numbers from 1 to n"""
    if n == 1:
        print(1)
    else:
        count_up(n-1)
        print(n)
```

## Mutual Recursion

> Two functions that call each other are *mutually recursive*

```
def f():
    return g()

def g():
    return f()
```

### Is Even and Is Odd (recursively)

My solution...

```
def is_even(n):
    if n == 0 and n < 2:
        return True
    if n < 0:
        return False
    return is_even(n-2)

def is_odd(n):
    return not is_even(n)
```

Instructor solution...

```python3
def is_even(n):
    if n == 0:
        return True
    return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n-1)
```
