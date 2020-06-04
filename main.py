import reader
import square_splitter
import numbers_check
import sys
import numpy as np
import printer

array_rows = (reader.reader(sys.argv[1]))
array_cols = np.array(array_rows).transpose().tolist()
squares = np.array(square_splitter.square_splitter(array_rows)).tolist()
	
def make_int(array):
	for i in range(len(array)):
		numbers = array[i]
		numbers = list(map(int, numbers))
		array[i] = numbers

	return array

rows = make_int(array_rows)
cols = make_int(array_cols)
squares = make_int(squares)

iteration = 0 

while any(0 in x for x in rows) and iteration < 3:
	#print(iteration)
	#for i in rows:
	#	print(i)

	cols    = make_int(np.array(rows).transpose().tolist())
	squares = make_int(np.array(square_splitter.square_splitter(rows)).tolist())

	iteration += 1
	possibilites = numbers_check.box_raster(rows, cols, squares)

	change_count = 0
	for i in range(9):
		for j in range(9):
			if len(possibilites[i][j]) == 1:
				rows[i][j] = possibilites[i][j][0]
	#print("-" * 20)

if iteration == 100:
	print('failed, %s %s' % (iteration, sys.argv[1]))

else:
	print('success, %s %s' % (iteration, sys.argv[1]))

#print(iteration)

for i in possibilites:
	print(i)

print("original")
original_rows = make_int(reader.reader(sys.argv[1]))
printer.sudoku_printer(original_rows)
print("final")
printer.sudoku_printer(rows)