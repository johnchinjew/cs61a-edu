# Lecture 15: OOP 2 Inheritance & Output

## Inheritance

```
class <Class Name>(<Superclass Name>):
    <suite>
```

- The more specialized class is a **subclass** of the general class and the general class a **superclass**
- The **subclass** *inherits* all class attributes of the **superclass**.
- The subclass can *override* attributes to specify how it is different from the superclass.

## New dot expression rules

```
<expression>.<name>
```

*How to evaluate:*
1. Evaluate <expression>, which yields an object.
2. <name> is matched against the instance attributes of that object; if an attribute with that name exists, its value is returned.
3. If not, the name is looked up in the class, which yields a class attribute value. If it is not found in the class, look in any superclasses.
4. That value is returned unless it is a function, in which case a bound method is returned instead.

```
>>> luxio = ElectricType('Luxio', 'Tammy')
>>> luxio.hp     # Found in instance
50
>>> luxio.damage # Found in Pokemon class
40
>>> luxio.basic_attack # Found in ElectricType class
'thunder shock'
```

## Calling superclass methods

```
class SubClass(SuperClass):
    def some_method(self):
        SuperClass.some_method(self)
```

## Designing for inheritance

- Don't repeat yourself; use existing implementations
- Attributes that have been overridden are still accessible via class objects
- Look up attributes on instances when possible to allow for more specialization

/Screen Shot 2018-07-17 at 12.26.41 PM.png

## Magic methods

Python classes can implement special methods that allow the object to be treated like certain built-in types.

These methods start and end with double underscores.

For example: `__init__`

## Objects as output

- The `__repr__` method defines a formal string representation of an object.
- The `__str__` method defines an informal readable representation of an object.

```
class Account:
	...

	def __repr__(self):
		"""Returns 'Account(<holder>)'."""
		return "Account('" + self.holder + "')"

	def __str__(self):
		"""Returns a string containing holder and balance."""
		return self.holder + "'s account: balance = " + \ 
              str(self.balance))
```

```
>>> a = Account('Tammy')
>>> a.__repr__()
Account('Tammy')
>>> a.__str__()
Tammy's account: balance = 0
>>> repr(a)							# Calls a.__repr__()
Account('Tammy')
>>> str(a)							# Calls a.__str__()
Tammy's account: balance = 0
>>> a     							# Prints a.__repr__()
Account('Tammy')
>>> print(a) 							# Prints a.__str__()
Tammy's account: balance = 0
```