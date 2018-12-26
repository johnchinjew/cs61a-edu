# Lecture 13: Scheme Lists

- Like Python, Scheme has **atomic** data types
    - Like numbers or bools which cannot be divided into smaller pieces
- Python has many **compound** data types: lists, etc which can be broken down
    - Scheme has only ONE: the `pair`

## Pairs in Scheme

- Fundamental unit of data abstraction is the **pair**
- Can be constructed with the `cons` built-in procedure
- Two fields
    - `car` - first
    - `cdr` - rest

```
scm> (define pair (cons 1 2)) ; (car . cdr)
pair
scm> pair
(1 . 2)
scm> (car pair)
1
scm> (cdr pair)
2
```

## Linking pairs together (Linked list)

We can create longer sequences by putting one element in the car and putting another pair in the cdr.

```
(cons 1 (cons 2 (cons 3 (cons 4 (cons 5 ())))))
```

/Screen Shot 2018-07-12 at 11.19.15 AM.png

When we say Scheme list, we mean **linked list**, since that's the only type of list that Scheme has!

Formally, we define a list in Scheme to be one of two things:

- the empty list, or
- a pair whose cdr is also a list


### The empty list

We use the empty list in our cdr to signal the end of our sequence.

```
scm> ()
()
scm> nil ; nil, aka empty list
()
```

## Constructing lists

You don't always need to use `cons` manually

```
scm> (define a 2)
a
scm> (cons 1 (cons a (cons 3 ())))
(1 2 3)
scm> (list 1 a 3)
(1 2 3)
scm> '(1 a 3)
(1 a 3)
```

*Note that cons and list are both built-in procedures, so each operand is evaluated, but using the quote special form means the entire expression (including symbols) is taken literally.*

## Symbolic Programming

> Scheme Code is Scheme Data 

- Consider the Scheme expression (+ 1 2).
- It looks a lot like a list of the + symbol, the number 1, and the number 2.
- That's because it is!
- Scheme code is actually built out of Scheme lists!
- When we enter an expression into the interpreter, it converts it into a Scheme list and then evaluates that.
- We can prevent the evaluation of an expression by quoting it.
- We can then manipulate our Scheme code as lists before evaluating it with eval.

## Mutating Scheme Lists

```
set-car! ; exclamation means procedure is mutative
ser-cdr!
```

```
scm> (define lst1 '(1 2 3))
lst1
scm> (define lst2 lst1)
lst2
scm> (set-car! lst1 6)
scm> (set-car! lst1 6)
scm> lst1
(6 2 3 4 5)
```

```
scm> (define code '(+ 1 2))
scm> code
(+ 1 2)
scm> (eval code)
3
scm> (set-car! (cdr code) 5)
scm> (eval code)
7
```

## Non-mutative `map` implementation

```
(define (map proc lst)
  (if (null? lst)
      nil
      (cons (proc (car lst))
            (map proc (cdr lst)))))
```

## Mutative `map!` procedure

```
(define (map! proc lst)
  (if (not (null? lst))
      (begin
        (set-car! lst (proc (car lst)))
        (map! proc (cdr lst)))))
```

## `filter` and `filter!`

```
(define (filter pred lst)
	(cond ((null? lst) nil)
				((pred (car lst)) (cons (car lst) (filter pred (cdr lst))))
				(else (filter pred (cdr lst)))))
```

```
???
```