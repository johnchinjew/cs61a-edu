# Lecture 25: Dynamic Programming

## Memoization

- Some procedures perform a lot of repeated work
- Instead of repeating this work, we can remember the results

## Ex. Fib

- Keep a cache of all of our work so far
- If we have already computed a particular Fibonacci number, we can retrieve it from the cache

```
1 def fib_memo(n):
2	 cache = {}
3	 cache[0], cache[1] = 0, 1

4	 def mem(n):
5		 if n not in cache:
6			 cache[n] = mem(n - 2) + mem(n - 1)
7		 return cache[n]

8	 return mem(n)
```

## Dynamic Programming

> Identifying subproblems and solving subproblems in the order of increasing complexity to avoid repeating work

- Do the easier stuff first
- Build up to the larger problem

1. Identify the subproblems
2. Strategize order of solving the subproblems

## Ex. Fib (w/ D.P.)

/Screen Shot 2018-08-02 at 11.35.58 AM.png

## Longest Common Subsequence

/Screen Shot 2018-08-02 at 11.46.04 AM.png

## LCS Solution 1

/Screen Shot 2018-08-02 at 11.46.23 AM 1.png

/Screen Shot 2018-08-02 at 11.51.08 AM.png

## LCS Solution 2 w/ Indexing

/Screen Shot 2018-08-02 at 11.57.28 AM.png

/Screen Shot 2018-08-02 at 11.57.34 AM.png

/Screen Shot 2018-08-02 at 11.58.03 AM.png

## LCS Solution 3 w/ Memoization

Idea: We should perform this *work once*, and *reuse the results*

```
1 def lcs(word1, word2):
2	 cache = {}

3	 def helper(i, j):
4		 if (i, j) in cache:
5			 return cache[(i, j)]

6		 if i == len(word1) or j == len(word2):
7			 cache[(i, j)] = 0
8		 elif word1[i] == word2[j]:
9	 		 cache[(i, j)] = 1 + helper(i+1, j+1)
10		 else:
11			 cache[(i, j)] = max(helper(i,j+1), helper(i+1,j))
12		 return cache[(i, j)]

13	 return helper(0, 0)
```

/Screen Shot 2018-08-02 at 12.01.18 PM.png

## LCS with Dynamic Programming

/Screen Shot 2018-08-02 at 12.20.50 PM.png

/Screen Shot 2018-08-02 at 12.21.42 PM.png

/Screen Shot 2018-08-02 at 12.25.10 PM.png

/Screen Shot 2018-08-02 at 12.24.55 PM.png

High level overview of code:

- Make a table from a list of lists
- Have indices that decrement from the lengths of the words to 0
    - Fill in table as we go
    - Discard old column when we fill in a new column
    - Add a new initialized column to the front of the table


```
def lcs_len_dp_opt(word1, word2):
    """
    DP implementation of longest common subsequence (len). Remove old columns.

    >>> lcs_len_dp_opt("dog", "")
    0
    >>> lcs_len_dp_opt("dog", "cat")
    0
    >>> lcs_len_dp_opt("louis", "gucci")  # ui
    2
    >>> lcs_len_dp_opt("romeo", "othello")  # oeo
    3
    >>> lcs_len_dp_opt("beamer", "bentley")  # bee
    3
    """
    if len(word1) > len(word2):
        word1, word2 = word2, word1

    empty_column1 = [[0 for _ in range(len(word1) + 1)]]
    empty_column2 = [[0 for _ in range(len(word1) + 1)]]
    columns = empty_column1 + empty_column2
    i, j = len(word1), len(word2) - 1
    while j >= 0:
        while i >= 0:
            if i == len(word1):
                columns[0][i] = 0
            elif word1[i] == word2[j]:
                columns[0][i] = 1 + columns[1][i + 1]
            else:
                columns[0][i] = max(columns[0][i + 1], columns[1][i])
            i -= 1
        columns.pop(1)
        columns.insert(0, [0 for _ in range(len(word1) + 1)])
        i = len(word1)
        j -= 1
    return columns[1][0]
```