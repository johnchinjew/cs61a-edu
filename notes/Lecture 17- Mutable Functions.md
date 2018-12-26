# Lecture 17: Mutable Functions

> A function with behavior that varies over time/usage.

## Bank account (closure)

/Screen Shot 2018-07-19 at 12.09.09 PM.png

/Screen Shot 2018-07-19 at 12.09.36 PM.png

/Screen Shot 2018-07-19 at 12.10.04 PM.png

## Nonlocal statements

```
nonlocal <name1>, <name2>, ...
```

Future assignments to the <name> change its pre-existing binding in the **first nonlocal frame** of the current environment in which that <name> is bound.

/Screen Shot 2018-07-19 at 12.45.49 PM.png

## Python Particulars

/Screen Shot 2018-07-19 at 11.28.25 AM.png

Python actually pre-computes which frame contains each name before executing the body of a function, thus, **within the body of a function, all instances of a name must refer to the same frame**

## Mutable values and persistent local state

Mutable values can be changed *without* a nonlocal statement

/Screen Shot 2018-07-19 at 11.31.17 AM.png

## Mutable functions in Scheme

## `set!`

Works like `define` but instead of creating a new binding in the current frame, **it modifies an existing binding (could be in the current frame or a parent frame)**

/Screen Shot 2018-07-19 at 11.46.44 AM.png

## Referential Transparency

Expressions are **referentially transparent** if substituting an expression with its return value does not change the meaning of the program.

For an expression to be referentially transparent, it must be both **pure** (no side-effects) and **deterministic** (the same every time)

Mutation operations violate the conditions of referential transparency because they are impure. They do more than just return a value and *they change the environment*