# Lecture 09: Data Abstraction

## Rational numbers

**Rational number**: exact representation of fractions as a pair of integers

```
>>> 3 / 7
0.4285... # EXACT REPRESENTATION IS LOST
```

## Compound values

> Values that consist of multiple components

- Ex: Rational numbers, Dates, Geographic locations

- Want to manipulate compound values as singular units with extractable parts

- **Data abstraction** allows us to represent compound values in our program

## Abstract data types (ADT)

- We can implement rational numbers as **abstract data types**
- ADT consists of a **constructor** (creates a single value of a particular data type) and some **selectors** (allow us to access attributes of a value).

### Constructor

Creates a rational number

```
numerator = 2
denominator = 3
two_thirds = rational(numerator, denominator) # constructs
```

## Selector

Selects from a rational number

```
# selects
>>> numer(two_thirds)
2
>>> denom(two_thirds)
3
```

## Rational number arithmetic implementation

/Screen Shot 2018-07-02 at 11.33.18 AM.png

```python3
def mul_rational(r1, r2):
    rational(numer(r1) * numer(r2),
        denom(r1) * denom(r2))

def add_rational(r1, r2):
    a, b = numer(r1), denom(r1)
    c, d = numer(r2), denom(r2)
    return rational(a*d + c*b, b*d)

def print_rational(r):
    print(numer(r1), '/', denom(r))
```

## Abstraction barrier

> An abstraction barrier exists between the implementation and use of data representations.

- Separation between how a thing is *implemented* and how it is *used*
- Can write functions for rational numbers (`mul_rational`, etc) without understanding implementation of rational.

## Abstraction violations

> Assuming a data type's implementation is known as an abstraction violation.

### One way to implement rational numbers

```
def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]
```

- All these functions are on the same side of the abstraction barrier.
- They can all **SAFELY ASSUME RATIONAL NUMBERS ARE IMPLEMENTED USING LISTS**.
- However, functions such as `mul_rational` which were written outside the abstraction barrier **CANNOT MAKE THIS ASSUMPTION**.

This (below) is **BAD** it violates the abstraction barrier making our code fragile and dependent on the current implementation of `rational`:

```
add_rational([1, 2], [4, 5])

def divide_rational(r1, r2):
    return [r1[0] * r2[1], r[1] * r[0]]
```

### Changes to the ADT implementation

- Changes to the *implementation* may BREAK the *usage* IF the usage violates the abstraction barrier.
- Changes to the underlying implementation shouldn't cause errors.

/Screen Shot 2018-07-02 at 11.58.37 AM.png

---

## Review

/Screen Shot 2018-07-02 at 12.05.01 PM.png

## Aside: best implementation of `rational`

```python3
from fractions import gcd

def rationals(numer, denom):
    g = gcd(numer, denom)
    return (numer//g, denom//g)

def numerator(r):
    return r[0]

def denominator(r):
    return r[1]
```