cimport numpy as np 
import numpy as np

np.import_array()

from libc.stdlib cimport malloc, free 

cdef extern from "numpy/arrayobject.h":
    void PyArray_ENABLEFLAGS(np.ndarray arr, int flags)
    void PyArray_CLEARFLAGS(np.ndarray arr, int flags)

cdef extern from "POCS_TV.hpp":
    cdef void pocs_tv(float* img, float* dst, float alpha, long*image_size, int maxIter)

def minimiseTV(np.ndarray[np.float32_t,ndim=3] img, float angle, int maxiter):
    cdef np.npy_intp size_img[3]
    size_img[2]= <np.npy_intp> img.shape[2]
    size_img[1]= <np.npy_intp> img.shape[1]
    size_img[0]= <np.npy_intp> img.shape[0]
    
    cdef long c_size[3]
    c_size[0]=<long>size_img[0]
    c_size[1]=<long>size_img[1]
    c_size[2]=<long>size_img[2]

    cdef float* c_imgout = <float*> malloc(size_img[0] *size_img[1] *size_img[2]* sizeof(float))
    cdef float* c_img = <float*> img.data
    cdef np.npy_intp c_maxiter = <np.npy_intp> maxiter
    cdef float c_angle = <float> angle
    pocs_tv(c_img,c_imgout,c_angle,c_size,c_maxiter)
    imgout = np.PyArray_SimpleNewFromData(3, size_img, np.NPY_FLOAT32, c_imgout)
    PyArray_ENABLEFLAGS(imgout, np.NPY_OWNDATA)

    return imgout
