# Lecture 18: Lazy Evaluation

## Defs

- **Lazy evaluation**: Delays eval of an expr until its value is needed
    - Allows control flow (if, and, or)
    - Allows to define infinite data structures
- **Iterables**: An obj capable of returning its members one at a time (lists, strings, tuples, dicts)
    - Like a book
- **Iterator**: An obj that provides sequential access to values, one by one
    - Like a bookmark
    - *All iterators are iterables, but not all iterables are iterators*

## Iterators

- `iter(iterable)`: returns an iterator over the elems of an iterable arg
    - If you pass in an iterator, it just returns itself
- `next(iterator)`: Return the next elem in an iterator
    - Returns the current "page" and moves the "bookmark" to the next "page"
    - Iterator remembers where you left off
    - If the curr page is the end of the book, ERR

/Screen Shot 2018-07-23 at 11.19.16 AM.png

*Note: Iterators are ALWAYS ordered even if the container that produced them (e.g. dict) is not ordered*

## Exceptions / Errors

`raise <expression>`

`<expression>` must eval to a subclass of `BaseException` or an instance of one

Exceptions are constructed like any other object: `TypeError('Error message')`

Examples:

```
TypeError: function passed wrong number/type of arg
NameError: A name wasn't found
KeyError: A key wasn't found in a dict
RuntimeError: Catch all for troubles during interpretation
```

/Screen Shot 2018-07-23 at 11.30.00 AM.png

## Try Statements

Handle exceptions, preventing crashing

```
try:
    <try suite>
except <exception class> as <name>:
    <except suite>
```

Execution rules:
1. The <try suite> is executed first
2. If, while exec <try suite>, an exception is raised that is not handled otherwise then the <except suite> is executed with <name> bound to the exception

/Screen Shot 2018-07-23 at 11.32.45 AM.png

## Iterators: The For Statement

```
for <name> in <expression>:
    <suite>
```

1. Evaluate the header <expression>, which must must eval to an iterable obj
2. For each elem in that seq, in order:
    3. Bind <name> to that elem in the first frame of the curr enviro
    4. Execute the suite

**When executing a `for` statement, iter returns an iterator and next provides each item:**

/Screen Shot 2018-07-23 at 11.39.45 AM.png

## Built-in iteration funcs

Many built-in Python sequence operations return iterators that compute results **LAZILY**.

/Screen Shot 2018-07-23 at 11.42.44 AM.png

*To view the contents of an iterator, place the resulting elements into a container*

/Screen Shot 2018-07-23 at 11.42.47 AM.png

/Screen Shot 2018-07-23 at 11.43.24 AM.png

**NOTE: map does not instantly double all numbers in the list... it just returns an iterator!**

## Generators & Gen. funcs

- Defs
    - **Generator**: An iterator created automatically by calling a generator function
    - **Generator func**: a func that contains the `yield` keyword anywhere in the body
- When a generator function is called, it returns a generator instead of going into the body of the function. The only way to go into the body of a generator function is by calling next on the returned generator.
- Yielding values are the same as returning values except yield remembers where it left off.
- *Generators are iterators which are iterable*

/Screen Shot 2018-07-23 at 11.52.36 AM.png

- We are allowed to call next on generators because generators are a type of iterator.
- Calling next on a generator goes into the function and evaluates to the first yield statement. The next time we call next on that generator, it resumes where it left off (just like calling next on any iterator!)
- Once the generator hits a return statement, it raises a StopIteration

## `yield from`

A `yield from` statement yields all values from an iterable.

/Screen Shot 2018-07-23 at 11.59.58 AM.png

---

## Streams (in Scheme)

Definitions:
- **Streams**- Are lazily computed pairs. They are analogous to lazily computed Scheme lists.
- **Promise**- An expression that evaluates to a value only when asked to. This is how streams accomplish lazy evaluation.
- **Not forced**- Means the promise has not been evaluated yet.
- **Forced**- Means the promise has already been evaluated.

```
scm> (cons 1 (/ 1 0))
Error: cannot divide by zero

scm> (cons-stream 1 (/ 1 0))
(1 . #[promise (not forced)])
```

## Constructing Streams

We use the special form cons-stream to create a stream:

```
(cons-stream <operand1> <operand2>)
```

`<operand1>` can be any value
`<operand2>` has to be another stream or nil

To evaluate this expression, Scheme does the following:
1. Evaluate the first operand.
2. Construct a promise containing the second operand.
3. Return a pair containing the value of the first operand and the promise.

/Screen Shot 2018-07-23 at 12.11.32 PM.png

## Evaluating streams

car- Returns the first element of the stream

cdr- Returns the rest of the stream. In this course, this should always return a promise.

cdr-stream- Forces the promise to evaluate. If the promise has already been forced, it immediately returns it (without reevaluating it).

/Screen Shot 2018-07-23 at 12.16.27 PM.png

## Recursively defined streams - Constant Stream

Infinitely long stream with a number repeated

```
(define (constant-stream i)
    (cons-stream i (constant-stream i))

scm> (define ones (constant-stream 1))
scm> (car ones)
1
scm> (car (cdr-stream ones)
1
```

## Natural number stream

```
(define (nats start)
    (cons-stream start (nats (+ start 1)))

scm> (define s (nats 0))
scm> (car s)
0
scm> (car (cdr-stream s))
1
scm> (car (cdr-stream (cdr-stream s)))
2
```

## Add-Stream

```
(define (add-stream s1 s2)
	(cons-stream (+ (car s1) (car s2))
				  (add-stream (cdr-stream s1) (cdr-stream s2)))
)
```

## Ints-Stream

```
(define ints (cons-stream 1 (add-stream ones ints))
```

## Stream Processing

/Screen Shot 2018-07-23 at 12.29.50 PM.png

## HOF on Streams

```
(define (map f lst)
  (if (null? lst)
      nil
      (cons (f (car lst)) (map f (cdr lst)))))
```

```
(define (map-stream f s)
  (if (null? s)
      nil
      (cons-stream (f (car s)) (map-stream f (cdr-stream s))))
```

*We still need the base case because streams can be finite. We just replace cons with cons-stream and cdr with cdr-stream!*