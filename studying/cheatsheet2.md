# Cheatsheet 2

`is` - identity operator

`is not` - mis-identity operator

*`not` here is not the normal `not` operator*

## WWPD

- Topics:
    - Iterator/generator
    - OOP
        - Class vs. instance attrs
        - Bound methods vs functions
    - Recursion, HOFs, and mutable functions
- Tips:
    - Use scratch paper in a smart way!
- When evaluating an object in repl, `__repr__` does not print out quotes, but it normally does return a quoted string value

```
>>> obj
my test object!
>>> obj.__repr__()
'my test object!'
```

- `map` returns an iterator, NOT a list

## Tree Recursion Strats

1. Use something or don't (count change, partitions)
2. Try all possibilities (count stairs, tree problems)

## Default arguments for scheme operators

```
(+ [0] [0])
(- [0] _)
(* [1] [1])
(/ [1] _)
```

## SQL

Filters out duplicate rows from all columns:

```
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

## SQL Query Order

```
5. SELECT ___
1. FROM ___
2. WHERE ___
3. GROUP BY ___
4. HAVING ___
6. ORDER BY ___
7. LIMIT ___
```

## Scheme Interpretation

/Screen Shot 2018-08-07 at 8.36.37 PM.png