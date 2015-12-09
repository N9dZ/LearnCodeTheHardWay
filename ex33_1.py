def p_lists(a,b):
	i = 0
	numbers = []
	# range(start_in, end_out, value_add)
	for i in range(i, a, b):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num,