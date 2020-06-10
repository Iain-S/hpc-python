from mpi4py import MPI
from numpy import arange, empty, zeros

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    a = arange(20, dtype=float)
else:
    a = None
# broadcast our array to all of the other processes
a = comm.bcast(a, root=0)
# a = a * rank
aloc = empty(20, dtype=float)
# Scatter/Gather to/from the other processes
comm.Alltoall(a, aloc)
print(f'{rank}: {aloc}')
