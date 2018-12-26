# Lecture 05: Higher-Order Functions

> Understanding functional abstractions

## Lambda expressions vs `def` statements

- Both create a function with the same behavior
- Both functions’ parents are the frame in which they are defined
- Lambdas are expressions and are limited in that they can only immediately return a single expression (no statements)
- `def` statements can contain other statements and use a return statement to return a value.
- Only the `def` statement gives the function an intrinsic name

## Higher-Order functions

- Can take function as argument
- Can return function as return value

> Functions are **first-class**, meaning they can be manipulated as values

## Describing Functions

- **Domain**: the set of possible inputs a function may take as arguments
- **Range**: The set of possible output values a function may return
- **Behavior**: The relationship between input and output

## Designing functions

- Function does exactly one job, but make it apply to many related situations
- Don't repeat yourself (DRY), duplicated code is unmaintainable

## Generalizing patterns with arguments

> A generalized function for areas of shapes

```python3
from math import pi, sqrt
def area(r, shape_constant):
    """Return teh area of a shape with some constant SHAPE_CONSTANT"""
    assert r >= 0, "A length must be positive"
    return r * r * shape_constant

area_square = lambda r: area(r, 1)
area_circle = lambda r: area(r, pi)
area_hexagon = lambda r: area(r, 3 * sqrt(3) / 2)
```

### Using `assert`

> Places restrictions on arguments

```python3
def func(x):
    assert x > 0, "argument must be positive"
```

## Generalizing over computational processes

- Similar computational processes can be represented as functions
- You can then pass those functions into other functions which generalize a larger functionality

## Function Composition

```python3
def make_adder(n):
    def adder(k):
        return n + k
    return adder

def square(x):
    return x * x

def compose(f, g):
    def h(x):
        return f(g(x))
    return h

add_5_squared = compose(square, make_adder(5))

>>> add_5_squared(3) # (3 + 5) ^ 2
64
```

## Self reference

```
def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n + k)
    return next_sum

>>> print_sums(1)(3)(5)
1
4
9
```