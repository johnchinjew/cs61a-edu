# Lecture 21: Macros

## Programs as data

Scheme programs consist of expressions, which can be:

- Primitive exprs: `2`, `#t`, `+`
- Combinations: `(quotient 10 2)`
- Scheme lists can represent combinations

We can easily make a program which writes a program.

```
; Code as data

(define (fact n)
  (if (= n 0) 1 (* n (fact (- n 1)))))

(define (fact-exp n)
  (if (= n 0) 1 (list '* n (fact-exp (- n 1)))))

(fact 5) ; 120
(fact-exp 5) ; (* 5 (* 4 (* 3 (* 2 (* 1 1)))))
(eval (fact-exp 5)) ; 120

(define (fib n)
  (if (< n 2) n (+ (fib (- n 2)) (fib (- n 1)))))

(define (fib-exp n)
  (if (< n 2) n (list '+ (fib-exp (- n 2)) (fib-exp (- n 1)))))
```

## Macros

```
; Macros

(print 2) ; prints 2
(begin (print 2) (print 2)) ; prints 2 twice

(define (twice expr) (begin expr expr))
(twice (print 2)) ; only prints 2 once

(define (twice expr) (list 'begin expr expr))
(twice '(print 2)) ; (begin (print 2) (print 2))
(eval (twice '(print 2))) ; actually prints 2 twice
```

A **macro** is an operation performed on the source code of a program

Scheme has `define-macro` special form

- Defines a procedure that takes in pieces of code and writes a new piece of code that then gets evaluated

/Screen Shot 2018-07-26 at 11.27.27 AM.png

```
(define-macro (twice expr) (list 'begin expr expr))
(twice (print 2)) ; actually prints 2 twice

(define-macro (add-to! sym expr)
  (list 'set! sym (list '+ sym expr)))
```


## Evaluation Procedure for Macros

1. Evaluate the operator sub-expression, which evaluates to a macro procedure.
2. Apply the macro procedure to the operand expressions without evaluating them first.
3. Evaluate the expression returned by the macro procedure

## Writing Macros

- When writing macros, we're given Scheme expressions (as Scheme lists) and our job is to construct a new Scheme list that represents the code we want to run.
- It's often helpful to write examples of both a macro's usage and equivalent code, so that you can figure out how to construct it. Consider `add-to!`, which is to `set!` what `+=` is to regular assignment in Python.

/Screen Shot 2018-07-26 at 11.37.48 AM.png

```
(define x 4)
(add-to! x (* 2 3))
x ; is now 10

(define-macro (for sym vals expr)
  (list 'map (list 'lambda (list sym) expr) vals))

(map (lambda (x) (* x x)) '(1 2 3 4)) ; (1 4 9 16)
(for x '(1 2 3 4) (* x x)) ; same as the above
```

## Quasiquotation

Quasiquotation allows you to have some parts of a list be read literally and some parts be evaluated.

```
- <- Quote
` <- Quasiquote
, <- Unquote
```

```
; Quasiquotation

(define x 2)

'(1 2 3) ; (1 2 3)
(list 1 x 3) ; (1 2 3)
'(1 x 3) ; (1 x 3)
`(1 ,x 3) ; (1 2 3)
'(1 ,x 3) ; (1 (unquote x) 3)
`(1 ,(+ x 5) 3); (1 6 3)


(define-macro (for sym vals expr)
  `(map (lambda (,sym) ,exprs) ,vals))
```

## Variable-arity Procedures

Definition: A procedure that can take different numbers of arguments

We can accomplish Python's `*args` in Scheme by putting a dot before the last formal parameter of a procedure.

```
; Variable-Arity Procedures

(define (count . args)
  (if (null? args)
      0
      (+ 1
         (apply count (cdr args))))) ; apply allows you to pass a list of arguments to any Scheme procedure (essentially, a spread operator)

(count) ; 0
(count 1) ; 1
(count 1 2 3) ; 3
(count 1 '(2 3) 4) ; 3
```

`apply` spreads/unpacks a list of args into a procedure

```
(apply fn '(1 2 3)) -> (fn 1 2 3)
```