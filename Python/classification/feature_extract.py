import numpy as np

# TODO: read in images and extract features
# f and fc are expected to be file paths
def carter_f(f, fc):
    # TODO: Read in files

    # TODO: Extract features
    features = [1.0, 2.0]

    return features

# TODO: read in images and extract features
# f and fc are expected to be file paths
def andrew_f(f, fc):
    # TODO: Read in files

    # TODO: Extract features
    features = [2.0, 3.0]

    return features

def all_f(f, fc):
    return carter_f(f, fc) + andrew_f(f, fc)
