def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	result = []

	if mode == 'row':
		for row in matrix:
			total = 0
			for i in row:
				total += i
			result.append(total/len(row))
		return result
	
	elif mode == 'column':
		rows = len(matrix)
		cols = len(matrix[0])

		for j in range(cols):
			total = 0
			for i in range(rows):
				total += matrix[i][j]
			result.append(total/rows)
		return result
	else:
		return []