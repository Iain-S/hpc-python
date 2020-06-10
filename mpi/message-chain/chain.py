from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
ntasks = 9  # should have used Get_size() instead of hard-coding
assert rank <= ntasks - 1

data = np.empty(100000, dtype=float)
if rank == 0:
    # send only
    array = np.zeros(100000)
    comm.Send(array, dest=1)
elif rank <= ntasks - 2:
    array = np.empty(100000)
    array.fill(rank)

    # apparently, this won't block
    comm.Sendrecv(array, rank + 1, recvbuf=data)
    print('rank={}, data={}'.format(rank, data[0]))
else:
    # receive only
    comm.Recv(data, source=ntasks - 2)
    print(f'rank={rank}, elem={data[0]}')

comm.barrier()

# or, we can use PROC_NULL as a target for the last process and
# a source for the first
if rank == 0:
    src = MPI.PROC_NULL
else:
    src = rank - 1

if rank == ntasks - 1:
    tgt = MPI.PROC_NULL
else:
    tgt = rank + 1

arr = np.empty(100, dtype=float)
arr.fill(rank)
data = np.empty(100, dtype=float)
comm.Sendrecv(arr, dest=tgt, recvbuf=data, source=src)
print(f"rank:{rank} recv:{data[0]}")
