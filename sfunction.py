"""
Function to produce the S function as defined in the 
'Simplicial variances, potentials and Mahalanobis distances' paper. 
See chapter 3.2 for definition.

S(k, covariance) = 
q(k, covariance, eigenvalues)/elementarysymmetric(k,eigenvalues)

Needed to produce k-Simplicial distance. 
distance = (x1 - x2)^T * S * (x1- x2)
"""

import efunction
import qfunction

def s(k, covariance):
    
    """
    Function to find the S matrix as defined in chapter 3.2.

    Input:
        - k, the value chosen for the k-Simplicial distance
        - covariance, the covariance matrix

    Output: 
        - smatrix, the S matrix
    """

    import numpy as np 

    eigenvalues = np.linalg.eigvals(covariance)

    smatrix = qfunction.q(k, covariance, eigenvalues)/efunction.elementarysymmetric(k,eigenvalues)

    return smatrix


