# Cheatsheet

> A record of useful test resources collected throughout the term.

## Interpreter

- `None` outputs nothing (literally nothing)
- `print(None)` outputs `None`
- `"string"` outputs `"string"`
- `print('string')` outputs `string`

## Partitions/Combinations

```python3
def count_partitions(n, m):
    if n == 0:
        return 1
    if n < 0 or m == 0:
        return 0

    return count_partitions(n-m, m) + count_partitions(n, m-1) # with m + without m
```

## Permutations
```python3
def count_k(n, k):
    if n == 0:
        return 1
    if n < 0:
        return 0

    # return count_k(n - 1, k) + count_k(n - 2, k) + ...
    total = 0
    for i in range(1, k+1):
        total += count_k(n - i, k)

    return total
```

## Lists

- `extend` does the same things `lst += [...]` but is different from `lst = lst + [...]`
- Copying in python is SHALLOW (so if you copy a list `lst2 = lst1[:]` and it has nested list items, those nested lists wil be shared between both lst1 and lst2)
- `.pop([index])`
- `.remove()` throws error if item is not found

/Screen Shot 2018-07-09 at 11.30.47 AM.png

## \<exp1\> `and` \<exp2\> `and` \<exp3\> `and` ...

> Evaluates to first false value. If none are false, evaluates to the last expression

### \<exp1\> `or` \<exp2\> `or` \<exp3\> `or` ...

> Evaluates to first true value. If none are true, evaluates to the last expression