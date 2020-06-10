from mpi4py import MPI
from numpy import arange, zeros

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = arange(10, dtype=float) * (rank + 1)
buffer = zeros(size * 10, float)

n = comm.gather(rank, root=0)  # returns the value
comm.Gather(data, buffer, root=0)  # in-place modification
print(f'{rank}: {n} {type(n)} {buffer[size-1]}')
