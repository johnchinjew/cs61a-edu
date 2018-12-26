# Lecture 12: Scheme

> Timeless functional programming language

## Scheme Expressions

Scheme programs consist **ENTIRELY** of **TWO** types of **EXPRESSIONS**.

### Atomic Expressions

- *Self-evaluating*: numbers, booleans
    - `3`, `5.5`, `-10`, `#t`, `#f`
- *Symbols*: names bound to values
    - `+`, `modulo`, `list`, `x`, `foo`, `hello-world`

### Combinations

```
(<operator> <operand1> <operand2> ...)
```

## Scheme values

### Atoms

> Primitive values that **cannot be broken into smaller parts**

1. Numbers
    - `10`, `-6`, `5.7`
2. Booleans
    - `#t`, `#f`
3. Symbols
    - `hello`, `world`

### Procedures

Function objects (built-in or user-defined)

```
(lambda (x) (* x x))
```

### Lists

A sequence of zero or more values

```
(1 2 3 4 5 6 7)
(c s 6 1 a)
```

## Combinations

All non-primitive expressions in Scheme have the following syntax:

```
(<operator> <operand1> ...)
```

A combination is either a **call expression** or a **special form expression**

- The operator of a *call expression* evaluates to a *procedure (a function object, a lambda)*
    - `(+ 2 3)`, `(abs (/ 20 5))`
- The operator of a *special form expression* is a *special form*
    - `(define x 5)`, `(if #t 10 20)`

### Call expressions

```
(<operator> <operand1> ...)
```

1. Evaluate the **operator** to get a **procedure**
2. Evaluate all **operands** *left to right* to get the arguments
3. Apply the **procedure** to the arguments

*All operands are evaluated to arguments before applying; this contrasts to special form expressions*

### Special form expressions

```
(<operator> <operand1> ...)
```

Special forms have special behaviors, allowing for more complex programs

- Each special form has **its own rules**
- **Some operands may not be evaluated (UNLIKE CALL EXPRESSIONS)**

```
scm> (define x (/ 10 2))
x
scm> (if (> 1 0) (- 3 4) (/ 1 0))
-1
scm> (quote (c s 6 1 a))
(c s 6 1 a)
scm> (lambda (x y) (+ x y))
(lambda (x y) (+ x y))
```

## Special forms

### Assigning values to names

The define special form assigns a value to a name:

```
(define <name> <expr>)
```

1. Evaluate the given expression
2. Bind the *resulting* value to the given name *in the current frame*.
3. Return the name as a **symbol**

```
scm> (define x (+ 3 4))
x
scm> x
7
scm> (define x (+ x 5))
x
scm> x
12
```

### Creating functions

The **lambda special form** returns a **lambda procedure**.

```
(lambda (<param1> ...) <body>)
```

1. Create a lambda procedure with the given parameters and body
2. Return the lambda procedure

Creating a lambda procedure with a **lambda special form expression** returns a **lambda procedure**

- *Body of expression is evaluated when the lambda procedure is applied. NOT AT DEFINITION*
- *All functions in Scheme are lambda functions*

```
scm> (lambda (x) (* x x))
(lambda (x) (* x x))
scm> ((lambda (x) (* x x)) 5)
25
scm> (define square (lambda (x) (* x x)))
square
scm> (square 4)
16
```

#### Defining functions with names

Second version of define is shorthand for creating a function with a name

```
(define (<nam> <param1> ...) <body>)
```

1. Create a lambda procedure with the given parameters and body
2. Bind it to the given name in the current frame
3. Return the function name as a symbol

```
scm> (define (square x) (* x x))
square
scm> square
(lambda (x) (* x x))
scm> (square 4)
16
scm> (square -10)
100
```

### Control flow

The **if special form** allows us to evaluates an expression based on a condition.

```
(if <predicate> <if-true> [if-false])
```

1. Evaluate predicate
2. If predicate evaluates to **ANYTHING** but `#f`, evaluate `<if-true>` and return value. Otherwise, evaluate `[if-false]` if provided and return the value.

```
scm> (if #t 3 5)
3
scm> (if 0 (+ 1 0) (/ 1 0))
1
scm> (if (> 10 1) (* 5 6))
30
scm> (if (not 4) 1 (if #f 5 6))
6
```

### Control flow with `cond`

The cond special form allows us to specify many conditions and consequences:

```
(cond (<pred1> <expr1>) (<pred2> <expr2>) … (else <else-expr>))
```

*Each (<pred> <expr>) is called a clause*

1. Evaluate <pred1>, <pred2>, etc. until one evaluates to a truth-y value.
2. Evaluate and return the expression corresponding to the first truth-y predicate. If no predicate evaluates to a truth-y value, evaluate and return <else-expr> if provided.

```
scm> (cond (#f 4)
 			 ((> 3 4) (/ 1 0))
 ((even? 10) 100)
 ((odd? 5) 200)
 (else (print 5)))
100
```

## Writing procedures

### Factorial

```
(define (fact n)
  (if (<= n 1)
      n
      (* n (fact (- n 1)))))
```

### Counting up

```
(define (count-up n)
  (define (counter k)
    (print k)
    (if (< k n)
        (counter (+ k 1))))
  (counter 1))
```

### Hailstone

```
(define (hailstone n)
  (print n)
  (cond ((= n 1) 1)
        ((even? n) (hailstone (/ n 2)))
        (else (hailstone (+ 1 (* n 3))))))
```

## Lists

The built-in list procedure takes in an arbitrary number of arguments and constructs a list containing the values of those arguments:

```
scm> (list 1 2 (+ 3 4))
(1 2 7)
scm> (list 5 (list 6 7) 8)
(5 (6 7) 8)
```

The quote special form can be used to create a list literal:

```
(quote <expr>)
'<expr>
```

*How to evaluate:*
1. Do not evaluate <expr>. Return it as a value.

```
scm> (quote (1 2 (+ 3 4)))
(1 2 (+ 3 4))
scm> '(h e l l o)
(h e l l o)
```

## Built-in list procedures

- `map` takes in 1-arg procedure and list, and returns the result of applying the procedure to every element in the list
- `filter` takes in a predicate and a list and returns a new list containing only elements that fulfill the predicate
- `reduce` takes in a combiner procedure and a list and returns the result of combining all values in the given list

```
scm> (map (lambda (x) (* x x)) '(1 2 3 4))
(1 4 9 16)
scm> (filter even? '(5 6 7 8))
(6 8)
scm> (reduce + '(9 10 11 12))
42
```