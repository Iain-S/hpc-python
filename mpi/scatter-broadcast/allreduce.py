from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = arange(10 * size, dtype=float) * (rank + 1)
buffer = empty(size * 10, float)

n = comm.allreduce(rank, op=MPI.SUM)  # returns the value

comm.Allreduce(data, buffer, op=MPI.SUM)  # in-place modification
