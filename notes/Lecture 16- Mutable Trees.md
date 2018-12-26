# Lecture 16: Mutable Trees

```
### ADT Based Representation of a Tree ###
def tree(label, branches=[]):
    """
    >>> t_adt = tree(3, [tree(2, [tree(5)]), tree(4)])
    >>> label(t_adt) = 6
    Traceback (most recent call last):
        ...
    SyntaxError: can't assign to function call
    """
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]


### Class Based Representation of a Tree ###
class Tree:
    """
    Class based representation of a tree.

    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True

    >>> t_class = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t_class.label = 6

    >>> t = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(8, [Tree(7), Tree(9)])])
    >>> 7 in t
    True
    >>> 10 in t
    False
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + '\n'
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False


class BST:
    """
    Class based representation of a binary search tree (BST).
    
    >>> bst1 = BST(4, BST(2, BST(1)))
    >>> bst1.max()
    4
    >>> bst1.min()
    1
    >>> bst2 = BST(6, BST(2, BST(1), BST(4)), BST(7, BST.empty, BST(9)))
    >>> bst2.max()
    9
    >>> bst2.min()
    1
    >>> 9 in bst2
    True
    >>> 10 in bst2
    False
    >>> bst3 = BST(6, BST(2, BST(1), BST(4)), BST(8, BST(7), BST(9)))
    >>> 7 in bst3
    True
    >>> 10 in bst3
    False
    """
    empty = ()
    def __init__(self, label, left=empty, right=empty):
        assert left is BST.empty or isinstance(left, BST)
        assert right is BST.empty or isinstance(right, BST)

        self.label = label
        self.left, self.right = left, right

        if left is not BST.empty:
            assert left.max() <= label
        if right is not BST.empty:
            assert label < right.min()

    def is_leaf(self):
        return self.left is BST.empty and self.right is BST.empty

    def __repr__(self):
        if self.is_leaf():
            return 'BST({0})'.format(self.label)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BST({0}, {1})'.format(self.label, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BST.empty' 
            template = 'BST({0}, {1}, {2})'
            return template.format(self.label, left, right)

    def max(self):
        """Returns max element in BST."""
        if self.right is BST.empty:
            return self.label
        return self.right.max()

    def min(self):
        """Returns min element in BST."""
        if self.left is BST.empty:
            return self.label
        return self.left.min()

    def __contains__(self, e):
        if self.label == e:
            return True
        elif e > self.label and self.right is not BST.empty:
            return e in self.right
        elif self.left is not BST.empty:
            return e in self.left
```

/Screen Shot 2018-07-18 at 11.29.37 AM.png

/Screen Shot 2018-07-18 at 11.29.25 AM.png

*`print` makes use of `__str__` method*

/Screen Shot 2018-07-18 at 11.33.04 AM.png

/Screen Shot 2018-07-18 at 11.36.30 AM.png

*invoke by using `in` operator*

## Binary Search Tree (BST)

- Each node has at **most 2 branches**
- Left branch elements are ALL **less than or equal** to label
- Right branch elements are all **greater than** label
- Branches are also BSTs

*Code above*

## BST Max

- If right branch is empty, then the current label is the max
- Otherwise keep going right

*Code above*

## Time Complexity

/Screen Shot 2018-07-18 at 12.14.43 PM.png