# Lecture 22: SQL I

- Declarative programming language

## Databases, SQL, and Tables

- **Database**: A structured set of data in computer
- **Database management systems (DBMS)**: the software that creates software and manages databases
- **Structured Query Language**: a programming language that interacts with the DBMS

A **table** is a collection of records, which are rows that have a value for each column

/Screen Shot 2018-07-30 at 11.21.08 AM.png

## Declarative vs Imperative Programming

- Python & Scheme are **imperative programming languages**
    - The "program" describes the computation process
- SQL is a **declarative programming language**
    - A "program" is a description of the desired result

## Structured Query Language (SQL)

- `SELECT` statement creates a new table, from scratch or by projecting a table
- `CREATE TABLE` statement gives a global name to a table
- Others: `DELETE`, `INSERT`, `UPDATE`, etc...

## `SELECTING`ing Value Literals

- A SELECT statement always includes a comma-separated list of column descriptions.
- A column description is an expression, optionally followed by AS and a column name.

```
SELECT [expression] AS [name], [expression] AS [name], ... ;
```

- SELECTing literals CREATEs a one-row table.
- The UNION of two SELECT statements is a table containing the rows of both of their results.

```
SELECT "delano" AS parent,	"herbert" AS child UNION
SELECT "abraham",				"barack"			  UNION
SELECT "abraham",				"clinton"		  UNION
SELECT "fillmore",			"abraham"		  UNION
SELECT "fillmore",			"delano"			  UNION
SELECT "fillmore",			"grover"			  UNION
SELECT "eisenhower",			"fillmore";
```

## Naming Tables

A `CREATE TABLE` statement gives the result a name.

```
    CREATE TABLE [name] AS [SELECT statements];
```

```
CREATE TABLE parents AS
  SELECT "delano" AS parent,	"herbert" AS child UNION
  SELECT "abraham",			"barack"			  UNION
  SELECT "abraham",			"clinton"		  UNION
  SELECT "fillmore",			"abraham"		  UNION
  SELECT "fillmore",			"delano"			  UNION
  SELECT "fillmore",			"grover"			  UNION
  SELECT "eisenhower",		"fillmore";
```

## Projecting Tables

- A `SELECT` statement can specify an input table using a `FROM` clause.
- A subset of the rows of the input table can be selected using a `WHERE` clause.
- Remaining rows don’t have an order (or at least not in the scope of this course), so ordering over the remaining rows can be declared using an ORDER BY clause.
- Column descriptions determine how each input row is projected to a result row:


```
SELECT [columns] FROM [table] WHERE [condition] ORDER BY [order] [ASC/DESC] LIMIT [number];
```

---

## Arithmetic in `SELECT` Expressions

- In a SELECT expression, column names evaluate to row values.
- Arithmetic expressions can combine row values and constants

```
CREATE TABLE restaurant AS
  SELECT 101 AS "table", 2 AS single	,  2 AS couple UNION
  SELECT 102 		, 0			,  3			  UNION
  SELECT 103 		, 4			,  1;
```

## Arithmetic Example: Ints

/Screen Shot 2018-07-30 at 11.53.45 AM.pns

```
SELECT word, one + two + four + eight AS value FROM ints ORDER BY value;
```

```
SELECT word FROM ints 
WHERE one + two/2 + four/4 + eight/8 = 1;
```

---

## Joining Tables

```
CREATE TABLE parents AS
  SELECT "delano" AS parent,	"herbert" AS child UNION
  SELECT "abraham",			"barack"			  UNION
  SELECT "abraham",			"clinton"		  UNION
  SELECT "fillmore",			"abraham"		  UNION
  SELECT "fillmore",			"delano"			  UNION
  SELECT "fillmore",			"grover"			  UNION
  SELECT "eisenhower",		"fillmore";
```

Two tables A & B are joined by a comma to yield all combinations of a row from A & a row from B. This is known as the cross product and will give num_rows in A * num_rows in B output rows.

/Screen Shot 2018-07-30 at 12.12.25 PM.png

## Aliases and Dot Exprs

Two tables may share a column name; dot expressions and aliases disambiguate column values.

```
SELECT [columns] FROM [table] WHERE [condition] ORDER BY [order];
```

[table] is a comma-separated list of table names with optional aliases.

Example:

```
SELECT a.child AS first, b.child AS second FROM parents AS a, parents AS b WHERE a.parent = b.parent AND a.child < b.child;
```

*We need to get rid of duplicates because pairs of siblings appear twice. We can do this by enforcing an arbitrary ordering, a.child < b.child alphabetically. Then we get the two columns we want.*

## Joining Multiple Tables

```
CREATE TABLE grandparents AS
  SELECT a.parent AS grandog, b.child AS granpup
  FROM parents AS a, parents AS b
  WHERE b.parent = a.child;
```

/Screen Shot 2018-07-30 at 12.24.07 PM.png

---

## String Exprs

```
sqlite> SELECT "hello," || " world";
hello, world
sqlite> SELECT name || " dog" FROM dogs;
abraham dog
barack dog
clinton dog
delano dog
eisenhower dog
fillmore dog
grover dog
herbert dog
```