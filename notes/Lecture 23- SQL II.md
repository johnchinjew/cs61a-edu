# Lecture 23: SQL II

## Review

/Screen Shot 2018-07-31 at 11.15.49 AM.png

/Screen Shot 2018-07-31 at 11.16.04 AM.png

## Aggregation

**Aggregation** is the process of doing operations on groups of rows instead of just a single row

SQL provides **aggregate functions** whose return values can be used as entries in a column

/Screen Shot 2018-07-31 at 11.47.53 AM.png

/Screen Shot 2018-07-31 at 11.48.20 AM.png

## Groups

Default: aggregation performed over all rows

However, we can specify certain groups of rows based on values in a particular column

```
SELECT fur, AVG(age) AS avg_age FROM dogs GROUP BY fur;
```

/Screen Shot 2018-07-31 at 11.58.30 AM.png

You can `GROUP BY` any valid SQL expression, which includes using multiple
column names and operators.

```
SELECT [columns] FROM [table] WHERE [condition] ORDER BY [order] [ASC/DESC] LIMIT [number] GROUP BY [expresssion];
```

A single group consists of all rows for which [expression] evaluates to the same value.

The output table will have **one row** per group.

## Examples

```
select parent, avg(age) as avg_age from parents, dogs where child = name group by parent;
```

```
select count(age) as count from dogs group by age % 2 = 0;
```

## Filtering Groups

To filter groups, use the HAVING [condition] clause!

A query that finds the average age of dogs for each fur type if there is at least one dog with that fur type.

```
SELECT fur, AVG(age) AS avg_age FROM dogs GROUP BY fur HAVING COUNT(*) > 1;
```

## Mutating Tables

To create an empty table, specify name and column names, and possible defaults

/Screen Shot 2018-07-31 at 12.26.15 PM.png

To remove a table from database:

```
DROP TABLE [IF EXISTS] [name];
```

## Inserting records

To insert rows into a table:

```
INSERT INTO [table]([columns]) VALUES([values]), ([values]);
```

/Screen Shot 2018-07-31 at 12.27.39 PM.png

## Updating records

To update existing entries in a table

```
UPDATE [table] SET [column] = [expression] WHERE [condition];
```

To delete existing rows in a table:

```
DELETE FROM [table] WHERE [condition];
```

/Screen Shot 2018-07-31 at 12.29.04 PM.png