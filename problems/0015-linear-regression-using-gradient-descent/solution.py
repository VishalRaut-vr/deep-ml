import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    # Your code here: implement gradient descent
    for _ in range(iterations):
        # 1. Predict
        y_pred = X @ theta                 # (m, 1)
        
        # 2. Compute error
        error = y_pred - y                 # (m, 1)
        
        # 3. Compute gradient
        gradient = (1 / m) * (X.T @ error) # (n, 1)
        
        # 4. Update weights
        theta = theta - alpha * gradient   # (n, 1)
    return theta.flatten()