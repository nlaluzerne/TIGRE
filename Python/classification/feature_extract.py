import numpy as np
from fAndrew import rgbProcData
from inference import infer as fCarter

# TODO: read in images and extract features
# f and fc are expected to be file paths
def carter_f(f, fc):
    return list(fCarter([f])[0]) + list(fCarter([fc])[0])

# TODO: read in images and extract features
# f and fc are expected to be file paths
def andrew_f(f, fc):
    return rgbProcData(f) + rgbProcData(fc)

def all_f(f, fc):
    return carter_f(f, fc) + andrew_f(f, fc)
