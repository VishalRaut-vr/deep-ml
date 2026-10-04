def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_observations = len(vectors[0])
    
    # Step 1: Compute means for each feature
    means = []
    for feature in vectors:
        means.append(sum(feature) / n_observations)
    
    # Step 2: Compute covariance matrix
    cov_matrix = [[0.0] * n_features for _ in range(n_features)]
    
    for i in range(n_features):
        for j in range(n_features):
            # Covariance between feature i and feature j
            cov = 0.0
            for k in range(n_observations):
                cov += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
            
            # Divide by (n - 1) for sample covariance
            cov_matrix[i][j] = cov / (n_observations - 1)
    
    return cov_matrix