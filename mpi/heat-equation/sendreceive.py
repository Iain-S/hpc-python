from mpi4py import MPI
from numpy import arange, empty

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

arr = empty((2, 10))
arr.fill(rank)

if rank == 0:
    comm.Sendrecv(arr[1], dest=1, recvbuf=arr[0], source=1)
else:
    comm.Sendrecv(arr[0], dest=0, recvbuf=arr[1], source=0)

print(f'rank: {rank} arr:{arr}')
