import numpy as np


def LUDecomposition (A):
    L = np.zeros(np.shape(A),np.float64)
    U = np.zeros(np.shape(A),np.float64)
    acc = 0
    L[0,0]=1
    for i in np.arange(len(A)):

        for k in range(i,len(A)):

            for j in range(0,i):
                acc += L[i,j]*U[j,k]
            U[i,k] = A[i,k]-acc


            for m in range(k+1,len(A)):
                if m==k:
                    L[m,k]=1
                else:

                    z = (A[m,k]-acc)
                    t = z / U[k,k]
                    L[m,k] = t
            acc=0
    return (L,U)


A = np.array([[6.0, -1, -2],
              [-4, 12, 3],
              [-4, -2, 18]])
L,U = LUDecomposition(A)
print(L)
print(U)