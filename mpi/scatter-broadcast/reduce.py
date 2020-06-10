from mpi4py import MPI
from numpy import arange, zeros

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = arange(3, dtype=float) * (rank + 1)
buffer = zeros(3, float)

n = comm.reduce(rank, op=MPI.SUM, root=0)  # returns the value
if rank == 0:
    data[1] = 100
comm.Reduce(data, buffer, op=MPI.SUM, root=0)  # in-place modification
print(f'{rank}: {buffer} {data}')
