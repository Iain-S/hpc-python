from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
ntasks = comm.Get_size()

data = np.empty(100000, dtype=float)
if rank == 0:
    # send only
    array = np.zeros(100000)
    comm.Isend(array, dest=1)
elif rank == ntasks - 1:
    # receive only
    recv_result = comm.Irecv(data, source=rank - 1)
    recv_result.wait()
    print(f'rank={rank}, elem={data[0]}')
else:
    array = np.empty(100000)
    array.fill(rank)

    send_result = comm.Isend(array, dest=rank + 1)
    recv_result = comm.Irecv(data, source=rank - 1)
    send_result.wait()
    recv_result.wait()
    print('rank={}, data={}'.format(rank, data[0]))
    # send_result.wait()
