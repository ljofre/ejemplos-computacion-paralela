from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank

xg = np.array(comm.allgather(rank)) + rank

my_matrix = comm.gather(xg, root=0)

if rank == 0:
    print np.array(my_matrix)