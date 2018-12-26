# Lecture 14: Object-Oriented Programming

- Organizes modular programs that represent the real world
- Bundles data with related behavior
- A metaphor for computation using distributed state
    - Each object has its own local state
    - Each object also knows how to manage its own local state
    - Method calls are messages passed between objects
    - Several objects may all be instances of a common type
    - Different types may relate to each other

## Class

- Template for its instances
- All instances should have some same attributes and behaviors (not shared)
- All instances might have some shared behaviors (like a common method)
- All instances might also have shared characteristics (like a max limit)

## The Class Statement

A class statement creates a new class and binds that class to the current environment

Assignment & def statements in the <suite> create *class attributes*.

```
class <name>:
    <suite>

class Account:
    max_withdrawal = 10
    ...
    def deposit(...):
        ...
    def withdraw(...):
        ...
    ...
```

/Screen Shot 2018-07-16 at 11.27.12 AM.png

## Creating an instance

Idea: All bank accounts have a balance and an account holder. These are not shared across Accounts.

```
>>> a = Account('James')
>>> a.balance
0
>>> a.holder
'James'
```

*Constructor returns `None`, but the name `a` is bound to the new instance, not the Return value*

When a class is called:

1. A new instance of that class is created.
2. The `__init__` method of a class is called with the new object as its first argument (named self), along with additional arguments provided in the call expression.

```
class Account:
    ...
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    ...
```

/Screen Shot 2018-07-16 at 11.44.21 AM.png

## Object Identity

```
>>> a = Account(“James”)
>>> b = Account(“John”)
>>> c = Account(“James”)
```

```
>>> a is a
True
>>> a is not b
True
>>> c is a
False
```

```
>>> d = a
>>> d is a
True
```

## Dot Expressions

```
<expression>.<name>
```

*The <expression> can be any valid Python expression that evaluates to a class or instance. The <name> must be a simple name.*

To evaluate a dot expression:

1. Evaluate the <expression> to the left of the dot, which yields the object of the dot expression 
2. <name> is matched against the instance attributes of that object; if an attribute with that name exists, its value is returned
3. If not, <name> is looked up in the class, which yields a class attribute value
4. That value is returned unless it is a function, in which case a bound method is returned instead

```
Account.depost # -> <function>
a.depost       # -> <bound method>
```

## Methods and Functions

**Methods** are functions defined in the suite of a class statement.

However methods that are accessed through an instance will be **bound methods**. Bound methods couple together a function and the object on which that method will be invoked. This means that when we invoke bound methods, **the instance is automatically passed in as the first argument**.

## Invoking Methods
 
1. Invoking **class methods as a *bound method***:
    - Bound methods are accessed through the instance and implicitly pass the instance object in as the first argument of the method.
    - `<instance>.<method_name>(<arguments>)`
        - `a` gets passed in to the deposit function as the first argument
    - Ex. `a.deposit(5)`
2. Invoking **class methods as functions**:
    - We can use the class name to directly call a method. These follow our typical function call rules and nothing is implicitly passed in.
    - `<class_name>.<method_name>(<instance>, <arguments>)`
    - Ex.`Account.deposit(a, 5)`

## The `Account` Class

```
class Account:
    max_withdrawal = 10

    def __init__(self, account_holder):
        """Creates an instance of the Account class"""
        self.balance = 0
        self.holder = account_holder
	
    def deposit(self, amount):
        """Deposits amount to the account."""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Subtracts amount from the account."""
        if amount > self.max_withdrawal or amount > self.balance:
            return "Can’t withdraw this amount"
        self.balance -= amount
        return self.balance
```

## Accessing Attributes

Using `getattr`, we can look up an attribute **using a string** instead.

- getattr(<expression>, <attribute_name (string)>)
- getattr(a, 'balance') is the same as a.balance
- getattr(Account, 'balance') is the same as Account.balance

Using hasattr, we can check if an attribute exists.

- hasattr(<expression>, <attribute_name (string)>)
- hasattr(a, 'balance') returns True
- hasattr(Account, 'balance') returns False 

## Assigning attributes

```
<expression>.<name> = <value>
```

Change attributes for the object of that dot expression.

- If the expression evaluates to an **instance**: then assignment sets an instance attribute, even if it exists in the class.
- If the expression evaluates to a **class**: then assignment sets a class attribute
    - **THIS WILL EFFECT ALL INSTANCES RETROACTIVELY**