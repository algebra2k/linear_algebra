import numpy as np

if __name__ == '__main__':
    """matrix of A"""
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    """matrix of B"""
    B = np.array([[11, 22, 33, 44], [55, 66, 77, 88], [99, 110, 120, 130]])
    """vector of B"""
    x = np.array([1, 1, 2])

    print("A = {} B ={}".format(A, B))

    print("2 * {} = {}".format(A, 2 * A))

    print("{} * {} = {}".format(A, x, A * x))

    print("A.shape = {}, B.shape = {}".format(A.shape, B.shape))

    print(A.T.T)

    print(A.dot(B))