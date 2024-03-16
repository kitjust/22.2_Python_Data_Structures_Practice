def intersection(L1, L2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    
	return list(set(L1) & set(L2))

	# Alternatively, use a comprehension:
	# set2 = set(L2)
	# return [val for val in L1 if val in set2]
