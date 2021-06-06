import sys
import numpy
import scipy


def version():
    print("{}\n{}\n{}\n", sys.version, numpy.version, scipy.version)
    numpy.matrix.transpose()