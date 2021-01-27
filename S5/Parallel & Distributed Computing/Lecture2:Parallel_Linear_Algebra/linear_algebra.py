#!/usr/bin/env python
from mpi4py import MPI

import iohelper as io

def add_vecs(x, y, M, comm):
    z = x
    i = comm.Get_rank() * (M / comm.size())
    j = comm.Get_rank() * (M / comm.size())
    for i in range(j):
        z[i] = z[i] + y[i]
    return z
            

# x_p1  +  y_p1 = z_p1   <- P1
# x_p2  +  y_p2 = z_p2   <- P2



def dot_product(x,y, M, comm):
    sum = 0
    for i in range(M):
        sum = sum + x[i]*y[i]
    return sum


def mat_vec_mult(A,x, M, N, comm):
    y = [0.0]*M
    for i in range(M):
        y[i] = 0
        for j in range(N):
            y[i] = y[i] + A[i*N+j]*x[j]
    return y


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

y1,M = io.read_vec_from_file('y1.csv',comm)
y2,M = io.read_vec_from_file('y2.csv',comm)
x,N = io.read_vec_from_file('x.csv',comm)
A,M,N = io.read_mat_from_file('A.csv',comm)

print(rank, y1)

io.print_vec(x, N, comm)
io.print_vec(y1, M, comm)
io.print_mat(A, M, N, comm)

y3 = add_vecs(y1, y2, M, comm)
io.print_vec(y3,M,comm)

# prod = dot_product(y1, y2, M, comm)
# print(prod)

# y = mat_vec_mult(A, x, M, N, comm)
# io.print_vec(y,M,comm)

