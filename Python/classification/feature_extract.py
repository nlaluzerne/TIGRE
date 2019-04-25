import numpy as np
from fAndrew import rgbProcData
from inference import infer as fCarter
from temperature_processing import temp_proc as natalie_f

# TODO: read in images and extract features
# f and fc are expected to be file paths
def carter_f(f, fc):
    return list(fCarter([f])[0]) + list(fCarter([fc])[0])

# TODO: read in images and extract features
# f and fc are expected to be file paths
def andrew_f(f, fc):
    return rgbProcData(f) + rgbProcData(fc)

def all_f(f, fc, temp_matrix):
    return carter_f(f, fc) + andrew_f(f, fc) + natalie_f(temp_matrix)
