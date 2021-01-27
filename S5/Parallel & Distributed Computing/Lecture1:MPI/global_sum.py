#!/usr/bin/env python
from mpi4py import MPI
import sys
import numpy

world_size = MPI.COMM_WORLD.Get_size()
world_rank = MPI.COMM_WORLD.Get_rank()

current_source = 0
dest = 0
global_sum = 0
rank_count = 0
comm = MPI.COMM_WORLD
sums = numpy.zeros((world_size))

print(sums)

for rank_count in range(world_size):
    current_source = world_rank
    comm.send(world_rank, dest=dest, tag=0)
    sums[world_rank] = comm.recv(source=0, tag=0)
    rank_count = rank_count + 1

while rank_count != world_size:
    received_value = comm.recv(source=current_source, tag=0)
    global_sum = global_sum + received_value
    print(global_sum)
