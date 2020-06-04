def sudoku_printer(array):
	for i in range(len(array)):
		#print(i % 3 == 2)
		if (i % 3) != 0 or i == 0:
			print("%s %s %s|%s %s %s|%s %s %s|" % tuple(array[i]))

		else:
			print("-" * 18)
			print("%s %s %s|%s %s %s|%s %s %s|" % tuple(array[i]))
