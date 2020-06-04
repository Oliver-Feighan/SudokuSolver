import random as rnd
import numpy as np
import numbers_check
import square_splitter

grid_start = [[0,0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0,0],
 			  [0,0,0,0,0,0,0,0,0],
	 		  [0,0,0,0,0,0,0,0,0],
		 	  [0,0,0,0,0,0,0,0,0]]

def fill_grid_first(grid):
	row_index = rnd.randrange(0, 9)
	col_index = rnd.randrange(0, 9)

	grid[row_index][col_index] = rnd.randrange(1, 10)

	return(grid)

def array_checker(array):
	test_array = []
	
	for i in array:
		test_array.append(i)

	while 0 in test_array:
		test_array.remove(0)

	if len(test_array) > len(set(test_array)):
		print(test_array)
		return True


def fill_grid_possibilities(grid):
	rows = grid
	cols = np.array(rows).transpose().tolist()
	squares = np.array(square_splitter.square_splitter(rows)).tolist()

	for i in rows:
		if array_checker(i):
			return

	for i in cols:
		if array_checker(i):
			return

	for i in squares:
		if array_checker(i):
			return

	possibilities = numbers_check.box_raster(rows, cols, squares)

	for i in possibilities:
		print(i)

	poss_row_index = rnd.randrange(0, 9)
	poss_col_index = rnd.randrange(0, 9)

	while len(possibilities[poss_row_index][poss_col_index]) == 1 and grid[poss_row_index][poss_col_index] != 0:
		print(possibilities[poss_row_index][poss_col_index])
		poss_row_index = rnd.randrange(0, 9)
		poss_col_index = rnd.randrange(0, 9)	

	print(possibilities[poss_row_index][poss_col_index])
	assert(grid[poss_row_index][poss_col_index] == 0)

	number = rnd.choice(possibilities[poss_row_index][poss_col_index])

	grid[poss_row_index][poss_col_index] = number

	return(grid)


grid_next = fill_grid_first(grid_start)

for n in range(40):
	print(n)
	grid_next = fill_grid_possibilities(grid_next)
	print(len(grid_next))
	for i in grid_next:
		print(i)

	print("-" * 20)