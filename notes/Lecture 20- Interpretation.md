# Lecture 20: Interpretation

## Translation

- Some languages are *compiled* (pre-translated), some are *interpreted* (translated on-the-fly)

## Interpreters

- An interpreter...
    - allows users (humans) to enter expressions in a particular language
    - translates the expressions in order to tell the computer to do things
    - presents the result of evaluating the expressions back to the user
- There are two languages involved:
    - **implemented language**: the language being interpreted
    - **implementing language**: the language the interpreter is implemented in

## Read-Eval-Print Loop

- Most interpreters are implemented as an infinite loop that
    - reads command line input
    - evaluates the expression
    - prints out its value

/Screen Shot 2018-07-25 at 11.18.30 AM.png

## Reading Input

- **Lexical analysis**: Turning the input string into a collection of tokens
    - A token is a single unit of the input string (literals, names, keywords, delimiters)
- **Syntactic analysis**: Turning tokens into a representation of the expression in the *implementing language*
    - The exact "representation" depends on the type of expression
    - Types of Scheme expressions: self-evaluating expressions, symbols, call expressions, special form expressions

/Screen Shot 2018-07-25 at 11.23.53 AM.png

## Representing Scheme primitive expressions

- **Self-evaluating** expressions (bools and nums)
    - Can just use Python bools and nums
- **Symbols**
    - Use Python strings

## Representing combinations

```
(<operator> <operand1> <operand2>)
```

**Combinations** are just Scheme lists containing an operator and operands.

/Screen Shot 2018-07-25 at 11.35.52 AM.png

/Screen Shot 2018-07-25 at 11.39.00 AM.png

### Special case: quote

The special ' syntax gets converted by the reader into a quote expression, which is a list with 2 elements, represented as a Pair.

/Screen Shot 2018-07-25 at 11.43.49 AM.png

## Read-Eval-Print Loop

/Screen Shot 2018-07-25 at 11.51.34 AM.png

## Evaluation

Rules for evaluating an expression depends on the expression's type

Types of Scheme expressions: self-evaluating expressions, symbols, call expressions, special form expressions

/Screen Shot 2018-07-25 at 11.58.44 AM.png

*Eval takes in one argument besides the expression itself: **The current environment.***

### Frames and environments

When evaluating expressions, the current  **environment** consists of the current frame, its parent frame, and all its ancestor frames until the Global Frame.

### Frames in our interpreter

- Frames are represented in our interpreter as instances of the Frame class 
- Each Frame instance has two instance attributes:
    - bindings: a dictionary that binds Scheme symbols (Python strings) to Scheme values
    - parent: the parent frame, another Frame instance
- The evaluator needs to know the current environment, given as a single Frame instance, in order to look up names in expressions.

### Evaluating primitive expressions

**Self-evaluating expressions:** These expressions evaluate to themselves.

**Symbols:**
1. Look in the current frame for the symbol. If it is found, return the value bound to it.
2. If it is not found in the current frame, look in the parent frame. If it is not found in the parent frame, look in its parent frame, and so on.
3. If the global frame is reached and the name is not found, raise a SchemeError.

/Screen Shot 2018-07-25 at 12.05.57 PM.png

### Evaluating combinations

```
(<operator> <operand1> <operand2> …)
```

- If the operator is a symbol and is found in the dictionary of special forms, the combination is a special form (and has special rules)
- Otherwise, the combination is a call expression
    - Step 1. Evaluate the operator to get a procedure. (recursive calls to eval)
    - Step 2. Evaluate all of the operands from left to right. (recursive calls to eval)
    - Step 3. Apply the procedure to the values of the operands.

## Types of Procedures

- A **built-in procedure** is a procedure that is predefined in our Scheme interpreter, e.g. +, list, modulo, etc.
    - Each built-in procedure has a corresponding Python function that performs the appropriate operation.
    - In our interpreter -- instances of the BuiltinProcedure class
- A **user-defined procedure** is a procedure defined by the user, either with a lambda expression or a define expression.
    - Each user-defined procedure has (1) a list of formal parameters, (2) a body (which is a Scheme list), and (3) a parent frame.
    - In our interpreter -- instances of the LambdaProcedure class

### Built-in procedures

**Applying built-in procedures:**

- Call the Python function that implements the built-in procedure on the arguments.

### User-defined procedures

**Applying** user-defined procedures:

- Step 1. Open a new frame whose parent is the parent frame of the procedure being applied.
- Step 2. Bind the formal parameters of the procedure to the arguments in the new frame.
- Step 3. Evaluate the body of the procedure in the new frame.

/Screen Shot 2018-07-25 at 12.19.42 PM.png

## The Evaluator

/Screen Shot 2018-07-25 at 12.22.19 PM.png

/Screen Shot 2018-07-25 at 12.31.40 PM.png

/Screen Shot 2018-07-25 at 12.31.47 PM.png