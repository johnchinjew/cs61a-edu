# Lecture 11: Growth

## Time complexity

### Factors example

/Screen Shot 2018-07-05 at 11.21.15 AM.png

- Each modulus operation takes a bit of time
- When `n` is small, the difference between *n* and *sqrt(n)* is small
- When `n` is large, the difference can be huge

## Space Consumption

- Which environment frames must we keep during evaluation
- Values and frames in active environments consume memory
- Memory that is used for other values and frames can be recycled

### Fibonacci example of "Active Frames"

/Screen Shot 2018-07-05 at 11.26.24 AM.png

## Orders of Growth

> A method for bounding the resources used by a function by the "size" of the input

- **n** — the size of the problem
- **R(n)** — measurement fo some resource used (time or space)

/Screen Shot 2018-07-05 at 11.30.24 AM.png

### Properties

#### Constant

**Constant** terms do not affect the order of growth

/Screen Shot 2018-07-05 at 11.35.50 AM.png

#### Log

The base of a **logarithm** does not affect order of growth

/Screen Shot 2018-07-05 at 11.35.40 AM.png

#### Lower-order terms

**Lower-order terms**: the fastest-growing part of the computation dominates

- As *n* gets very large, you don't "feel" the lower-order terms, you only feel the effect of the largest growing term

/Screen Shot 2018-07-05 at 11.36.41 AM.png

#### Nesting

> When an inner process is repeated for each step in an outer process, multiply the steps in the outer and inner process

/Screen Shot 2018-07-05 at 11.43.11 AM.png

*before multiplying, check to make sure that both processes run to completion and that neither terminate early*

### Factors example

(with the new formalization)

/Screen Shot 2018-07-05 at 11.41.21 AM.png

## Exponentiation

/Screen Shot 2018-07-05 at 12.08.37 PM.png

/Screen Shot 2018-07-05 at 12.16.14 PM.png

## Comparing Orders of Growth

/Screen Shot 2018-07-05 at 12.24.03 PM.png

## Important sums

/Screen Shot 2018-07-05 at 12.30.11 PM.png

/Screen Shot 2018-07-05 at 12.30.18 PM.png