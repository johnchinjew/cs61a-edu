# Lecture 04: Environment Diagrams

## Abstraction

- Assignment is a simple abstraction: bind name to value
- Function is a powerful abstraction: bind name to suite of  computations
- **Functional abstraction**
    - We can call functions w/o knowing how they work

## Environment Diagrams

> Formalization of how Python code is evaluated

- *Always start in the Global frame*

### When a function is defined:

1. Create a function value in the following form: 
    - `func <name>(<formals>) [parent=<label>]`
        - The parent is the frame in which the function is defined
2. Bind `<name>` to the function value in the current frame

### When a function is applied:

1. Add a local frame and copy the parent of the function
2. Bind the <formals> to the arguments in the local frame
3. Execute the body of the function

## Variable lookup

- lookup name in current frame
- then parent frame
- then its parent frame
- stop at the global frame
- if not found, throw error

## Lambda Expressions

- A way to write one-liner functions
- Creates "anonymous" functions—no intrinsic name

```python3
square = lambda x: x * x
prod = lambda x, y: x * y
```

> A function with parameter x that returns the value of x * x

## Lambda Expressions vs `def` Statements

- Both
    - create a function with the same behavior
    - have their parent as the frame in which they were defined
    - bind the function to the same name
- Only the `def` statement gives the function an intrinsic name
- Lambda functions are **EXPRESSIONS**, whereas `def` functions are **STATEMENTS**
    - Thus, lambda functions cannot contain a suite of statements, like def functions can

`func λ(x) [parent=Global]` vs `func square(x) [parent=Global]`

## Higher-order functions

> A function that takes a function(s) as argument(s) and/or returns a function