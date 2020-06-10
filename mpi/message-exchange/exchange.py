from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

data = np.empty(100000, dtype=float)
if rank == 0:
    comm.send({'rank': 0.0}, dest=1)
    received = comm.recv(source=1)
    print('rank={}, received={}'.format(rank, received))

    array = np.zeros(100000)
    comm.Send(array, dest=1)
    comm.Recv(data, source=1)
    print(f'rank={rank}, elem={data[0]}')
elif rank == 1:
    # reversing the order of send and recv does not deadlock
    # comm.send({'rank': 1.1}, dest=0)
    received = comm.recv(source=0)
    comm.send({'rank': 1.1}, dest=0)
    print('rank={}, received={}'.format(rank, received))

    array = np.ones(100000)
    # reversing the order of Send and Recv results in deadlock
    # comm.Send(array, dest=0)
    comm.Recv(data, source=0)
    print(f'rank={rank}, elem={data[0]}')
    comm.Send(array, dest=0)
