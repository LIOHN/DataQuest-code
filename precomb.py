from numba.pycc import CC 
from numba import int32, jit,prange
import numpy

cc = CC('finalCsvSearch2')
cc.verbose = True

@cc.export('fastcomb',int32[:,:](int32[:,:], int32[:,:],int32[:,:], int32[:,:]))
def comb(gold, oil,wheat,iron):

    result = numpy.zeros_like(gold)

    for i in range(991):
        for j in range(991):
            num = 0
            for ii in range(10):
                for jj in range(10):
                    num += gold[i+ii, j+jj] * 20
                    num += oil[i+ii, j+jj] * 22
                    num += wheat[i+ii, j+jj] * 8
                    num += iron[i+ii, j+jj] * 11

            result[i, j] = num
    return result


#fastcomb = jit(double[:,:](double[:,:], double[:,:],double[:,:], double[:,:]))(comb)
#@jit(double[:,:](double[:,:], double[:,:],double[:,:], double[:,:]))

if __name__ == "__main__":
    cc.compile()