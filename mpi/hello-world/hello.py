from mpi4py import MPI

communicator = MPI.COMM_WORLD

rank = communicator.Get_rank()
size = communicator.Get_size()

print('I am {} of {}'.format(rank, size))
