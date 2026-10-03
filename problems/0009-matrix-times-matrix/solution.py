def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:
    
    # Get dimensions
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    
    # Check compatibility: columns of a must equal rows of b
    if cols_a != rows_b:
        return -1
    
    # Initialize result matrix with zeros
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            row.append(0)
        result.append(row)
    
    # Perform matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    
    return result