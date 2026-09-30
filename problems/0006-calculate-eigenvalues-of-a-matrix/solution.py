import math

def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return []
    
    n = len(matrix)
    
    if n == 1:
        return [float(matrix[0][0])]
    
    if n == 2:
        a, b = matrix[0][0], matrix[0][1]
        c, d = matrix[1][0], matrix[1][1]
        
        trace = a + d
        det = a * d - b * c
        discriminant = trace * trace - 4 * det
        
        if discriminant < 0:
            return [trace / 2.0]
        
        sqrt_disc = math.sqrt(discriminant)
        lambda1 = (trace + sqrt_disc) / 2.0
        lambda2 = (trace - sqrt_disc) / 2.0
        
        return [lambda1, lambda2]   # ✅ Larger first, no sorting
    
    return []