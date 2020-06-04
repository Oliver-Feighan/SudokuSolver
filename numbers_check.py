import square_splitter
import numpy as np

def box_raster(rows, cols, squares):
	possibilities = [[list(range(1,10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10))],
					 [list(range(1,10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10))],
					 [list(range(1,10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10))],
					 [list(range(1,10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10))],
					 [list(range(1,10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10))],
					 [list(range(1,10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10))],
					 [list(range(1,10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10))],
					 [list(range(1,10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10))],
					 [list(range(1,10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10)),list(range(1, 10))]]


	box_indicies = [[[0,0, 0], [0,1, 0], [0,2, 0], [0,3, 1], [0,4, 1], [0,5, 1], [0,6, 2], [0,7, 2], [0,8, 2]],
					[[1,0, 0], [1,1, 0], [1,2, 0], [1,3, 1], [1,4, 1], [1,5, 1], [1,6, 2], [1,7, 2], [1,8, 2]],
					[[2,0, 0], [2,1, 0], [2,2, 0], [2,3, 1], [2,4, 1], [2,5, 1], [2,6, 2], [2,7, 2], [2,8, 2]],
					[[3,0, 3], [3,1, 3], [3,2, 3], [3,3, 4], [3,4, 4], [3,5, 4], [3,6, 5], [3,7, 5], [3,8, 5]],
					[[4,0, 3], [4,1, 3], [4,2, 3], [4,3, 4], [4,4, 4], [4,5, 4], [4,6, 5], [4,7, 5], [4,8, 5]],
					[[5,0, 3], [5,1, 3], [5,2, 3], [5,3, 4], [5,4, 4], [5,5, 4], [5,6, 5], [5,7, 5], [5,8, 5]],
					[[6,0, 6], [6,1, 6], [6,2, 6], [6,3, 7], [6,4, 7], [6,5, 7], [6,6, 8], [6,7, 8], [6,8, 8]],
					[[7,0, 6], [7,1, 6], [7,2, 6], [7,3, 7], [7,4, 7], [7,5, 7], [7,6, 8], [7,7, 8], [7,8, 8]],
					[[8,0, 6], [8,1, 6], [8,2, 6], [8,3, 7], [8,4, 7], [8,5, 7], [8,6, 8], [8,7, 8], [8,8, 8]]]

	for i in box_indicies:
		for j in i:
				row_index    = j[0]
				col_index    = j[1]
				square_index = j[2]

				box_checker(rows, row_index, col_index, possibilities)
				row_checker(rows, row_index, col_index, possibilities)
				col_checker(cols, row_index, col_index, possibilities)
				square_checker(squares, row_index, col_index, square_index, possibilities)
	
	poss_rows = possibilities
	poss_cols = np.array(possibilities).transpose().tolist()
	poss_squares = np.array(square_splitter.square_splitter(possibilities)).tolist()

	is_singular = 0

	for row in poss_rows:
		for lists in row:
			if len(lists) != 1:
				is_singular += 1

	if is_singular == 0:
		return(possibilities)


	for i in box_indicies:
		for j in i:
				row_index    = j[0]
				col_index    = j[1]
				square_index = j[2]

				for number in range(1, 10):
					row_possibilities_checker(number, poss_rows[row_index], row_index, col_index, possibilities)
					col_possibilities_checker(number, poss_cols[col_index], row_index, col_index, possibilities)
					squares_possibilities_checker(number, poss_squares[square_index], row_index, col_index, possibilities)

	for i in box_indicies:
		for j in i:
				row_index    = j[0]
				col_index    = j[1]
				square_index = j[2]
		
				row_naked_pair    = naked_pair_check(poss_rows[row_index])
				col_naked_pair    = naked_pair_check(poss_cols[col_index])
				square_naked_pair = naked_pair_check(poss_squares[square_index])

				if row_naked_pair:
					remove_naked_pair_numbers(row_index, col_index, row_naked_pair, possibilities)
				if col_naked_pair:
					remove_naked_pair_numbers(row_index, col_index, col_naked_pair, possibilities)
				if square_naked_pair:
					remove_naked_pair_numbers(row_index, col_index, square_naked_pair, possibilities)

	for i in box_indicies:
		for j in i:
				row_index    = j[0]
				col_index    = j[1]
				square_index = j[2]
		
				row_pointing_pair = pointing_pair_check(row_index, col_index, poss_rows[row_index], poss_squares[square_index], possibilities)
				col_pointing_pair = pointing_pair_check(row_index, col_index, poss_cols[col_index], poss_squares[square_index], possibilities)
				
				#if row_pointing_pair:
					#if row_pointing_pair[1].index(2) == row_index % 3:
					#	print('here', possibilities[row_index][col_index])
					#	print(possibilities[row_index], row_pointing_pair[0])
						#remove_pointing_pair_numbers(row_index, col_index, row_naked_pair, possibilities)
				#if col_pointing_pair:
					#remove_pointing_pair_numbers(row_index, col_index, col_naked_pair, possibilities)
				#if square_naked_pair:
				#	remove_naked_pair_numbers(row_index, col_index, square_naked_pair, possibilities)


	return possibilities

def box_checker(rows, row_index, col_index, possibilities):
	if rows[row_index][col_index] != 0:
		possibilities[row_index][col_index] = [rows[row_index][col_index]]

def row_checker(rows, row_index, col_index, possibilities):
	numbers = possibilities[row_index][col_index]
	for i in range(1,10):
		if i in rows[row_index] and i in numbers and len(numbers) > 1:
			possibilities[row_index][col_index].remove(i)

def col_checker(cols, row_index, col_index, possibilities):
	numbers = possibilities[row_index][col_index] 
	for i in range(1, 10):
		if i in cols[col_index] and i in numbers and len(numbers) > 1:
			possibilities[row_index][col_index].remove(i)

def square_checker(squares, row_index, col_index, square_index, possibilities):
	numbers = possibilities[row_index][col_index] 
	for i in range(1, 10):
		if i in squares[square_index] and i in numbers and len(numbers) > 1:
			possibilities[row_index][col_index].remove(i)

def row_possibilities_checker(number, row, row_index, col_index, possibilities):
	poss_numbers = possibilities[row_index][col_index]
	if sum([len(i) for i in row]) != len(row):
		count = sum([i.count(number) for i in row])
	else:
		count = 1

	if number in poss_numbers and len(poss_numbers) != 1 and count == 1:
			possibilities[row_index][col_index] = [number]

def col_possibilities_checker(number, col, row_index, col_index, possibilities):
	poss_numbers = possibilities[row_index][col_index]
	if sum([len(i) for i in col]) != len(col):
		count = sum([i.count(number) for i in col])
	else:
		count = 1

	if number in poss_numbers and len(poss_numbers) != 1 and count == 1:
			possibilities[row_index][col_index] = [number]

def squares_possibilities_checker(number, square, row_index, col_index, possibilities):
	poss_numbers = possibilities[row_index][col_index]
	if not isinstance(square[0], int):
		count = sum([i.count(number) for i in square])
	else:
		count = 1

	if number in poss_numbers and len(poss_numbers) != 1 and count == 1:
			possibilities[row_index][col_index] = [number]

def naked_pair_check(poss_array):
	for numbers in poss_array:
		occurances = poss_array.count(numbers)

		if occurances == 2 and len(numbers) == 2:
			return(numbers)
				
def remove_naked_pair_numbers(row_index, col_index, numbers, possibilities):
	for number in numbers:
		if number in possibilities[row_index][col_index] and possibilities[row_index][col_index] != numbers and len(possibilities[row_index][col_index]) > 1:
			possibilities[row_index][col_index].remove(number)


def pointing_pair_check(row_index, col_index, poss_array_row, poss_array_square, possibilities):
	sectioned_array = [poss_array_row[x:x+3] for x in range(0, len(poss_array_row), 3)]
	for number in range(1, 10):
		counts = []
		for section in sectioned_array:
			counts.append(sum(numbers.count(number) for numbers in section))

		if sum(counts) == 2 and 1 not in counts:
			sections_with_number = []
			for section in sectioned_array:
				if number in section:
					sections_with_number.append(section)
			
			print(poss_array_row)
			print(poss_array_square)
			print(sections_with_number)
			print(number)

			#if sum(numbers.count(number) for numbers in poss_array_square) > 2:
			#	print(poss_array_row, poss_array_square, i)

def remove_pointing_pair_numbers():
	return
