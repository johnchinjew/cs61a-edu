# Lecture 19: Tail Recursion

## Streams (review)

Streams are like **lazy** Scheme lists: the rest is computed only when needed

## Recursion v. Iteration

- In Python, a new frame is opened for each recursive call before the current one is closed; this results in more space consumption
- However, iterative solutions often have constant space complexity

## Scheme Tail Recursion ("Iterative recursion")

- In Scheme, **a frame can be removed** if there is **no further work to be done**
- A procedure is tail recursive if **every** recursive call is a **tail call**
    - A **tail call** is a call expression in a **tail context**
        - The following are examples of tail contexts:
            - The last body subexpression in a lambda (a function)
            - The consequent and alternative in a tail context if
            - All non-predicate sub-expressions in a tail context cond
            - The last sub-expression in a tail context and, or, begin, let

```
1 (define (fact-alt n k)
2	 (if (= n 0)
3		 k
4		 (fact-alt (- n 1) (* k n))
5	 )
6 )
```

- This function has a constant space consumption!

### Scheme "Iteration"

/Screen Shot 2018-07-24 at 11.43.26 AM.png

/Screen Shot 2018-07-24 at 11.43.32 AM.png

## Example: Length

/Screen Shot 2018-07-24 at 12.06.06 PM.png

## Example: Map

/Screen Shot 2018-07-24 at 12.07.20 PM.png