# Lecture 08: Tree Recursion

/Screen Shot 2018-06-28 at 11.48.29 AM.png

## Recursion vs Iteration

- In theory, any recursive func can be written iteratively, and vice versa
- Tree recursive procedures are difficult to write iteratively
- Tree recursion is best for trying multiple possibilities at the same time

## Tree recursion

> Makes multiple recursive calls and explores different choices

*Use tree recursion if...*

1. Answer depends on multiple previous numbers
2. At each step, we need to consider multiple cases

## Count Partitions

*Goal: Count the number of ways to give out n (> 0) pieces of chocolate if nobody can have more than m (> 0) pieces.*

```
>>> count_part(6, 4) # count the ways you can distribute (or partition) 6 pieces of chocolate so that no body has more than 4 pieces
9
```

/Screen Shot 2018-06-28 at 12.05.14 PM.png

/Screen Shot 2018-06-28 at 12.28.35 PM.png

```
def count_part(n, m):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if m == 0:
        return 0
    return count_part(n-m, m) + count_part(n, m-1)
```