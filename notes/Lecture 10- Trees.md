# Lecture 10: Trees

## Sequence Aggregation

- **Aggregate** means to reduce multile values to one
- An **Iterable** is an object capable of returning its members one at a time

Some built in functions take iterable args and aggregate them to one value

- `sum(iterable [, start])` (Doesn't work on strings)
- `max(iterable [, key=func])` (largest after applying func)
- `min` - same as max, but returns smallest value

More

- `bool(any_value) -> bool` (Returns whether any_vale is True/False)
- `all(iterable) -> bool` (Returns True if all elems in iterable are True)
    - Returns True if empty iterable
- `any(iterable) -> bool` (Returns True if any elem in iterable is True)
    - Return False if iterable is empty

## Trees

### Tree Abstraction

/Screen Shot 2018-07-03 at 11.42.41 AM.png

(Trees need not be binary)

#### Recursive definition

- A **tree** has a **root** and a list of **branches**
- Each branch is a tree
- A tree with zero branches is called a **leaf**

#### Relative description

- Each location in a tree is called a node
- Each **node** has a label (any value)
- One node can be the **parent/child** of another

## Tree ADT

/Screen Shot 2018-07-03 at 11.46.29 AM.png

## Tree Processing

### Using recursion

Just like checking for whether the branches were trees, we also use recursion in tree processing functions.

1. The base case is the smallest version of the problem, many times if its a leaf (though not always).
2. The recursive call happens on smaller subproblems, which tend to be branches (though not always).
3. We use the recursive calls with some type of aggregation afterwards to get our final solution.

/Screen Shot 2018-07-03 at 12.00.57 PM.png

```python3
def count_nodes(t):  
    if is_leaf(t):
        return 1
    total = 1
    for b in branches(t):
        total += count_nodes(b)
    return total

def count_nodes(t):
    total = 1
    for b in branches(t):
        total += count_nodes(b)
    return total

def count_nodes(t):
    return 1 + sum([count_nodes(b) for b in branches(t)])
```

### List the leaves

```python3
def list_leaves(t):
    if is_leaf(t):
        return [label(t)]
    return sum([list_leaves(b[t]) for b in branches(t)], [])
```

## How does tree problems that use recursion (a subset of tree recursion problems) work?

/Screen Shot 2018-07-03 at 12.17.35 PM.png

---

## Implementing `print_tree`

```python3
def print_tree(t, indent=0):
    if is_leaf(t):
        print(' ' * indent + str(label(t)))
    else:
        print((' ' * indent) + str(label(t)))
        for b in branches:
            print_tree(b, indent=indent+1)
```

## Creating Trees

### Square Tree

```python3
def square_tree(t):
    if is_leaf(t):
        return tree(label(t) ** 2)
    squared_branches = []
    for b in branches(t):
        squared_branches += [square_tree(branches(t))]
    return tree(label(t) ** 2, squared_branches)
```

## Fib Tree

```python3
def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    l, r = fib_tree(n-2), fib_tree(n-1)
    fib_n = label(l) + label(r)
    return tree(fib_n, [l, r])
```