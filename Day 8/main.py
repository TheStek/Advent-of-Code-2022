import numpy as np

with open('input.txt', 'r') as file:
	data = file.read().split('\n')


data_mat = np.array(list(map(lambda x: list(map(int, x)) , filter(lambda x: x != '', data))))



with open('test.txt', 'r') as file:
	test_data = file.read().split('\n')


test_data_mat = np.array(list(map(lambda x: list(map(int, x)) , filter(lambda x: x != '', test_data))))

print(test_data_mat)

def check_array(arr):
	max_height = -1
	res = []
	for item in arr:
		if item <= max_height:
			res.append(0)
		else:
			res.append(1)
			max_height = item
	return res

def left(arr):
	return check_array(arr)

def right(arr):
	arr_rev = np.flip(arr)
	return np.flip(check_array(arr_rev))


left_visibility = np.apply_along_axis(left, 1, data_mat)
right_visibility = np.apply_along_axis(right, 1, data_mat)

top_visibility = np.apply_along_axis(left, 1, data_mat.T).T
bottom_visibility = np.apply_along_axis(right, 1, data_mat.T).T


visibility_map = left_visibility + right_visibility + top_visibility + bottom_visibility


print(np.count_nonzero(visibility_map))



# Part 2

from functools import reduce



def get_matrix_scores(mat = data_mat, verbose = False):
	def visible_trees(r, c):
		height = mat[r][c]

		scores = []

		# check upwards
		row = r-1
		scores.append(0)
		tallest = height
		while row >= 0:
			scores[-1] += 1
			if mat[row][c] < tallest:
				tallest = max(mat[row][c], tallest)
				row -= 1
				

			else:
				break

		# check downwards
		row = r+1
		scores.append(0)
		tallest = height
		while row < r_max:
			scores[-1] += 1
			if mat[row][c] < tallest:
				tallest = max(mat[row][c], tallest)
				row += 1
			else:
				break

		# check left
		col = c-1
		scores.append(0)
		tallest = height
		while col >= 0:
			scores[-1] += 1
			if mat[r][col] < tallest:
				
				tallest = max(mat[r][col], tallest)
				col -= 1
			else:
				break

		# check right
		col = c+1
		scores.append(0)
		tallest = height
		while col < c_max:
			scores[-1] += 1
			if mat[r][col] < tallest:
				
				tallest = max(mat[r][col], tallest)
				col += 1
			else:
				break

		if verbose:
			print(r, c, height,  scores)

		return reduce(lambda x, y: x*y, scores)


	r_max, c_max = mat.shape

	visibility_scores = []

	for i in range(r_max):
		for j in range(c_max):
			visibility_scores.append(visible_trees(i, j))


	print(max(visibility_scores))

get_matrix_scores(data_mat, False)