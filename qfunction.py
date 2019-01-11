"""
Function to produce the q function as defined in the 
'Simplicial variances, potentials and Mahalanobis distances' paper. 
See chapter 3.2 for definition.

Needed to produce the S function in the k-Simplicial distance. 
"""
import efunction

def q(k, covariance, eigenvalues):
    """
    Find the q value as defined in chapter 3.2. 

    Input: (see paper for notation)
        - k, the value chosen for the k-Simplicial distance
        - covariance, the covariance matrix
        - eigenvalues, the eigenvalues of the covariance matrix

    Output: 
        - qvalue
    """
    import numpy as np 

    qvalue = 0

    for i in range(k):
        product = ((-1)**(i))*efunction.elementarysymmetric(k-i-1, eigenvalues)*(np.linalg.matrix_power(covariance,i))
        qvalue = qvalue + product
    
    return qvalue