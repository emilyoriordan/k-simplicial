"""
Function to find distances in the form

(x1 - x2)^T * MATRIX * (x1 - x2)

"""

def distance(x1, x2, matrix):

    A = np.matmul(np.matmul(np.transpose(x1 - x2),matrix),(x1-x2))

    return A