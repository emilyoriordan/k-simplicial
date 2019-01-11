"""
Function to produce the elementary symmetric function as defined in the 
'Simplicial variances, potentials and Mahalanobis distances' paper. 

Needed to produce the S function in the k-Simplicial distance. 

"""
import itertools

def elementarysymmetric(k,eigenvalues):

    """
    Find the elementary symmetric function for a list of values and a given k.

    Input: (see paper for notation)
        - k, the degree of the symmetric function
        - eigenvalues, the set of eigenvalues for the covariance matrix

    Output:
        - evalue, the elementary symmetric function value
    """
    if k == 0:
        evalue = 1
    else:
        subscripts = []
        for subscript, _ in enumerate(eigenvalues):
            subscripts.append(subscript)

        combinationsofsubscripts = list(itertools.combinations(subscripts,k))
        
        product = 1 
        evalue = 0
        for combination in combinationsofsubscripts:
            for subscript in range(k):
                product = product * eigenvalues[combination[subscript]]
            evalue += product
            product = 1 

    return evalue 

