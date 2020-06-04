import numpy as np

def square_splitter(array):
	squares = []

	for i in range(3):
		for j in range(3):
			increments = [j*3, i*27]
			increment = sum(increments)

			indices_list = [0,1,2,9,10,11,18,19,20]
			indices = [x+increment for x in indices_list]

			numbers = []

			for k in indices:
				numbers.append(np.ravel(array)[k])

			squares.append(numbers)

	return(squares)