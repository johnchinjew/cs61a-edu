## HIGHER ORDER FUNCTIONS ##

def do_n_then_again(n, x):
	"""
	>>> do_n = do_n_then_again(1, 2)
	>>> do_n(lambda x: x * x)
	4 # (2 * 2)
	>>> do_n = do_n_then_again(3, 2)
	>>> do_n(lambda x: x+2)(lambda x: x*x)(lambda x: -x)
	-4096 # (((2 + 2 + 2 + 2)^2)^2) * -1
	"""
	def do_n(f):
		if n == 1:
			return f(x)
		new_x = x
		for _ in range(n):
			new_x = f(new_x)
		return do_n_then_again(n-1, new_x)
	return do_n

## TREE RECURSION ##

def contains_skip_sum(n, lst):
	"""Returns whether lst contains elements which sum n. But elements cannot be sequential."""
	if n == 0:
		return True
	if not lst:
		return False
	with_first = contains_skip_sum(n - lst[0], lst[2:])
	without_fist = contains_skip_sum(n, lst[1:])
	return with_first or without_first

## TREES ##

def replace_with_sum(t):
	if is_leaf(t):
		return tree(label(t))
	new_branches = [replace_with_sum(b) for b in branches(t)]
	branch_sum = sum(label(b) for b in new_branches)
	return tree(label(t) + branch_sum, new_branches)

def closest(t):
	"""Returns the smallest difference between a root node and the sum of the children trees."""
	diff = abs(label(t) - sum(label(b) for b in branches(t)))
	return min([diff] + [closest(b) for b in branches(t)])
