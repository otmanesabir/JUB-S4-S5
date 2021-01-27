#!/usr/bin/env python
from mpi4py import MPI

import iohelper as io
import time

def add_vecs(x, y, M, comm):
    local_M = int(M / comm.Get_size())

    z = x
    for i in range(local_M):
        z[i] = z[i] + y[i]
        
    return z


def dot_product(x,y, M, comm):
    local_M = int(M / comm.Get_size())
    
    local_sum = 0
    for i in range(local_M):
        local_sum = local_sum + x[i]*y[i]

    sum = comm.allreduce(local_sum) 
    return sum


def mat_vec_mult(A,x, M, N, comm):
    local_M = int(M / comm.Get_size())

    global_x = comm.allgather(x)
    global_x = [item for sublist in global_x for item in sublist]
    
    y = [0]*local_M
    for i in range(local_M):
        y[i] = 0
        for j in range(N):
            y[i] = y[i] + A[i*N+j]*global_x[j]
    return y


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

reps = 10

#--------------------------------------------
# Benchmarking sum of two vectors
#-------------------------------------------- 

M=1024*1024

time_sum = 0.0

for i in range(reps):
    y1,M = io.fill_random_vec(M, comm)
    y2,M = io.fill_random_vec(M, comm)

    comm.barrier()
    time1 = time.perf_counter()
    y3 = add_vecs(y1, y2, M, comm)
    time2 = time.perf_counter()
    comm.barrier()
    time_sum = time_sum + (time2 - time1)

time_sum = time_sum / reps

print("Elapsed time: %lf\n" % time_sum)


# #--------------------------------------------
# # Benchmarking dot product of two vectors
# #-------------------------------------------- 

# M=1024*1024

# time_sum = 0.0

# for i in range(reps):
#     y1,M = io.fill_random_vec(M, comm)
#     y2,M = io.fill_random_vec(M, comm)

#     comm.barrier()
#     time1 = time.perf_counter()
#     sum = dot_product(y1, y2, M, comm)
#     time2 = time.perf_counter()
#     comm.barrier()
#     time_sum = time_sum + (time2 - time1)

# time_sum = time_sum / reps

# print("Elapsed time: %lf\n" % time_sum)


# #--------------------------------------------
# # Benchmarking matrix vector product
# #-------------------------------------------- 

# M = 1024
# N = 1024

# time_sum = 0.0

# for i in range(reps):
#     x,M = io.fill_random_vec(N, comm)
#     A,M,N = io.fill_random_mat(M, N, comm)

#     comm.barrier()
#     time1 = time.perf_counter()
#     y = mat_vec_mult(A, x, M, N, comm)
#     time2 = time.perf_counter()
#     comm.barrier()
#     time_sum = time_sum + (time2 - time1)

# time_sum = time_sum / reps

# print("Elapsed time: %lf\n" % time_sum)


