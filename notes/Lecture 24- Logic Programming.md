# Lecture 24: Logic Programming

## Declarative programming

> In **declarative programming**, we specify the properties that a solution satisfies, instead of specifying the instructions to compute the solution

Instead of describing *how* to do the solution (imperative), we just describe *what* the solution should look like!

## Example:

/Screen Shot 2018-08-01 at 11.25.22 AM.png

Find a solution where:

- Each TA is assigned to a section
- Each section is assigned a TA
- TAs are available for the section they teach

## The Logic Language

/Screen Shot 2018-08-01 at 11.26.53 AM.png

## Variables

/Screen Shot 2018-08-01 at 11.29.58 AM.png

## Compound Queries

/Screen Shot 2018-08-01 at 11.32.25 AM.png

## Negation

/Screen Shot 2018-08-01 at 11.34.22 AM.png

## Compound Facts

/Screen Shot 2018-08-01 at 11.47.32 AM.png

## Hierarchal Facts

/Screen Shot 2018-08-01 at 11.49.03 AM.png

## Recursive facts

/Screen Shot 2018-08-01 at 11.52.44 AM.png

## Example Pt. 2: Assigning 6 TAs to Sections

```
(fact (available cameron 1))
(fact (available cameron 2))
(fact (available chae 2))
(fact (available chae 4))
(fact (available chris 3))
(fact (available chris 4))
(fact (available christina 1))
(fact (available christina 3))
(fact (available jennifer 2))
(fact (available jennifer 3))
(fact (available jennifer 4))
(fact (available jennifer 5))
(fact (available jenny 4))
(fact (available jenny 6))
(fact (available cameron 5))
(fact (available christina 6))

(fact (tas (cameron chae chris christina jennifer jenny)))
(query (tas (?first . ?rest)))
; first: cameron   rest: (chae chris christina jennifer jenny)

(fact (in ?item (?item . ?rest)))
(fact (in ?item (?first . ?rest))
      (in ?item ?rest))

(fact (assign-all () ()))
(fact (assign-all (?ta . ?tas) (?section . ?sections))
      (available ?ta ?section)
      (assign-all ?tas ?sections)
      (not (in ?section ?sections)))

(query (assign-all (cameron chae chris
                    christina jennifer jenny)
                   ?sections)

(query (assign-all ?tas ?sections)
       (tas ?tas))
```

## The Declarative Programming Trade-Off

- Declarative languages move the job of solving the problem over from the programmer to the interpreter
- However, building a problem solver is hard! We don’t know how to build a universal problem solver
- As a result, declarative languages usually only handle a subset of problems
- Many problems will still require careful thought and a clever approach from the programmer

/Screen Shot 2018-08-01 at 12.04.48 PM.png