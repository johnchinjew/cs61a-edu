# Lecture 02: Functions

## Names

- You can assign a **single value** to a name
- Names are unaware of how the value they reference was obtained/computed
- *Names are primitive expressions*
- One way to introduce a new name in a program is with an **assignment statement**
    - Evaluate the expression to the right of `=`
    - Bind the value of the expression to the name to the left of `=` in the current environment.

## Environments

- Names and their values are stored in environments
- Environment determines meaning of the symbols in expressions.
- `add(x, 1)` is meaningless without specifying the environment which  provides meaning for the name `x` or `add`.

## Functions

- Functions are a series of statements that map input arguments to a output return value.
- Define functions with the `def` statement, for example:

```
def hyp(a, b): \ # with **parameters** `a` & `b`
    return sqrt(a ** 2 + b ** 2)
```

- Python binds name to a function
    - Note that `hyp` is the function's *intrinsic name*
- Note that `def` statements can be nested
    - Doing so creates a **closure**, where the state of the outer function is accessible from the inner function
    - You can also return the inner function from the outer function
    - To pass arguments to a returned inner function use consecutive parenthesis, like so `f(x)(y)` where `f(x)` returns the inner function and `(y)` is the argument passed to the inner function

## Calling functions

1. Evaluate the operator (should be a function)
2. Evaluate the operands to get the argument values
3. Apply the alue of the operator (function) to the value of the operands (arguments)

## Call frames

- To apply a function, a new **call frame** must be added to the environment
    1. Create a new frame, labeling it with a sequential frame number, the intrinsic name of the function, and the parent frame
        - **Parent frame**: where the function was defined
    2. Bind the parameters of the function to the argument values
    3. Execute the body of the function in this new frame

## `return` statement

- specifies expression to evaluate to obtain return value for function call
- if function does not have a a return statement, the function returns `None` by default

## Abstractions categories

- Assignment statements
    - Bind names to values (such as `7`)
- `def` statements
    - Bind names to statements (such as `return x + y`)
- *The goal is to hide computational complexity in a human-readable name we can easily refer to and logically manipulate*