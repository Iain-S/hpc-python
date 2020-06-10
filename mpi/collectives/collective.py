from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4, 'Number of MPI tasks has to be 4.'

if rank == 0:
    print('First collective:')


def case1(in_data, out_data):
    comm.Scatter(in_data, out_data, root=0)

    assert out_data[0] == 0 + rank * 2
    assert out_data[1] == 1 + rank * 2
    for elem in out_data[2:]:
        assert elem == -1
    print('case1 passed')


def case2(in_data, out_data):
    pass

    if rank == 1:
        assert (out_data == np.array([0, 1, 8, 9, 16, 17, 24, 25])).all(), out_data
    else:
        for elem in out_data:
            assert elem == -1
    print('case2 passed')


cases = {1: case1, 2: case2}

for i in range(1, 3):
    # Create some data in 0 and send it to the other tasks
    data_size = size * 2
    if rank == 0:
        data = np.arange(data_size, dtype=int)
    else:
        data = np.zeros(data_size, dtype=int)
    comm.Bcast(data, root=0)
    assert data[0] == 0 and data[size * 2 - 1] == size * 2 - 1
    print('  Task {0}: {1}'.format(rank, data))

    # Prepare data vectors ..
    data = data + (rank * data_size)
    # .. and receive buffers
    buff = np.full(data_size, -1, int)

    cases[i](data, buff)
