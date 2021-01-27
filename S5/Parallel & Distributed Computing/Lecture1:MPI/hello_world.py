#!/usr/bin/env python

from mpi4py import MPI

world_size = MPI.COMM_WORLD.Get_size()
world_rank = MPI.COMM_WORLD.Get_rank()

print("Hello World from rank %d out of %d processes."
      % (world_rank, world_size))
      
