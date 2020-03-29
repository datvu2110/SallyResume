def firstDuplicate(a):
	lst = []
	for each in a:
		if each not in lst:
			lst.append(each)
		else:
			return each
	if len(lst) == len(a):
		return -1



a = firstDuplicate([2, 4, 3, 5, 1])
print(a)