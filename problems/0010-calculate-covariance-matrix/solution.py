def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	n_features = len(vectors)
	n_obs = len(vectors[0])

	means = []
	
	for features in vectors:
		means.append(sum(features) / n_obs)

	cov_matrix = [[0.0] * n_features for _ in range(n_features)]

	for i in range(n_features):
		for j in range(n_features):

			cov = 0.0

			for k in range(n_obs):
				cov += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])

			cov_matrix[i][j] = cov / (n_obs-1)
	
	return cov_matrix