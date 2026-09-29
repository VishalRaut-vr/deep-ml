def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		result = []
		for row in matrix:
			total = 0
			for x in row:
				total += x
			result.append(total/len(row))
		return result
	
	elif mode == 'column':
		rows = len(matrix)
		cols = len(matrix[0])

		result = []

		for j in range(cols):
			total = 0
			for i in range(rows):
				total += matrix[i][j]
			result.append(total/rows)
		return result

	else:
		return []