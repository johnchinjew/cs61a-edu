# Lecture 03: Control
> Creating logical path for program to follow

## `None`

> Special value `None` represents nothing in Python

- Means nothing is returned
- Function will default to returning `None` if they do not explicitly return another value

## `print` vs `return`
- Printing is just a side-effect
    - Value printed is not useable by Python
- Return statements allow us to pass values between functions

## Pure functions

- Applying them has no effects beyond returning a value
- Will always return the same value when called with the same arguments
- Essential for writing concurrent programs, where multiple call expressions are evaluated simultaneously

## Non-pure functions

- Can generate side-effects, which make some change to the state of the interpreter or computer. (e.g. the `print` function)

## Conditional statements (`if` statements)

```python3
if (<conditional expression>):  # an if "clause"
    <statements suite>          # an if "clause"
elif (<conditional expression>):  # the elif "clause"
    <statements suite>            # the elif "clause"
else:
    <statements suite>
```

## Boolean context

> Any place where an expression is evaluated to check if it's a True value or a False value

```
if x < 0:     # a boolean context
elif x == 0:  # another boolean context
```

### False values

- `False`
- `None`
- 0
- ""

### True values

- everything else

## Boolean expressions

> Contains special operator(s) `and`, `or`, or `not`

### \<exp1\> `and` \<exp2\> `and` \<exp3\> `and` ...

> Evaluates to first false value. If none are false, evaluates to the last expression

### \<exp1\> `or` \<exp2\> `or` \<exp3\> `or` ...

> Evaluates to first true value. If none are true, evaluates to the last expression

### `not` \<exp\>

> Evaluates to True if \<exp\> is a false value and False if \<exp\> is a true value

### Short-circuiting

> Short-circuiting is when an expression returns the value and stops evaluating latter expressions.

- If `and` finds a `False` value, it returns that value and stops evaluating remaining values.
- If `or` finds a `True` value, it returns that value and stops evaluating remaining values.

## Iteration

### `while` loops

- Runs `while`'s suite until header's expression (the *stop condition*) evaluates to `False`

### `for` loops using range

```python3
for i in range(1, n + 1)
```

*Range starts at `1`, but does **NOT** include `n + 1`*